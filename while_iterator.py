# pets = [ 'dog', 'cat', 'bird', 'dog' ]
# while "dog" in pets:
#     pets.remove("dog")
# print(pets)

# names = ["John", "Michael", "David"]
# while names:
#     name = names.pop()
#     print(f"welcome to our group {name}")

#
response = {}

while True:
    name = input("Enter your name: ")
    if name == "end":
        break
    vote = input("Enter your vote: ")
    response[name] = vote
print(response)

for key, val in response.items():
    print(f"{key} Wants to vote {val.title()}")