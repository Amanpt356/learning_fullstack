class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name of Student : ", self.name)
        print("Marks :")
        for key , value in self.marks.items():
            print(f"\t{key}   : {value}")
    def total_marks(self):
        print("Total Marks : ",sum(self.marks.values()))
    def update_marks(self, subject, new_marks):
        self.marks[subject] = new_marks

student1 = Student("Aman" , {"English" : 50 , "Hindi" : 45})
student2 = Student("Ahan" , {"English" : 40 , "Hindi" : 49})

student1.display()
student2.display()

student1.update_marks("English" ,48)
student1.display()
student1.total_marks()


        