import os


def write(filename):
    writing = True
    while writing == True:
        with open(f"{filename}.txt", "a"):
            date = input("What is the date of this item? (Day of the month) ")

def file_exists(filename):
    exists = os.path.isfile(f"{filename}.txt")
    return exists

def user_choice(answer, filename, month):
    if answer.lower() == ("y") or ("yes"):
        write(filename)
    elif answer.lower() == ("n") or ("no"):
        return
    else:
        etc = True
        while etc == True:
            new_answer = input(f"Sorry, your answer couldn't be recognized. Would you like to add an item to your planner for {month}? (y/n)")
            user_choice(new_answer, filename, month)

def main():
    filename = input("What would you like to name your planner file? (exclude file extension) ")
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    exists = file_exists(filename)
    while exists == True:
        filename = input("A file with this name already exists. what would you like to rename your planner? (exclude file extension) ")
        exists = file_exists(filename)
    for month in months:
        answer = input(f"Would you like to add any items to your planner for {month}? (y/n) ")
        user_choice(answer, filename, month)



if __name__ == "__main__":
    main()
