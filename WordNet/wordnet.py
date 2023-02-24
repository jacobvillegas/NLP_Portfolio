from nltk.corpus import wordnet as wn
from fpdf import FPDF
import nltk
import math
from nltk.book import text4
#nltk.download('punkt')
#nltk.download('popular')
from nltk.wsd import lesk
from nltk.corpus import sentiwordnet as swn


# Create a text file
# text_file = open('wordnet.txt', 'a')
# text_file.write("WordNet is a corpus created at Princeton University used in Natural Language Processing.\
#                  Wordnet provides a functionality in which is a part thesaurus, dictionary that finds synonyms\
#                  nouns and their hierarchy. Provided with Morphy function, WordNet can find the base meaning of\
#                  words and  has aid in the finding the lemma of words.")
# text_file.close()

# Use of Free PDF  --- Question 1
pdf_file = FPDF()
pdf_file.add_page()

file = open('WordNet.txt', 'r')
pdf_file.set_font("Arial", size=12)

# # create PDF
# for sentences in file:
#     pdf_file.cell(500,11, txt=sentences, ln=1, )
# pdf_file.output('WordNet.pdf')

noun = 'telephone'  # please note that I originally used thesaurus,but it yielded no examples.
verb = 'walk'   # please note that I originally used the verb created, however it providded no heiarchy

print("\n Synsets of the noun ='Telephone' :\n")
# -----QUESTION 2-----------
# Output Synets
syn = wn.synsets(noun)[0]
syn_list = wn.synsets(noun)
print(syn_list)
print(' ')

# -----QUESTION 3----------
# definition
print('Definition of Noun', syn.definition())
# Example
example = syn.examples()
print('Here is an example', example)
# Lemmas
lemma = syn.lemmas()
print('Here are the lemmas: ', lemma)

# Heiarchy
hyper = lambda s: s.hypernyms()
print("Hiearchy", list(syn.closure(hyper)))
print("WordNet seems to organize noun from a base entity, towards a more specific definition of the object.\
        In this case the telephone starts an entity, then tow a specific tangible object, to an instrument\
         and finally a specialized electronic  instrument.")

print(" -----VERBS______________")

# -------QUESTION 4 ------------
hyper = syn.hypernyms()[0]
hypo = syn.hyponyms()[0]
mero = syn.member_meronyms()
holo = syn.member_holonyms()
anto = syn.lemmas()[0].antonyms()

print('Hypernyms:', hyper)
print('Hyponyms:', hypo)
print("Meronyms:", mero)
print('Holonyms:', holo)
print('Antonyms:', anto)

# -----QUESTION 5----------
# Output Verb - Synets
verb_syn = wn.synsets(verb)[0]
verb_syn_list = wn.synsets(verb)
print(verb_syn_list)

# -----QUESTION 6----------
# definition
print('Definition of Verb: ', verb_syn.definition())
# Example
example = verb_syn.examples()
print('Here is an example', example)
# Lemmas
lemma = verb_syn.lemmas()
print('Here are the lemmas: ', lemma)

# Hierarchy using Dr. Mazidi elegent form to obtain
hyper = lambda s: s.hypernyms()
print("Hierarchy:", list(verb_syn.closure(hyper)))
print("The hierarchy of verbs has the base entity at the bottom similar to the nouns, which turns into an abstraction\
       to the past tense of the verb, and finally to an action and in this case a specifeid action -locomotion. Thus,\
        the hierarchy stems from a base to a more concrete action.")

# ------Question 7------------
print(" ")
print("-----The use of NLTK Morphy on different forms of the word  walk----")
print("Morphy on 'walked' :")
print(wn.morphy('walked'))
print("Morphy Utilized on the word 'walking' :")
print(wn.morphy('walking', wn.VERB))


# -----QUESTION 8 -------------------
word1 = wn.synsets("resembling")
word2 = wn.synsets("comparable")
print('Synset for Resembling: ', word1)
print('Synset for Comparable: ', word2)
wu_palmer = wn.wup_similarity(word1[0], word2[0])
print('Wu Palmer Score', wu_palmer)

# Use of Lesk Algorithm
for synset in wn.synsets('similar'):
    print(synset, synset.definition())


sent1 = ['The', 'daughter', 'resembles' 'her', 'mother' '.']
print('\nAll Lesk Synset for resembles in a sentence:' )
print(lesk(sent1, 'resembles'))


print("\nThe Wu Palmer Score for the words resembling and comparable is exactly 1/3, which seems a little low,\
however, it does show there is a significant correlation between the chosen words.The Lesk algorithm\
supports the sentence provided with the correct Synset as expected.\n")


# -------QUESTION 9 --------------
print("SentiWordNet is a NLP resource that provides a means for opinion mining or sentiment analysis.  It is a lexical\
resource that provides a positive, negative or objective score. This could be used in social media mining, product ratings\
and other applications by which human behavior might be deduced electronically.\n")

emotional_word = 'doomed'
print("The Sentiment Score for the Synset of the word 'Doomed': ")
senti_list = list(swn.senti_synsets(emotional_word))
for element in senti_list:
    print(element)

senti_sentence = "The Super Bowl halftime show has been uncharacteristically surprising the past few years."
print('An Example of onf sentiment analysis on the sentanece:\n')
print("\t", senti_sentence)
# adapted from Dr. Mazidi's website
neg = 0
pos = 0
obj = 0
word_tokens = senti_sentence.split()
for token in word_tokens:
    syn_list = list(swn.senti_synsets(token))
    if syn_list:
        syn = syn_list[0]
        neg += syn.neg_score()
        pos += syn.pos_score()
        obj += syn.obj_score()

print("neg: \tpos: \tobjective:")
print(neg, '\t', pos, '\t', obj)
print("\nThe Scores indicate that the sentence was overall objective, however, had higher positive elements, over\
minimal negative sentiment. Given if this were a Tweet or poll given to the NFL, they could gauge this along with\
other opinions to change their approach in the Superbowl halftime show, or utilize this for marketing")

# -------QUESTION 10------------------
print(" ")
print("Collocations are a pair or small grouping of words that appear together. As noted in linguistics a \
collocation is a habitual juxtaposition with greater frequency or chance.\n ")
print("\nThe following are the Collocations of the Inaugural Address:")
print(" ")
text4.collocations()
print("  ")
text = ' '.join(text4.tokens)

print("Calculation of the PMI of the Collocation of 'Federal Government")

corpora_len = len(set(text4))
collocation = text.count('Federal Government') / corpora_len
print("p(Federal Government) = ", collocation)
first_word = text.count('Federal') / corpora_len
print("p(Federal) = ", first_word)
second_word = text.count('Government') / corpora_len
print('p(Government) = ', second_word)
pmi = math.log2(collocation / (first_word * second_word))
print('pmi = ', pmi)
