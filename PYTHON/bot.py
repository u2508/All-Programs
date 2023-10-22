from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import json
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize chatbot
bot = ChatBot(
    'Master Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///chatbot_database.db',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.98
        },
        {
            'import_path': 'chatterbot.logic.TimeLogicAdapter',
        },
    ]
)

knowledge_base_file = 'knowledge_base.json'
custom_responses_file = 'custom_responses.json'
conversation_file = 'conversation_data.json'  # Add the path to your conversation dataset JSON file

# Function to train the chatbot
def train_bot(chatbot):
    try:
        with open(knowledge_base_file, 'r') as file:
            knowledge_base = json.load(file)
        
        with open('conversation.json', 'r') as file:
            convo = json.load(file)

        list_trainer = ListTrainer(chatbot)

        for item in knowledge_base.keys():
            
            list_trainer.train([item,knowledge_base[item]])

        for key in convo.keys():
            list_trainer.train(convo[key])

        # Load conversation dataset and train the chatbot
        with open(conversation_file, 'r') as file:
            conversation_data = json.load(file)

        for message_data in conversation_data:
            sender = message_data.get("sender")
            message = message_data.get("message")

            if sender and message:
                list_trainer.train([sender, message])

        ChatterBotCorpusTrainer(chatbot).train("chatterbot.corpus.english")
        
        logger.info("Chatbot trained successfully.")
    
    except Exception as e:
        logger.error(f"Error training the chatbot: {e}")

# Function to load custom responses from a JSON file
def load_custom_responses():
    try:
        with open(custom_responses_file, 'r') as file:
            custom_responses = json.load(file)
        return custom_responses
    except FileNotFoundError:
        logger.warning("Custom responses file not found.")
        return {}
    except Exception as e:
        logger.error(f"Error loading custom responses: {e}")
        return {}

# Function to save custom responses to a JSON file
def save_custom_responses(custom_responses):
    try:
        with open(custom_responses_file, 'w') as file:
            json.dump(custom_responses, file, indent=4)
        logger.info("Custom responses saved successfully.")
    except Exception as e:
        logger.error(f"Error saving custom responses: {e}")

# Function to customize the chatbot's responses
def customize_bot(chatbot):
    custom_responses = load_custom_responses()
    
    try:
        while True:
            question = input("Enter a question to customize (or 'exit' to finish): ")
            
            if question.lower() == 'exit':
                break
            
            response = input("Enter the custom response: ")
            
            custom_responses[question] = response

        save_custom_responses(custom_responses)
        
        list_trainer = ListTrainer(chatbot)
        
        for question, response in custom_responses.items():
            list_trainer.train([question, response])

        logger.info("Custom responses added successfully.")
    
    except Exception as e:
        logger.error(f"Error customizing bot responses: {e}")

# Function to interact with the chatbot
def main():
    try:
        name = input("Enter Your Name: ")
        print(f"Hello, {name.capitalize()}! How can I assist you today?")
        
        retrain_ask = input("Would you like to retrain the bot with added commands? (yes/no): ")
        
        if retrain_ask.lower() in ('yes', 'y'):
            train_bot(bot)

        customize_ask = input("Would you like to customize the bot's responses? (yes/no): ")
        
        if customize_ask.lower() in ('yes', 'y'):
            customize_bot(bot)

        while True:
            request = input(f"{name.capitalize()}: ")
            
            if request.lower() in ('bye', 'exit'):
                print('Bot: Goodbye!')
                break
            else:
                response = bot.get_response(request)
                print('Bot:', response)

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
