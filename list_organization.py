nums = [2,5,3,7,4,6,9,8,1]
nums.sort()  #permenently sorting
print(nums)

nums = [2,5,3,7,4,6,9,8,1]
# sorted_value = sorted(nums)
sorted_value = sorted(nums, reverse=True) #reverse value
print(nums)
print(sorted_value) #copying sorting

bikes = ["honda", "suzuki", "dukati", "busa"]
bikes.sort()
print(bikes)
bikes.sort(reverse=True)
print(bikes)

bikes = ["honda", "suzuki", "dukati", "busa"]
bikes.reverse() #just reverse not sorting
print(bikes)
print(len(bikes)) #value counting