from school import School
import random

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1,100)


class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}  # {"Eng" : 70}
        self.subject_grade = {} # {"Eng":  "A"}
        self.grade = None

    def calculate_final_grade(self):
        sum = 0
        gpa = 0.00
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade) # 5.00
            sum += point
        if sum == 0:
            gpa = 0.00
            self.grade = "F"
        else:
            gpa = sum / len(self.subject_grade) # 6 / 2
            self.grade = School.value_to_grade(gpa)
        return f"{self.name} Final Grader : {self.grade} with GPA = {gpa:.2f}\n"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
