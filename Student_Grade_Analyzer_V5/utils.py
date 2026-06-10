import logging
from validator import (
    validate_name,
    validate_duplicate,
    validate_marks
)
from student import Student
def get_menu_choice():
    while True:
        try:
            choice = input("Enter your choice: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= 13:
                return choice
            print("Invalid choice. Please enter a number between 1 and 13.")
        except ValueError as e:
            print(e)
def add_students(students):
    try:
        n = int(input("How many students do you want to add? "))
    except ValueError:
        print("Please enter a valid number.")
        return
    for _ in range(n):
        try:
            name = input("Enter student name: ")
            validate_name(name)
            validate_duplicate(name,students)
            marks = list(map(float,input("Enter marks separated by space: ").split()))
            if not marks:
                raise ValueError("Marks cannot be empty.")
            for mark in marks:
                validate_marks(mark)
            student = Student(name,marks)
            students.append(student)
            logging.info(f"Student {name} added successfully.")
        except (ValueError, TypeError) as e:
            print(f"Input error: {e}")
def view_students(students):
    if not students:
        print("No students to display.")
        return
    for student in students:
            student.display()
def topper(students):
    if not students:
            print("No students to evaluate.")
            return
    top_student = max(students, key=lambda s: s.average())
    print("Topper:")
    top_student.display()
def search_students(students):
    name = input("Enter student name to search: ").strip()
    found_students = [student for student in students if student.name.lower() == name.lower()]
    if found_students:
        for student in found_students:
            student.display()
    else:
        print("Student not found.")
def total_students(students):
    print(f"Total number of students: {len(students)}")
def class_average(students):
    if not students:
        print("No students to calculate average.")
        return
    total_avg = sum(student.average() for student in students) / len(students)
    print(f"Class Average: {total_avg:.2f}")
def delete_student(students):
    try:
        name = input("Enter student name to delete: ").strip()
        validate_name(name)
        for i, student in enumerate(students):
            if student.name.lower() == name.lower():
                del students[i]
                logging.info(f"Student {name} deleted successfully.")
                return
        print("Student not found.")
    except ValueError as e:
        print(e)
def update_student(students):
    try:
        name = input("Enter student name to update: ").strip()
        validate_name(name)
    except ValueError as e:
        print(e)
        return
    for student in students:
        if student.name.lower() == name.lower():
            try:
                new_name = input("Enter new name (leave blank to keep current): ").strip()
                if new_name:
                    validate_name(new_name)
                    for s in students:
                        if (s != student and s.name.lower() == new_name.lower()):
                            raise ValueError("Student name already exists.")
                    student.name = new_name
                new_marks_input = input("Enter new marks separated by space (leave blank to keep current): ").strip()
                if new_marks_input:
                    new_marks = list(map(float, new_marks_input.split()))
                    for mark in new_marks:
                        validate_marks(mark)
                    student.marks = new_marks
                logging.info("Student updated successfully.")
            except ValueError as e:
                print(f"Invalid input: {e}")
            return
    print("Student not found.")
def sort_students(students):
    if not students:
        print("No students to sort.")
        return
    students.sort(key=lambda s: s.name)
    print("Students sorted by name successfully.")
def highest_lowest(students):
    if not students:
        print("No students to evaluate.")
        return
    highest_student = max(students, key=lambda s: s.average())
    lowest_student = min(students, key=lambda s: s.average())
    print("Highest Average:")
    highest_student.display()
    print("Lowest Average:")
    lowest_student.display()