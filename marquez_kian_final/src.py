import os


def file_exists(filename):
    exists = os.path.isfile(f"{filename}.txt")
    return exists

def main():
    filename = input("What would you like to name your planner file? (exclude file extension) ")
    exists = file_exists(filename)
    if exists == True:
        user_ans = input("A file with this name already exists, would you like to continue? (y/n) ")
        if user_ans.lower == ("y") or ("yes"):
            pass
        if user_ans.lower == ("n") or ("no"):
            new_filename = input("What would you like to rename your planner file? (exclude file extension) ")
            file_exists(new_filename)
    if exists == False:
        pass



if __name__ == "__main__":
    main()
