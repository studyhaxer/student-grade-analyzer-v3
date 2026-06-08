import json
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return 'A+'
        elif avg >= 80:
            return 'A'
        elif avg >= 70:
            return 'B'
        elif avg >= 60:
            return 'C'
        elif avg >= 50:
            return 'D'
        elif avg >= 40:
            return 'E'
        else:
            return 'F'
    def display(self):
        print(f"Name: {self.name} | Marks: {self.marks} | Average: {self.average():.2f} | Grade: {self.grade()}")
def add_students(students):
    try:
        n = int(input("How many students do you want to add?"))
        for i in range(n):
            name = input("Enter student name: ").strip()
            if not name:
                print("Student name cannot be empty. Please try again.")
                continue
            marks = list(map(int, input("Enter marks separated by space: ").split()))
            if not marks:
                print("Marks cannot be empty. Please try again.")
                return
            for mark in marks:
                if mark < 0 or mark > 100:
                    print("Marks should be between 0 and 100. Please try again.")
                    continue
            student = Student(name, marks)
            students.append(student)
            print(f"Student {name} added successfully.")
    except ValueError:
        print("Invalid input. Please enter a number.")
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
def save_students(students, filename="students.json"):
    std_data = []
    for student in students:
        std_data.append({
            "name": student.name,
            "marks": student.marks
        })
    with open(filename, 'w') as file:
        json.dump(std_data, file, indent=4)
    print("Students saved successfully.")
def load_students(students, filename="students.json"):
    try:         
        with open(filename, 'r') as file:
            std_data = json.load(file)
            students.clear()    
            for std in std_data:
                student = Student(std["name"], std["marks"])
                students.append(student)
        print("Students loaded successfully.")
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error: File is corrupted or not valid JSON. Students not loaded.")
    except KeyError as e:
        print(f"Error: Missing expected field {e} in file. Students not loaded.")
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
    name = input("Enter student name to delete: ").strip()
    for i, student in enumerate(students):
        if student.name.lower() == name.lower():
            del students[i]
            print(f"Student {name} deleted successfully.")
            return
    print("Student not found.")
def main():
    students = []
    while True:
        print("\nStudent Grade Analyzer")
        print("1. Add Students")
        print("2. View Students")
        print("3. Topper")
        print("4. Save Students")
        print("5. Load Students")
        print("6. Search Students")
        print("7. Total Students")
        print("8. Class Average")
        print("9. Delete Students")
        print("10. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_students(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            topper(students)
        elif choice == '4':                
            save_students(students)
        elif choice == '5':
            load_students(students)
        elif choice == '6':
            search_students(students)
        elif choice == '7':
            total_students(students)
        elif choice == '8':
            class_average(students)
        elif choice == '9':
            delete_student(students)
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()