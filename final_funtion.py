
nums = list(range(1,101))
def list22(arr):
    arr[0] = 1000
    for i in range(0, len(arr)):
        arr[i] = arr[i] ** 2
    return arr

nums2 = list22(nums.copy())
print(nums2)