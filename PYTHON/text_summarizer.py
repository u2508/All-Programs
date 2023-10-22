import re
import nltk
import bs4 as bs
import urllib.request
import wikipedia as wk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('stopwords')

inputquery=input("enter topic:- ")
'''scraped_data = urllib.request.urlopen(f'https://en.wikipedia.org/wiki/%s',inputquery)
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text
    
data = open('dataset.txt', 'r', errors='ignore')
raw = data.read()
article_text = raw.lower()
'''
wk.set_lang('en')
article_text=wk.page(inputquery).summary
# Our next step is to normalize these sentences. Normalization is a process that converts a list of words to a more uniform sequence. This is useful in preparing the text for later processing. By transforming the words to a standard format, other operations are able to work with the data and will not have to deal with issues that might compromise the process.

#This step involves word tokenization, Removing ASCII values, Removing tags of any kind, Part-of-speech tagging, and Lemmatization.
'''
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
sentence_list = nltk.sent_tokenize(article_text)
stopwords = nltk.corpus.stopwords.words('english')
word_frequencies = dict()
for i in formatted_article_text.split(" "):
    if i not in stopwords:
        if i not in word_frequencies.keys():
            word_frequencies[i] = 1
        else:
            word_frequencies[i] += 1
maximum_frequncy = max(word_frequencies.values())
#print(formatted_article_text)
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 90:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)'''
print(article_text)