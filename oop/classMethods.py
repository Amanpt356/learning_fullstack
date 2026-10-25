class Employee:
    company = "Google"

    def __init__(self,name):
        self.name = name

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company


e1 = Employee("Aman")
e2 = Employee("Rahul")
print(e1.company)
print(e2.company)

Employee.change_company("Microsoft")
print(e1.company)
print(e2.company)

e1.company = "Anthropic"
print(e1.company)
print(e2.company)

Employee.change_company("Microsoft")
print(e1.company)


