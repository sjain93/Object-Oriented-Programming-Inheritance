class People:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hi my name is {}".format(self.name)

class Student(People):

    def __init__(self, student):
        super().__init__(student)

    def learn(self):
        return "I get it!"

class Instructor(People):

    def __init__(self, instructor):
        super().__init__(instructor)

    def teach(self):
        return "An object is an instance of a class"

nadia = Instructor('Nadia')
chris = Student('Chris')

print(nadia.greeting())
print(chris.greeting())

print(nadia.teach())
print(chris.learn())

print(chris.teach()) # this doesnt work because it is trying to access a function that lives on a parallel branch of the inheritance tree.
