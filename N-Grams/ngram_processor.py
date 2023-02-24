import pickle
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.util import ngrams

# file_open = open('LangId.train.Italian', 'r')
#
# sentence_list = []
# for line in file_open:
#     sentence_list.append(line.replace('\n', ""))
# print(sentence_list[:3])
# # print(len(sentence_list))

def preprocess(text):
    return [word.lower() for word in word_tokenize(text)]


def unigram_former(text):
    return list(ngrams(preprocess(text), 1))


def bigrams_former(text):
    return list(ngrams(preprocess(text), 2))


def create_dictionaries(file_location):
    file_open = open(file_location, 'r')
    text = file_open.read()
    unigrams = unigram_former(text)
    bigrams = bigrams_former(text)
    unigram_dictionary = {word: unigrams.count(word) for word in set(unigrams)}
    bigram_dictionary = {word: bigrams.count(word)for word in set(bigrams)}
    return [unigram_dictionary, bigram_dictionary]


def create_data():
    for f in ['LangId.train.Italian', 'LangId.train.English', 'LangId.train.French']:
        uni, bi = create_dictionaries(f)
        # print(uni)
        # print(bi)
        p = open(f + '_unigram_training.txt', 'wb')
        pickle.dump(uni, p)
        b = open(f + '_bigram_training.txt', 'wb')
        pickle.dump(bi, b)













