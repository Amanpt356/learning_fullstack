class Student:
    school = "CBSE"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        return f"Marks of {self.name} : {self.marks}"

    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school

    @staticmethod
    def valid_mark(mark):
        return 0 <= mark <= 100

student1 = Student("Aman" , 85)
print(student1.school)
details = student1.display()
print(details)
Student.change_school("Jyothi College")
print(student1.school)
print(Student.school)
print(Student.valid_mark(105)) 