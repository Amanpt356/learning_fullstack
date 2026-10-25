class laptop():
    def __init__(self , brand , ram):
        self.brand = brand
        self.ram = ram


lap1 = laptop("Dell" , 16)
lap2 = laptop("Apple" , 8)

print(lap1.brand)
print(lap1.ram)
print(lap2.brand)
print(lap2.ram)