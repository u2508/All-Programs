import nltk
import random
import string
import re
import unicodedata
import wikipedia as wk
from collections import defaultdict
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from spellchecker import SpellChecker

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('stopwords')

data = open('dataset.txt', 'r', errors='ignore')
raw = data.read()
raw = raw.lower()
sent_tokens = nltk.sent_tokenize(raw)
spell = SpellChecker()
stop_words = set(stopwords.words('english'))


# Our next step is to normalize these sentences. Normalization is a process that converts a list of words to a more uniform sequence. This is useful in preparing the text for later processing. By transforming the words to a standard format, other operations are able to work with the data and will not have to deal with issues that might compromise the process.

#This step involves word tokenization, Removing ASCII values, Removing tags of any kind, Part-of-speech tagging, and Lemmatization.

def Normalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    #word tokenization
    word_token = nltk.word_tokenize(text.lower().translate(remove_punct_dict))
    
    #remove ascii
    new_words = []
    for word in word_token:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    
    #Remove tags
    rmv = []
    for w in new_words:
        text=re.sub("&lt;/?.*?&gt;","&lt;&gt;",w)
        rmv.append(text)
        
    #pos tagging and lemmatization
    tag_map = defaultdict(lambda : wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV
    lmtzr = WordNetLemmatizer()
    lemma_list = []
    rmv = [i for i in rmv if i]
    for token, tag in nltk.pos_tag(rmv):
        lemma = lmtzr.lemmatize(token, tag_map[tag[0]])
        lemma_list.append(lemma)
    
    return lemma_list
welcome_input = ("hello", "hi", "greetings", "sup", "what's up","hey",)
welcome_response = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def welcome(user_response):
    for word in user_response.split():
        if word.lower() in welcome_input:
            return random.choice(welcome_response)
def generateResponse(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=Normalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    #vals = cosine_similarity(tfidf[-1], tfidf)
    vals = linear_kernel(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0) or "tell me about" in user_response:
        print("Checking Wikipedia")
        if user_response:
            robo_response = wikipedia_data(user_response)
            return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response#wikipedia search
def wikipedia_data(input):
    reg_ex = re.search('tell me about (.+)', input)
    try:
        if reg_ex:
            topic = reg_ex.group(1)
            wiki = wk.summary(topic, sentences=3)
            if "may refer to:" in wiki:
                return "Chatterbot: The topic is ambiguous. Can you provide more specific details?"
            return wiki
    except Exception as e:
        print("Error: Couldn't fetch Wikipedia data for the topic.")
        return None

def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)
    return sentiment_score['compound']
flag = True
conversation_history = []
user_name = None
print("My name is Chatterbot, and I'm a chatbot. If you want to exit, type Bye!")
while flag:
    user_response = input("What can I help you with today? ")
    user_response = user_response.lower()
    
    # Sentiment Analysis
    sentiment_score = get_sentiment(user_response)
    if sentiment_score < -0.2:
        print("Chatterbot: I'm sorry to hear that. Is there anything specific I can help you with?")
    
    # Multi-Turn Conversations
    if user_name:
        user_response = user_response.replace('your name', user_name)
    
    # Spell Checking
    words = nltk.word_tokenize(user_response)
    corrected_words = [spell.correction(word) if word not in stop_words else word for word in words]
    user_response = ' '.join(corrected_words)
    
    if user_response not in ['bye', 'shutdown', 'exit', 'quit']:
        if user_response in ['thanks', 'thank you']:
            flag = False
            print("Chatterbot: You are welcome.")
        else:
            if not user_name:
                user_name = user_response.split()[-1]  # Assume the last word is the name
                print(f"Chatterbot: Nice to meet you, {user_name}!")
            elif welcome(user_response) is not None:
                print("Chatterbot: " + welcome(user_response))
            else:
                response = generateResponse(user_response, conversation_history, user_name)
                if response:
                    print("Chatterbot: " + response)
                    conversation_history.append(user_response)
                else:
                    print("Chatterbot: I'm sorry, I couldn't understand your query. Can you please rephrase it?")
    else:
        flag = False
        print("Chatterbot: Bye!!!")
