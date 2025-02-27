import json
import os

class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {self.roll_number: {"name": self.name, "marks": self.marks}}

    @classmethod
    def from_dict(cls, data):
        roll_number, student_data = next(iter(data.items()))
        return cls(roll_number, student_data["name"], student_data["marks"])

class StudentDatabase:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    return [Student.from_dict({k: v}) for k, v in data.items()]
            else:
                return []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {self.filename}. Creating new database.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def save_students(self):
        try:
            data = {}
            for student in self.students:
                data.update(student.to_dict())
            with open(self.filename, "w") as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    def add_student(self, student):
        self.students.append(student)
        if self.save_students():
            print("Student record added successfully!")
        else:
            print("Student record addition failed.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("Student Records:")
        for student in self.students:
            print(f"Roll No: {student.roll_number}, Name: {student.name}, Marks: {student.marks}")

    def search_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Student Found: Name: {student.name}, Marks: {student.marks}")
                return
        print("Student not found.")

database = StudentDatabase()

while True:
    print("\nWelcome to Student Management System")
    print("1. Add Student Record")
    print("2. View Student Records")
    print("3. Search Student by Roll Number")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))
            student = Student(roll_number, name, marks)
            database.add_student(student)
        except ValueError:
            print("Error: Invalid marks. Marks must be an integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    elif choice == "2":
        database.view_students()

    elif choice == "3":
        roll_number = input("Enter Roll Number to search: ")
        database.search_student(roll_number)

    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")