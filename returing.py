# def power(num, pow):
#     return num ** pow
#
# final = power(2, 2)
#
# print(final)

first = input("Enter your first name: ")
last = input("Enter your last name: ")

def name_format(first_name, last_name):
    full_name = f"{first_name.title()} {last_name.title()}"
    return {
        "first" : first_name.title(),
        "last": last_name.title(),
        "full_name": full_name
    }
format = name_format(first, last)
print(format)