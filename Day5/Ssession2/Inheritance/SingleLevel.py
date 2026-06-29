class Dog:
    def sound():
        print("Bow Bow")
    def eat(self):
        print("Dog is eating.")
class Cat(Dog):
    def sound():
        print('Meow Meow')
#instance
d=Cat()
d.eat()
