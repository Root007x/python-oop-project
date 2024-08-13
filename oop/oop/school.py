class Student:
    def __init__(self, name,current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class
        
    def __repr__(self) -> str: # when print only object this information will be showed
        return f"Student name: {self.name}, class :  {self.current_class}, id : {self.id}"
        
class Teacher:
    def __init__(self,name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
        
    def __repr__(self):
        return f"Teacher  : {self.name}, Subject : {self.subject}, ID : {self.id}"
    
class School:
    def __init__(self,name) -> None:
        self.name = name
        self.teachers = []
        self.students = []
        
    def add_teacher(self,name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
        
    def enroll(self, name, fee):
        if fee < 6500:
            return "Not Enough Fee"
        else:
            id = len(self.students) + 1
            student = Student(name,"C",id)
            self.students.append(student)
            return f"{name} is enrolled with id : {id}, extra money {fee - 6500}"
    
    def __repr__(self) -> str:
        print("Welcome to", self.name)
        print("------------OUR TEACHER------------")
        for t in self.teachers:
            print(t)
            
        print("--------------OUR STUDENTS---------------")
        for s in self.students:
            print(s)
            
        return "ALL Done"
        


# alia = Student("Hasan",9,211011010)
# print(alia)

# ranbir = Teacher("Jomir Uddin", "English", 22022022)
# print(ranbir)

hero = School("Programming Hero")
hero.enroll("rani",6000)
hero.enroll("tom",8000)
hero.enroll("jacob",7600)

hero.add_teacher("Kabir","English")
hero.add_teacher("Shohag","Biology")

print(repr(hero))