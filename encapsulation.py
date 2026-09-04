class cars:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.__odometer = 0

    def print_cars_details(self):
        print(f"the car brand name is {self.brand}")
        print(f"the car model is {self.model}")
        print(f"the year is {self.year}")

    def get_odometer(self):
        return self.__odometer
    def set_odometer(self, mileages):
        if self.__odometer > mileages:
             print("You Can not roll back odometer")
        else:
            self.__odometer = mileages



the_car = cars("BMW", "I8", "2020")

the_car.print_cars_details()
print(the_car.get_odometer())
the_car.set_odometer(1000)
print(the_car.get_odometer())
the_car.set_odometer(50)
print(the_car.get_odometer())