import json
from utils.nlp_tools import parse_input

# Reading the data
with open ("data/knowladge_base.json") as file:
    data = json.load(file)


# model start here
print("Hello! I'm Voya, How can I help you Today? ")

run = True

while run:
    user_input = input("Enter Your message: ").lower() 

    # check for the user intent and entities to generate the desired output
    parsed = parse_input(user_input)

    if parsed["intent"] == "recommended_place":
        if "japan" in parsed["entities"] and "december" in parsed["entities"]:
            print("Japan is great in December! Try Kyoto and Sapporo.") 
        else:
            print("I'm still learning")

    elif user_input == "bye":
        print("Happy to help you, have a nice day!")
        run = False
    elif user_input in data:
        print(data[user_input])
    else:
        print("I don't know this yet :(")
        