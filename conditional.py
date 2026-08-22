# age = 15
# print(age)
#
# print(100==10009)
#
# print("walid".upper() != "walid")
#
# less_than_18 = age <= 18
# grater_than_100 = age >= 10
#
# print(less_than_18 and grater_than_100)

food = ["biriyani", "hotdog", "apple", "orrange", "lemon", "banana"]
fav = "hotdog"
sec_fav = "apple"
for i in food:
    if i in fav:
        print(f"i love {i.title()}")

    elif i in sec_fav:
        print(f"i also love {i.title()}")

    else:
        print(f"i don't love {i.title()}")