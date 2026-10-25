import os

ROOT = "project"
PLAN = ["project\\common\\data.txt", "project\\src\\README.md", "project\\src\\utils.py",
        "project\\src\\test.py", "project\\src\\main.py"]

def main():
    while True:
        menu()
        choice = input("Enter command: ")
        # needs validation
        if choice == "1":
            showplan()
        elif choice == "2":
            create_structure()
        elif choice == "3":
            showtree(ROOT)
        elif choice == "4":
            statistics(ROOT)
        elif choice == "5":
            saverecord()
        elif choice == "6":
            delete_structure()
        elif choice == "0":
            break
        else:
            print("Error 001: command not found")

def menu():
    print("=== Menu ===")
    print("1. Show Plan")
    print("2. Create Structure")
    print("3. Show File Tree")
    print("4. Show Stats")
    print("5. Save Record")
    print("6. Delete File Structure")
    print("0. Exit")

def showplan():
    print("-"*10)
    print(f"Contents:\n{"\n".join(PLAN)}")
    print(f"File count: {len(PLAN)}")

def create_structure():
    files = 0
    dirs = 0

    for path in PLAN:
        folder = os.path.dirname(path)
        filename = os.path.basename(path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
            dirs += 1
        if filename and not os.path.exists(path):
            with open(path, "w") as f:
                if ".py" in filename:
                    f.write(f"print(\"{filename}\")")
                else:
                    f.write(f"# {filename}\n")
            files += 1
    print(f"{files} files and {dirs} directories created")

def showtree(path):
    if not os.path.exists(path):
        print("Error 002: path not found")
        return
    for root, dirs, files in os.walk(path):
        print(root)

        if dirs == []:
            dirs = "no directories"
        else:
            dirs = ", ".join(dirs)
        if files == []:
            files = "no files"
        else:
            files = ", ".join(files)
        
        print(f"Directories: {dirs}, Files: {files}")
        print("-"*20)

def statistics(path):
    # project\main.py
    # 'project\\[]\\data.txt'
    # "project\\common\\data.txt"
    if not os.path.exists(path):
        print("Error 002: path not found")
        return
    sizecounter = 0
    for root, dirs, files in os.walk(path):
        for i in range(len(files)):
            sizecounter += os.path.getsize(f"{root}\\{files[i]}")
        
        print(f"{len(dirs)} directories and {len(files)} files in {root}")
    
    print(f"Sum of file sizes in {path}: {(sizecounter/1024):.2f} KB")

def saverecord():
    lines = []
    lines.append("=== REPORT ===")
    lines.append(f"Root directory: {ROOT}")

    if not os.path.exists(ROOT):
        print("Error 002: path not found")
        return
    sizecounter = 0
    for root, dirs, files in os.walk(ROOT):
        for i in range(len(files)):
            sizecounter += os.path.getsize(f"{root}\\{files[i]}")
        
        lines.append(f"{len(dirs)} directories and {len(files)} files in {root}")
    
    lines.append(f"Sum of file sizes in {ROOT}: {(sizecounter/1024):.2f} KB")

    try:
        with open("report.txt", "w") as file:
            file.write("\n".join(lines))
    except Exception as e:
        print(f"Error 003: program error {e}")

def delete_structure():
    prompt = input("Are you sure you want to delete all files and directories? (y/n)")

    if not yes_no_validation(prompt):
        print("Error 004: input is invalid")
    else:
        if prompt == "no" or prompt == "n":
            return
        if not os.path.exists(ROOT):
            print("Nothing to delete. Please create structure.")
            return
        for root, dirs, files in os.walk(ROOT, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        
        os.rmdir(ROOT)

def yes_no_validation(prompt):
    valid_prompts = ["y", "n", "yes", "no"]

    if prompt not in valid_prompts:
        return False
    return True

if __name__ == "__main__":
    main()
