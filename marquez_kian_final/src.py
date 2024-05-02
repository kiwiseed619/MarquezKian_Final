import os


def write(filename, month):
    writing = True
    answer = ()
    etc = False
    while writing == True:
        with open(f"{filename}.txt", "a") as file:
            date = input("What is the date of this item? (Day of the month)\n")
            title = input("What would you like to name this item?\n")
            start_time = input("Does this item have a start time?\nIf yes, enter a time. If no, press enter\n" )
            end_time = input("Does this item have an end time?\nIf yes, enter a time. If no, press enter\n")
            notes = input("Would you like to add any additional notes? If no, press enter.\n")
            if start_time == ("") and end_time == (""):
                file.write(f"{month}, {date}\n{title}\n")
            elif start_time == (""):
                file.write(f"{month}, {date}\n{title}\n{end_time}\n")
            elif end_time == (""):
                file.write(f"{month}, {date}\n{title}\n{start_time}\n")
            else:
                file.write(f"{month}, {date}\n{title}\n{start_time} - {end_time}\n")
            if notes == (""):
                pass
            else:
                file.write(f"{notes}\n")
            answer = input("Add another item? (y/n) ")
            if answer.lower() == ("y") or answer.lower() == ("y"):
                pass
            if answer.lower() == ("n") or answer.lower() == ("n"):
                file.write("===============================\n\n")
                writing = False
                return
            else:
                etc = True
                while etc == True:
                    new_answer = input(f"Sorry, your answer couldn't be recognized. Add another item? (y/n) ")
                    user_choice(new_answer, filename, month)
                    if new_answer.lower() == ("y") or new_answer.lower() == ("yes"):
                        etc = False
                        pass
                    if new_answer.lower() == ("n") or new_answer.lower() == ("no"):
                        file.write("===============================\n\n")
                        writing = False
                        return

def file_exists(filename):
    exists = os.path.isfile(f"{filename}.txt")
    return exists

def user_choice(answer, filename, month):
    if answer.lower() == ("y") or answer.lower() == ("yes"):
        write(filename, month)
        return
    if answer.lower() == ("n") or answer.lower() ==("no"):
        return
    else:
        etc = True
        while etc == True:
            new_answer = input(f"Sorry, your answer couldn't be recognized. Would you like to add an item to your planner for {month}? (y/n) ")
            user_choice(new_answer, filename, month)
            if new_answer.lower() == ("y") or new_answer.lower() == ("yes"):
                etc = False
                write(filename, month)
                return
            if new_answer.lower() == ("n") or new_answer.lower() == ("no"):
                return

def main():
    filename = input("What would you like to name your planner file? (exclude file extension) ")
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    answer = ()
    exists = file_exists(filename)
    while exists == True:
        filename = input("A file with this name already exists. what would you like to rename your planner? (exclude file extension) ")
        exists = file_exists(filename)
    for month in months:
        answer = input(f"\nWould you like to add any items to your planner for {month}? (y/n) ")
        user_choice(answer, filename, month)



if __name__ == "__main__":
    main()
