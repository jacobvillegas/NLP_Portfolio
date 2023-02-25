import string

import nltk.tokenize
from nltk import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
import pandas as pd

def create_txt_file(string, counter):
    files = 'file-number' + str(counter) + '.txt'
    new_file = open(files, 'x')
    for text in string:
        new_file.write(text)
    new_file.close()
    return new_file

# Function to Return an Array of Sentences, Word_tokens, and all non-Stopwords
def get_sentences_words(webpage):
    sentences = sent_tokenize(webpage)
    words = RegexpTokenizer(r"\w+")
    word_tokens = words.tokenize(webpage)
    long_words = [elements.lower() for elements in word_tokens if elements.isalpha() and len(elements) > 5]
    non_stop_words = [wrd for wrd in long_words if wrd not in stopwords.words("english")]
    return sentences, long_words, non_stop_words

 # function to read  a text file
def open_read(file):
    with open(file, 'r') as document:
        text_data = document.read()
    return text_data
#sanity check on on function
sent, wrdtkn, nswords = get_sentences_words(open_read('file-number0.txt'))
#print(sent[:10])
#print(wrdtkn[:10])
#print(nswords[:10])

#for each_sent in sent:
    #print(each_sent)


# Function to isolated unique lemma in text
def get_word_lemma(word_list):
    lemmatizer = WordNetLemmatizer()
    word_lemmas = [lemmatizer.lemmatize(tken) for tken in word_list]
    unique_lemma = word_list(set(word_lemmas))
    return unique_lemma


# TD-IDF
def obtain_tfidf(new_text):
    tdidf_vec = TfidfVectorizer(use_idf=True, stop_words='english')
    tfIdf = tdidf_vec.fit_transform(list(new_text))
    df = pd.DataFrame(tfIdf[0].T.todense(), index=tdidf_vec.get_feature_names_out(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)
    print(df.head(25))

# print(df["TF-IDF"].tolist())
# print(list(new_text.split(".")))


# def create_knowledge_base():
# empty lists and variables for later
text_files = []
knowledge_base = {}
counter = 0
# get file pattern
while counter <= 15:
    file_name = 'file-number' + str(counter) + '.txt'
    text_files.append(file_name)
    counter += 1
print(text_files)
impact_words = ['chatgpt', 'ai', 'help', 'work', 'like', 'business','job','data','writing', 'code']
data_files =[]
for file in text_files:
    with open(file, 'r') as f:
        data = f.read()
        sent, wrd, ns_wrd = get_sentences_words(data)
        #print(sent)
        for s in sent:
            for iw in impact_words:
                if iw in s.lower():
                    knowledge_base[iw] = s.lower()


print(knowledge_base)
print(len(knowledge_base))




        # file_sentences, wrd_tokens, ns_wrd_tokens  = get_sentences_words(data)
        # list_of_text =[]
        # for fs in file_sentences:

        # for [index] in range(len(file_sentences)):
        #     print(file_sentences[index])




        # print(file_sentences)
        # for sent_token in file_sentences:
        #     for word in impact_words:
        #        if word in sent_token.lower():
        #            knowledge_base[word] = sent_token






