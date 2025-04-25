import spacy

nlp = spacy.load("en_core_web_sm")



def identify_user_intent(user_input):
    if "go" in user_input or "where" in user_input or "travel" in user_input:
        return "recommended_place"
    
    if "hi" in user_input or "hello" in user_input or "thank you" in user_input or "good bye" in user_input or "bye" in user_input:
        return "greeting"
    
    if "weather" in user_input or "temperature" in user_input or "cold" in user_input or "hot" in user_input:
        return "weather_info"
    

def identify_entities(user_input):
    entitiy_list = []
    doc = nlp(user_input)
    for entitiy in doc.ents:
        entitiy_list.append(entitiy.text.lower())
    

    return entitiy_list






def parse_input(user_input):
    intent = identify_user_intent(user_input)
    entity = identify_entities(user_input)

    return {
        "intent": intent,
        "entities": entity
    }

dic = parse_input("does japan hot in december")
print(dic)