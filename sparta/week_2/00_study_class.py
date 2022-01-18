class Person:
    def __init__(self, param_name):
        self.name = param_name

    def talk(self):
        self.talk = print("Hi! My name is", self.name, "~~!")

person_1 = Person("A")
print(person_1.name)
person_2 = Person("B")
print(person_2.name)

person_1.talk()
person_2.talk()