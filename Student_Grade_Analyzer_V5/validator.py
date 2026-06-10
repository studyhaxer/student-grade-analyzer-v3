def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    elif len(name) < 2:
        raise ValueError("Name must contain atleast two Chracters. ")
def validate_marks(marks):
    if not isinstance(marks, (int, float)):
        raise TypeError("Marks must be numeric.")
    if marks < 0:
        raise ValueError("Marks cannot be negative.")
    if marks > 100:
        raise ValueError("Marks cannot exceed 100.")   
def validate_duplicate(name, students):
    for student in students:
        if student.name.lower() == name.lower():
            raise ValueError(
                "Student already exists."
            )
