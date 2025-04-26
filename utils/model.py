from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pickle

# Training data
training_sentence = [
    "Where should I go in Japan?",
    "Suggest me a place to visit in December.",
    "Which countries are best to travel?",
    "Can you recommend a destination?", 
    "I want to travel somewhere cold.",
    "Do I need a visa for Japan?",
    "Visa requirements for USA?",
    "Is visa needed to travel to Canada?",
    "What documents are needed for traveling?",
    "Tell me about visa rules.",
    "Hello",
    "Hi there",
    "Hey",
    "Good morning",
    "What's up?",
    "Goodbye",
    "Bye",
    "See you later",
    "Talk to you soon",
    "Catch you later",
    "How is the weather in Japan?",
    "Tell me the temperature in Paris.",
    "Is it cold in Canada right now?",
    "What's the weather like in Italy?",
    "Do I need warm clothes for Switzerland?"
]

# Correct labels
training_label = [
    "recommended_place",
    "recommended_place",
    "recommended_place",
    "recommended_place",
    "recommended_place",
    "visa_info",
    "visa_info",
    "visa_info",
    "visa_info",
    "visa_info",
    "greeting",
    "greeting",
    "greeting",
    "greeting",
    "greeting",
    "goodbye",
    "goodbye",
    "goodbye",
    "goodbye",
    "goodbye",
    "weather_info",
    "weather_info",
    "weather_info",
    "weather_info",
    "weather_info"
]

# Creating the vectorizer
vectorizer = TfidfVectorizer()

# Fit Transform the texts
x = vectorizer.fit_transform(training_sentence)

# Creating the encoder
encoder = LabelEncoder()
# Correct way to encode the labels
y = encoder.fit_transform(training_label)

# Creating and training the model
model = LogisticRegression()
model.fit(x, y)

# Save the model and files inside 'models/' folder
with open("model/intent_model.pkl", "wb") as file:
    pickle.dump(model, file)

with open('model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

with open('model/label_encoder.pkl', 'wb') as f:
    pickle.dump(encoder, f)