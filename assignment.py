# Student Record and Academic Management System
# Computational Thinking and Basic Programming

students = []


# Function to calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


# Function to add student
def add_student():
    print("\n--- Add Student ---")

    roll_no = input("Enter roll number: ").strip()

    # Check empty roll number
    if not roll_no:
        print("Roll number cannot be empty.")
        return

    # Check duplicate roll number
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this roll number already exists.")
            return

    name = input("Enter student name: ").strip()
    department = input("Enter department: ").strip()
    semester = input("Enter semester: ").strip()

    # Number of subjects
    try:
        number_of_subjects = int(input("Enter number of subjects: "))

        if number_of_subjects <= 0:
            print("Number of subjects must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    # Enter marks
    marks = []

    for i in range(number_of_subjects):

        while True:
            try:
                mark = float(
                    input(f"Enter marks for subject {i + 1} (0-100): ")
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    # Enter attendance
    while True:
        try:
            attendance = float(
                input("Enter attendance percentage (0-100): ")
            )

            if 0 <= attendance <= 100:
                break
            else:
                print("Attendance must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    # Calculate average and grade
    average = calculate_average(marks)
    grade = calculate_grade(average)

    # Create student record
    student = {
        "roll_no": roll_no,
        "name": name,
        "department": department,
        "semester": semester,
        "marks": marks,
        "attendance": attendance,
        "average": average,
        "grade": grade
    }

    # Store student
    students.append(student)

    print("\nStudent record added successfully.")


# Function to display one student
def display_student(student):

    print("\n---------------------------------------------")
    print("Roll Number :", student["roll_no"])
    print("Name        :", student["name"])
    print("Department  :", student["department"])
    print("Semester    :", student["semester"])
    print("Marks       :", student["marks"])
    print("Attendance  :", f"{student['attendance']:.2f}%")
    print("Average     :", f"{student['average']:.2f}")
    print("Grade       :", student["grade"])
    print("---------------------------------------------")


# Function to display all students
def display_records():

    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No student records available.")
        return

    for student in students:
        display_student(student)


# Function to search student
def search_student():

    print("\n--- Search Student ---")

    roll_no = input("Enter roll number to search: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:
            print("\nStudent found!")
            display_student(student)
            return

    print("Student record not found.")


# Function to calculate/display average
def average_menu():

    if len(students) == 0:
        print("No student records available.")
        return

    roll_no = input("Enter roll number: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:

            print(
                "Average marks:",
                f"{student['average']:.2f}"
            )

            return

    print("Student record not found.")


# Function to display grade
def grade_menu():

    if len(students) == 0:
        print("No student records available.")
        return

    roll_no = input("Enter roll number: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:

            print(
                "Grade:",
                student["grade"]
            )

            return

    print("Student record not found.")


# Function to display menu
def display_menu():

    print("\n==========================================")
    print("     STUDENT RECORD MANAGEMENT SYSTEM")
    print("==========================================")

    print("1. Add Student")
    print("2. Display Student Records")
    print("3. Search Student")
    print("4. Calculate Average Marks")
    print("5. Display Grade")
    print("6. Exit")

    print("==========================================")


# Main program
def main():

    while True:

        display_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":

            add_student()

        elif choice == "2":

            display_records()

        elif choice == "3":

            search_student()

        elif choice == "4":

            average_menu()

        elif choice == "5":

            grade_menu()

        elif choice == "6":

            print("\nThank you for using the Student Record Management System!")
            print("Program ended.")

            break

        else:

            print("Invalid choice!")
            print("Please enter a number between 1 and 6.")


# Program starts here
if __name__ == "__main__":
    main()