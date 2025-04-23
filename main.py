import json


# Reading the data
with open ("data/knowladge_base.json") as file:
    data = json.load(file)


# model start here
print("Hello! I'm Voya, How can I help you Today? ")

run = True

while run:
    user_input = input("Enter Your message: ").lower() 

    if user_input == "good bye":
        print("Happy to help you, have a nice day!")
        run = False
    elif user_input in data:
        print(data[user_input])
    else:
        print("I don't know this yet :(")
        