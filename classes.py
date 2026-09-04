class animals:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def print_name(self):
        print(f"the dogs name is {self.name}")

dog = animals("dog", "walid")
dog.print_name()

cat = animals("cage", "hilfigure")
cat.print_name()