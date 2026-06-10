
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        if not self.marks:
            return 0.0
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
    def __str__(self):
        return f"Name: {self.name} | Marks: {self.marks} | Average: {self.average():.2f} | Grade: {self.grade()}"
    def display(self):
        print(str(self))
    def to_dict(self):
        return {
            "name": self.name,
            "marks": self.marks
        }