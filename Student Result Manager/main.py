import json

FILE_PATH = "Student Result Manager/rsm.json"

def main():
    students = students_result()

    while True:
        print("\n-----Student Result Manager-----")
        print("1. View Students")
        print("2. Add Student")
        print("3. Check Result")
        print("4. Exit\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "3":
            check_result(students)
        elif choice == "4":
            print("GOODBYE!!")
            break
        else:
            print("Invalid choice. Please try again.")

def students_result():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return {"students": []}

def save_result(students):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(students, file)
    except:
        print("Couldn't save!!!")

def add_student(students):
    name = input("Enter the name of the student: ").strip()
    marks = input("Enter the marks of the student: ").strip()
    if marks:
        students["students"].append({"Name": name, "marks": marks})
        save_result(students)
        print("Student added.\n")
    else:
        print("Please provide the name of the student.")

def view_students(students):
    print()
    students_list = students["students"]
    if len(students_list) == 0:
        print("No students to Display")
    else:
        print("\n-----Students list-----")
        for idx, student in enumerate(students_list):
            print(f"{idx + 1}. {student['Name']}")

def check_result(students):
    view_students(students)
    print()
    try:
        students_list = students["students"]
        student_name = input("Enter the name of the student: ").strip()
        for student in students_list:
            if student["Name"].lower() == student_name.lower():
                print(f"Name - {student['Name']} | Marks - {student['marks']}")
                return
        print("Student doesn't exist!")
    except:
        print("Enter a valid name.")

main()