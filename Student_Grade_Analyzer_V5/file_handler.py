import logging
import json
from student import Student
def save_students(students, filename="students.json"):
    std_data = []
    for student in students:
        std_data.append(student.to_dict())
    try:
        with open(filename, 'w') as file:
            json.dump(std_data, file, indent=4)
        logging.info("Students saved successfully.")
    except Exception as e:
        logging.error(f"Error saving students: {e}")
def load_students(students, filename="students.json"):
    """Clears and repopulates the students list from a JSON file."""
    try:         
        with open(filename, 'r') as file:
            std_data = json.load(file)
            students.clear()    
            for std in std_data:
                student = Student(std["name"], std["marks"])
                students.append(student)
        logging.info("Students loaded successfully.")
    except FileNotFoundError:
        logging.error("Students file not found.")
    except json.JSONDecodeError:
        print("Error: File is corrupted or not valid JSON. Students not loaded.")
    except KeyError as e:
        print(f"Error: Missing expected field {e} in file. Students not loaded.")