from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom


school = School("Prgoti", "Dhaka")

eight = ClassRoom("Eight")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(ten)

karim = Student("Karim",eight)
rahim = Student("Rahim",eight)
sakib = Student("Sakib",ten)
fahad = Student("Fahad",ten)

school.student_admission(karim)
school.student_admission(rahim)
school.student_admission(sakib)
school.student_admission(fahad)


kalam = Teacher("Kalam Alil")
korim = Teacher("Korim Mia")
bidhar = Teacher("Bidhar Khan")

bangla = Subject("Bangla", kalam)
english = Subject("English",korim)
physics = Subject("Physics", bidhar)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(physics)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(physics)

eight.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)