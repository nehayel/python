class animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def print_f(self):
        print(f"the animal name is {self.name}")
dog = animal(type="dog", name="tommy")
dog.print_f()

cat = animal(type="cat", name="fuck")
cat.print_f()