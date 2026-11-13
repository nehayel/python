class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animals):
    def __init__(self, name, age, bread):
        super().__init__(name=name, age=age)
        self.bread = bread
    def bark(self):
        print(f"{self.name} is barking")
    def show_details_info(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")
        print(f"my bread is {self.bread}")
dog = Dog("Tommy", 45, "German Shepherd")

class Cat(Animals):
    def __init__(self, name, age):
        super().__init__(name=name, age=age)

    def sound(self):
        print(f"{self.name} say's mew mew...")
cat = Cat("pussy", 45)
cat.sound()