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

    elif parsed["intent"] == "greeting":
        print("Hey there how can I help you with your Travel plan today ?")

    elif parsed["intent"] == "weather_info":
        if "japan" in parsed["entities"] and "december" in parsed["entities"]:
            print("Yes Japan is cold in December")

    elif user_input in ["thanks", "thank you"]:
        print("You are Welcome 😊")  

    elif user_input in ["who are you", "what is your name"]:
        print("I'm Voya, your travel assistant bot 🧳✨")


    elif user_input == "bye":
        print("Happy to help you, have a nice day!")
        run = False

    elif user_input in data:
        print(data[user_input])
    else:
        print("Hmm. Im not sure how to respond to that")
        print("I don't know this yet, Would you like to teach me? (yes/no)")

        choice = input(">>> ").lower()
        if choice == "yes":
            print(f"Okey cool. How should i reply when someone say {user_input} ?")
            new_answer = input(">>> ")

            data[user_input] = new_answer
            with open("data/knowladge_base.json", "w") as file:
                json.dump(data, file, indent=2)
            
            print("Got it!, I'll Remember this for the next time 😊")
        
        else:
            print("No worries! Let's keep going....")
        