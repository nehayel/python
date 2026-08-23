cat= {
    "color": "black",
    "age": 18
}
print(cat)
print(cat["color"])

cat["eye_color"] = "blue"
print(cat)
del cat["color"]
print(cat.get("color", "no colors"))