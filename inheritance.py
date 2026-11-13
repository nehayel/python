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

class electricCar(cars):
    def __init__(self, brand, model, year):
        super().__init__(brand=brand, model=model, year=year)
        self.battery = 20

    def get_battery(self):
        return self.battery

    def set_battery(self, battery):
        if self.battery > battery:
            print("you can't roll it")
        else:
            self.battery = battery

tesla = electricCar("tesla", "model", year=2020)
tesla.set_battery(50)
print(tesla.get_battery())

tesla.set_battery(9)
print(tesla.get_battery())