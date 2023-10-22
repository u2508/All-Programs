from voicerecog_module import *
import tkinter as tk
from tkinter import filedialog
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from transformers import BartForConditionalGeneration, BartTokenizer
from spacy import load as spacy_load

nltk.download('punkt')

# Load English tokenizer, POS tagger, parser, NER, and word vectors
nlp = spacy_load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = set()
    for entity in doc.ents:
        if entity.text.strip() not in entities and entity.label_ in ["ORG", "PERSON", "GPE"]:
            entities.add(entity.text.strip())
    return entities

def clean_text(text):
    words = word_tokenize(text.lower())
    stopwords_list = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stopwords_list]
    return " ".join(words)

def calculate_sentence_scores(text):
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        words = [word for word in words if word.isalnum()]
        sentence_scores[sentence] = len(words)
    return sentence_scores

def generate_summary(text, max_sentences=20, max_words_per_sentence=30):
    cleaned_text = clean_text(text)
    entities = extract_entities(cleaned_text)
    
    #print("Entities:", ", ".join(entities) if entities else "No entities found.")
    
    sentence_scores = calculate_sentence_scores(text)
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max_sentences]
    
    summarized_text = " ".join(sorted_sentences)
    
    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)
    
    inputs = tokenizer(summarized_text, max_length=10000, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=max_sentences*max_words_per_sentence, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Example text for summarization



root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
data = open(file_path, 'r', errors='ignore')
raw = data.read()
input_text =raw.lower()


try:
    summary = generate_summary(input_text)
    print("\nSummarized Text:")
    print(summary)
except Exception as e:
    print("An error occurred:", e)
