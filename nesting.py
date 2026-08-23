# cat_1 ={
#     "name": "walid",
#     "age": 12,
#     "color": "orange",
# }
# cat_2 ={
#     "name": "neyal",
#     "age": 23,
#     "color": "Black",
# }
# cat_3 ={
#     "name": "tom",
#     "age": 34,
#     "color": "white",
# }
#
# cats = [cat_1,cat_2,cat_3]
# for cat in cats:
#     print(f"The cat {cat['name'].title()} color is {cat['color'].title()} ")


# menu = {
#     "pizza": ["mashroms", 'chicken', "chees","water"],
#     "burger": ["beef", "buns", "sose"]
# }
# # for item in menu:
# #     print(f"The ingridience of this {item} food off {menu[item]} ")
#
# fav_food = "burger"
#
# for food in menu:
#     if fav_food in food:
#         print(f"the ingredients of {food} ")
#         for ingredient in menu[food]:
#             print(f"\t {ingredient} ")


users = {
    "walid": {
        "first_name": "walid",
        "last_name": "Hossain",
        "email": "walidhossain179@gmail.com",
        "password": "343343"
    },
    "nehayel": {
        "first_name": "nehayel",
        "last_name": "Hossain",
        "email": "nehayel@gmail.com",
        "password": "rwettt32"
    },
    "junior": {
        "first_name": "junir",
        "last_name": "tabssim",
        "email": "junior@gmail.com",
        "password": "ef445"
    },
}

for user in users:
    info = users[user]
    for person in info:
        print(f"{person} is {info[person]} ")

