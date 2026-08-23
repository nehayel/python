# names = {
#     "nehayel": 24,
#     "mila": 13,
#     "toma": 23,
#     "walid": 25
#
# }
# print(names.keys())
# print(names.values())
#
# for i in names:
#     print(names[i])
#
# for f in names.values():
#     print(f)
#
# for m in names.keys():
#     print(m)
#
# for n, l in names.items():
#     print(n, l)

fav_lang = {
    "walid": "python",
    "nehayel": "cotlin",
    "mila": "C++",
    "toma": "java",
}

for k in fav_lang:
    print(f"{k.title()} loves {fav_lang[k].title()}")

for c,v in fav_lang.items():
    print(c)
    print(v)