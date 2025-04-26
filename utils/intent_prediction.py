import pickle

# 🔥 1. Load model/vectorizer/encoder ONCE
with open('model\\intent_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('model\\vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('model\\label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# 🔥 2. Start chat loop
print("Hello! I'm Voya. How can I assist you today?")

run = True
while run:
    user_input = input("You: ")

    # Vectorize + predict
    X_test = vectorizer.transform([user_input])
    y_pred = model.predict(X_test)
    predicted_intent = label_encoder.inverse_transform(y_pred)

    print(f"Predicted intent: {predicted_intent[0]}")

    if predicted_intent[0] == "goodbye":
        print("Goodbye! Safe travels! ✈️")
        run = False
