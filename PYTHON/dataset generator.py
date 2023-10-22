import json
import spacy
from textblob import TextBlob

# Load spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Function to extract sender and message content
def extract_sender_and_message(line):
    parts = line.strip().split(":")
    if len(parts) == 2:
        sender = parts[0].strip()
        message = parts[1].strip()
        return sender, message
    else:
        return None, None

# Function to analyze sentiment using TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment.polarity, sentiment.subjectivity

# Read the raw conversation data from a text file
with open("dataset1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Initialize variables for the JSON dataset
conversation_data = []

# Iterate through the lines of conversation data
for line in range( len(lines)):
    sender, message = extract_sender_and_message(lines[line])
    if sender and message:
        # Perform NLP tasks (e.g., named entity recognition, sentiment analysis) here if needed
        # For simplicity, we'll just analyze sentiment
        polarity, subjectivity = analyze_sentiment(message)

        # Create a dictionary for each message
        message_data = {
            "sender": sender,
            "message": message,
            "sentiment": {
                "polarity": polarity,
                "subjectivity": subjectivity
            }
        }

        # Append the message data to the conversation dataset
        conversation_data.append(message_data)
        print(line+1,"out of ",len(lines))

# Save the conversation data as a JSON file
with open("conversation_data.json", "w", encoding="utf-8") as json_file:
    json.dump(conversation_data, json_file, indent=4)

print("JSON dataset created successfully.")
