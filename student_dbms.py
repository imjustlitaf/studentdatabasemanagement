"""
Fields :- ['name','department','regno','dob','fathername','address','email','phone']
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Quit
"""

import csv
# Define global variables
student_fields = ['name', 'department', 'regno', 'dob', 'fathername', 'address', 'email', 'phone']
student_database = 'students.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    try:
        student_data = []
        for field in student_fields:
            value = input("Enter " + field + ": ")
            student_data.append(value)
        
        while "7107" not in student_data[2]:
            student_regno = input("Type the correct register number\nPlease write your Register number again: ")
            if len(student_regno) < 11:
                student_regno = input("YOur Register number is too short\nPlease write your Register number again: ")
            if len(student_regno) > 12:
                student_regno = input("Your Register number is too long\nPlease write your Register number again: ")
            student_data[2]=student_regno
        while "@" not in student_data[6]:
            student_email = input("Your email address must have '@' in it\nPlease write your email address again: ")
            if len(student_email) <= 6 :
                student_email = input("Your email address is too short\nPlease write your email address again: ")
            if "." not in student_email:
                student_email = input("Your email address must have '.' in it\nPlease write your email address again: ")
            student_data[6]=student_email
        while "." not in student_data[6]:
            student_email = input("Your email address must have '.' in it\nPlease write your email address again: ")
            if len(student_email) <= 6 :
                student_email = input("Your email address is too short\nPlease write your email address again: ")
            if "@" not in student_email:
                student_email = input("Your email address must have '@' in it\nPlease write your email address again: ")
            student_data[6]=student_email

        with open(student_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([student_data])

        print("Data saved successfully")
        input("Press any key to continue")
        return
    except KeyboardInterrupt:
        print ("Student not added")
    except EOFError:
        print ("Student not added")


def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n--------------------------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    name = input("Enter name to search: ")
    name = name.lower()
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if name == row[0].lower():
                    print("----- Student Found -----")
                    print("Name: ", row[0])
                    print("Department: ", row[1])
                    print("Reg No: ", row[2])
                    print("DOB: ", row[3])
                    print("Father's Name: ", row[4])
                    print("Address: ", row[5])
                    print("E-mail: ", row[6])
                    print("Phone: ", row[7])
                    break
        else:
            print("Student not found in our database")
    input("Press any key to continue")


def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    name = input("Enter name to update: ")
    name = name.lower()
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if name == row[0].lower():
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Student not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    name = input("Enter name to delete: ")
    name = name.lower()
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if name != row[0].lower():
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Name ", name, "deleted successfully")
    else:
        print("Student not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")