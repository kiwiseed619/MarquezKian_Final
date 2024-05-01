import os


def file_exists(filename):
    exists = os.path.isfile(f"{filename}.txt")
    return exists

def main():
    filename = input("What would you like to name your planner file? (exclude file extension) ")
    exists = file_exists(filename)
    while exists == True:
        filename = input("A file with this name already exists. what would you like to rename your planner? (exclude file extension) ")
        exists = file_exists(filename)
    with open(f"{filename}.txt", "w") as planner:
        print("next")



if __name__ == "__main__":
    main()
