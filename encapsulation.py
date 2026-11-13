class cars:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0

    def print_car_details(self):
        print(f"the car brand is {self.brand}")
        print(f"the model is {self.model}")
        print(f"the release year is {self.year}")

    def get_odometer(self):
        return self.__odometer
    def set_odometer(self, mileage):
        if self.__odometer > mileage:
            print("you can't roll it")
        else:
            self.__odometer = mileage

ford = cars(brand="Ford", model="Mustang", year=1964)
ford.print_car_details()
ford.set_odometer(1200)
print(ford.get_odometer())

ford.set_odometer(3000)
print(ford.get_odometer())
