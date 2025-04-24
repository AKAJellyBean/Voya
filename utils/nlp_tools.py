import spacy

nlp = spacy.load("en_core_web_sm")



def identify_user_intent(user_input):
    if "go" in user_input or "where" in user_input or "travel" in user_input:
        return "recommended_place"
    

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

dic = parse_input("good bye")
print(dic)