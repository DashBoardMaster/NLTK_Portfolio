import sys
import pickle
import re

# Amol Perubhatla
# AVP180003
# CS4395.001
# Professor Karen Mazidi

# This is the person class where we will store the data that we parse from the .csv


class Person:
    def __init__(self, line):
        # First we take the line input as a string, then strip and split it by comma and make it all lowercase
        last, first, mi, id, phone = line.strip().split(',')
        # Regex to fix weird characters from getting into my last name
        regex = re.compile('[^a-zA-Z]')
        self.last = ''.join([i for i in regex.sub(
            '', last) if i.isalpha()]).capitalize()

        self.first = first.capitalize()
        # If middle inital is missing then default to X if otherwise then take the input
        if len(mi) == 0:
            self.mi = "X"
        else:
            self.mi = mi.upper()

        # If the ID isn't in the right format then prompt the user to re-enter
        if (len(id) != 6):
            print("ID is invalid: ", id.upper())
            print("ID is two letters followed by 4 digits")
            self.id = input("Please enter a valid id: ").upper()
        else:
            self.id = id.upper()

        # Check if the phone number matches the expected format if not then prompt the user to re-enter

        match = re.search(r'\A[0-9]{3}-[0-9]{3}-[0-9]{4}', phone)

        if (match):
            self.phone = phone
        else:
            print(f"Phone " + str(phone) + " is invalid")
            print("Enter phone number in form 123-456-7890")
            self.phone = input("Enter phone number: ")

    # These are simple return definitions
    def first(self):
        return self.first

    def mi(self):
        return self.mi

    def last(self):
        return self.last

    def id(self):
        return self.id

    def phone(self):
        return self.phone

    # The display function that has our specific formatting
    def display(self):
        print("Employee ID:", self.id)
        print(self.first, self.mi, self.last)
        print(self.phone)
        print("\n")


def main():
    # Check if a sys arg was provided if not then give an error message and quit
    if len(sys.argv) > 1:
        data_path = sys.argv[1]
    else:
        print("Sys arg not provided.")
        quit()

    # Create the employee list dictionary
    employee_list = {}

    # Populate the employee list dictionary and check if there are duplicate keys if so then quit
    f = open(data_path, 'r')
    for line in f:
        tempPerson = Person(line)
        if (tempPerson.id not in employee_list):
            employee_list.update({tempPerson.id: tempPerson})
        else:
            print("Duplicate key error")
            quit()
    f.close()

    # Print the entire employee list dictionary
    print("\nEmployee List:\n")
    for i in employee_list:
        employee_list[i].display()

    # Pickle the employee list dictionary
    pickle.dump(employee_list, open('dict.p', 'wb'))
    dict_in = pickle.load(open('dict.p', 'rb'))

    # Print the pickled dictionary
    print("\nEmployee List:\n")
    for i in dict_in:
        dict_in[i].display()

    return employee_list


if __name__ == '__main__':
    main()
