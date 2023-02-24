import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer
#from nltk import *
text_file ='/Users/jacobvillegas/PycharmProjects/WordGuessGame-HW2/anat19.txt'


# # Function to read file and return text into a variable
# def open_read(file):
#     with open(file, 'r') as document:
#         text = document.read()
#     return text


# test = open_read(text_file)
# print(test)

def preprocess_get_words(sentence):
    tokenizer = RegexpTokenizer(r"\w+")
    word_tokens = tokenizer.tokenize(sentence)
    words = [elements.lower() for elements in word_tokens if elements.isalpha() and len(elements) > 5]
    words = [wrd for wrd in words if wrd not in stopwords.words("english")]
    return words

corpus = open_read(text_file)
refined = preprocess_get_words(corpus)
print(refined)