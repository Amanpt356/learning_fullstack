class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))

#We use @staticmethod when a function is related to the class \n
#  but doesn't need access to a particular object or the class itself.