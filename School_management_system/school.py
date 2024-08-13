class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}  # {"bangla" : teacher_object}
        self.classrooms = {}  # {"eight" : classroom_object}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        class_name = student.classroom.name
        self.classrooms[class_name].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return "A+"
        elif 70 <= marks < 80:
            return "A"
        elif 60 <= marks < 70:
            return "A-"
        elif 50 <= marks < 60:
            return "B"
        elif 40 <= marks < 50:
            return "C"
        elif 33 <= marks < 40:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            "A+": 5.00,
            "A": 4.00,
            "A-": 3.50,
            "B": 3.00,
            "C": 2.00,
            "D": 1.00,
            "F": 0.00,
        }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return "A+"
        elif 3.5 <= value < 4.50:
            return "A"
        elif 3.0 <= value < 3.5:
            return "A-"
        elif 2.5 <= value < 3.0:
            return "B"
        elif 2.0 <= value < 2.5:
            return "C"
        elif 1.0 <= value < 2.0:
            return "D"
        else:
            return "F"

    def __repr__(self):
        for key in self.classrooms.keys():
            print(key)

        print("All Students")
        result = ""
        for key, value in self.classrooms.items():
            result += f"----{key.upper()} Classroom Students"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)

        subject = ""
        for key, value in self.classrooms.items():
            subject += f"----{key.upper()} Classroom Subjects\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)

        print("Students Result")
        for key, value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.calculate_final_grade())
        return ""
