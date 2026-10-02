class Father:
    def __init__(self):
        self.age = 50
        self.name = "Bhagaban"
        self.gender = "male"

class Son(Father):
    def __init__(self):
        super().__init__()
        self.age = 25
        self.name = "pramod"
        self.gender = "male"

a=Father()
print(a.age)
print(a.name)
print(a.gender)
b=Son()
print(b.age)
print(b.name)
print(b.gender)