# Employee Attendance Tracker

import os

filename = "attendance.txt"

# Function to add a new employee
def add_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    with open(filename, "a") as file:
        file.write(f"{emp_id},{name},0\n")
    print(f"Employee {name} added successfully!\n")

# Function to mark attendance
def mark_attendance():
    emp_id = input("Enter employee ID: ")
    lines = []
    found = False
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == emp_id:
                data[2] = str(int(data[2]) + 1)
                found = True
            file.write(",".join(data) + "\n")
    if found:
        print("Attendance marked successfully!\n")
    else:
        print("Employee ID not found!\n")

# Function to view attendance report
def view_report():
    print("\nEmployee Attendance Report:")
    print("ID\tName\tDays Present")
    if not os.path.exists(filename):
        print("No records found.\n")
        return
    with open(filename, "r") as file:
        for line in file:
            emp_id, name, days = line.strip().split(",")
            print(f"{emp_id}\t{name}\t{days}")
    print()

# Function to delete an employee
def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    lines = []
    found = False
    if not os.path.exists(filename):
        print("No records found.\n")
        return
    with open(filename, "r") as file:
        lines = file.readlines()
    with open(filename, "w") as file:
        for line in lines:
            data = line.strip().split(",")
            if data[0] != emp_id:
                file.write(",".join(data) + "\n")
            else:
                found = True
    if found:
        print(f"Employee ID {emp_id} deleted successfully!\n")
    else:
        print("Employee ID not found!\n")

# Menu-driven program
while True:
    print("----- Employee Attendance Tracker -----")
    print("1. Add Employee")
    print("2. Mark Attendance")
    print("3. View Attendance Report")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_report()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Try again.\n")
