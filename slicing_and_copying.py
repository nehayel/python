nums = list(range(20,51))
print(nums)


# empty_list = []
# for num in range(10,21):
#     empty_list.append(nums[num])
# print(empty_list)

sliced_list = nums[10:21]
print(sliced_list)

#last 5 index
last_index = nums[-5:]
print(last_index)

#copyed list
copy_list = nums.copy()
copy_list[5]= 999
print(copy_list)