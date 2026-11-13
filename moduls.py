from inheritance import electricCar


tesla = electricCar("tesla", "aur", 2000)
tesla.set_battery(50)
print(tesla.get_battery())

tesla.set_battery(9)
print(tesla.get_battery())