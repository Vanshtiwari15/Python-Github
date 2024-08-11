class Employee:
    a = 1
    
    @classmethod
    def show(cls): # If we will use self then they show 45 as a value but after writting @classmethod and cls they will show 1
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()