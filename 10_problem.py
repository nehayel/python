# problem 1:
from encodings import zlib_codec

from practice_list import largest

names = ["John", "Michael", "David", "Alex"]
for k in names:
    print(k)

# problem 2:
numbers = [10, 20, 30, 40, 50]
sum = 0
for n in numbers:
    sum += n
print(sum)

# problem 3:
numbers = [10, 15, 20, 25, 30, 35]
for l in numbers:
    if l % 2 == 0:
        print(l)

# problem 4:
numbers = [45, 12, 89, 23, 67, 100, 34]
largest = numbers[0]
for m in numbers:
    if m > largest:
        largest = m
print(largest)

# problem 5:
names = ["John", "Michael", "David"]

while names:
    name = names.pop()
    print(name)

# problem 6:
student = {
    "name": "Walid",
    "age": 26,
    "country": "Bangladesh"
}
for k, v in student.items():
    print(f"{k}: {v}")

# problem 7:
student = {
    "name": "Walid",
    "age": 26
}
print(student)
student["country"] = "Bangladesh"
print(student)

# problem 8:
person = {
    "name": "John",
    "age": 30,
    "city": "London"
}
for k, v in person.items():
    print(v)

# problem 9:
odd = 0
even = 0
numbers = [10, 15, 22, 33, 40, 51, 60]
for p in numbers:
    if p % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"even: {even}")
print(f"odd: {odd}")

# problem 10:
students = {
    "John": 75,
    "Michael": 45,
    "David": 80,
    "Alex": 30
}
for name, marks in students.items():
    if marks >= 50:
        print(f"{name}: Pass")
    else:
        print(f"{name}: Fail")