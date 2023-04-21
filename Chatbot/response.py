# python libraries
import random
import json
import pickle


# NLP libraries
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

word_tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()

tags = []
words =[]
tagged_words = []


bot_interaction = open('intents.json').read()
intents = json.loads(bot_interaction)

bot_game = open('JEOPARDY_QUESTIONS1.json').read()
jeopardy = json.loads(bot_game)

# print(jeopardy[0])
entry = jeopardy[0]
print(entry['question'], '\n', entry['answer'])

for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = word_tokenizer.tokenize(pattern)
        words.extend(w)
        tagged_words.append((w, intent["tag"]))
        if intent["tag"] not in tags:
            tags.append(intent["tag"])

words = [lemmatizer.lemmatize(w.lower()) for w in words]

# list of words
words = sorted(list(set(words)))
tags = sorted(list(set(tags)))

pickle.dump(words,open('words.pkl', 'wb'))
pickle.dump(tags, open('tags.pkl', 'wb'))