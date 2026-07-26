#একটি list-এর সব সংখ্যার যোগফল বের করো।
numbers = [10, 20, 30, 40, 50]
summation = sum(numbers)
print(summation)

#একটি list-এর সবচেয়ে বড় সংখ্যাটি বের করো।
numbers = [8, 12, 45, 3, 19]
largest = max(numbers)
print(largest)

#একটি list-এর সবচেয়ে ছোট সংখ্যাটি বের করো।
numbers = [8, 12, 45, 3, 19]
minumum = min(numbers)
print(minumum)

#একটি list-এ কয়টি Even এবং কয়টি Odd সংখ্যা আছে তা বের করো।
numbers = [1, 2, 3, 4, 5, 6, 7]
even = 0
odd = 0
for num in numbers:
    if num % 2 ==0:
        even += 1
    else:
        odd += 1
print("even=", even)
print("odd=", odd)

#কোন built-in reverse() ব্যবহার না করে list উল্টো করে প্রিন্ট করো।
numbers = [1, 2, 3, 4, 5]
reverse_list = numbers[::-1]
print(reverse_list)

#একটি list থেকে duplicate value বাদ দিয়ে নতুন list তৈরি করো।
numbers = [1, 2, 2, 3, 4, 4, 5]
uniq_list = []
for num in numbers:
    if num not in uniq_list:
        uniq_list.append(num)
print(uniq_list)

#একটি list-এর দ্বিতীয় বড় সংখ্যাটি বের করো।
numbers = [10, 25, 8, 50,50, 42]
number = list(set(numbers))
number.sort()
print(number[-2])

#ইউজারের কাছ থেকে একটি সংখ্যা নিয়ে list-এ আছে কি না তা বের করো।
# numbers = [5, 10, 15, 20]
# user_input = int(input("Enter a number: "))
# if user_input in numbers:
#     print("found")
#
# else:
#     print("not found")


#দুটি list একসাথে যোগ করে নতুন list তৈরি করো।
list1 = [1, 2, 3]
list2 = [4, 5, 6]
marge_list = list1 + list2
print(marge_list)

#একটি list-এর সংখ্যাগুলোর Average বের করো।
numbers = [10, 20, 30, 40]
summation = sum(numbers)
length = len(numbers)
average = summation / length
print(average)