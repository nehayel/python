bikes = ["Honda", "yamaha", "suzuki"]
print(bikes)

bikes[0]= "hero"
print(bikes)

bikes.append("Dukati")  #append means added last position
print(bikes)

bikes.insert(2,"Honda") #index wise added
print(bikes)

del bikes[1]  #index wise delete
print(bikes)

bikes.pop()  #last position remove
print(bikes)

pop_value = bikes.pop(1) #index wise remove
print(bikes)

print(pop_value) #just pop method deleted item stored  not del method

print(bikes)

bikes.append("suzuki")
print(bikes)

bikes.remove("suzuki") #value name wise delete
print(bikes)