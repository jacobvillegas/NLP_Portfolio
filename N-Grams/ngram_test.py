from ngram_processor import *
import pickle


# function to open and read solution file
def get_solutions():
    file_open = open('LangId.sol', 'r')
    read = file_open.read()
    solutions = read.split()
    return [element for element in solutions if element.isalpha()]


#  correctness function
def corectness_check(solutions_file, my_sol):
   correct = []
   incorrect = []
   for index in range(len(solutions_file)):
       if solutions_file[index] == my_sol[index]:
          correct.append(my_sol[index])
       else:
        incorrect.append(my_sol[index])
   return correct, incorrect

# print(correct)
# print(incorrect)
# Preprocess dictionary
def predictions(train_dictionary):
   read_file = open('LangId.test', 'r')
   #read_test = read_file.read()
   sentence_tokens = read_file.readlines()
   #print(test_tokens)
   v = 0
   for language, training_data in train_dictionary.items():
       v += len(training_data['unigrams'])
   output = ''
   for index in range(len(sentence_tokens)):
       sentence = sentence_tokens[index]
       #unigrams = unigram_former(sentence)
       bigrams = bigrams_former(sentence)
       max_probability = -1
       max_probability_language = ""
       for language, training_data in train_dictionary.items():
           train_bi_dict = training_data['bigrams']
           train_uni_dict = training_data['unigrams']
           probability = calucluate_probablity(bigrams, train_uni_dict, train_bi_dict, v)
           if probability >= max_probability:
               max_probability = probability
               max_probability_language = language
       output += str(index + 1) + " " + max_probability_language + "\n"
       # print(index, max_probability_language)
   return output


def calucluate_probablity(test_bigrams, train_uni_dict, train_bi_dict, v):
    prob = 1
    for bigram in test_bigrams:
        b= train_bi_dict[bigram] if bigram in train_bi_dict else 0
        uni = bigram[0]
        u = train_uni_dict[uni] if uni in train_uni_dict else 0
        prob = prob* ((b+1)/(u+v))
    return prob

# pickled_files = ['LangId.train.Italian_unigram_training.txt', 'LangId.train.Italian_bigram_training.txt',\
#                  'LangId.train.English_unigram_training.txt', 'LangId.train.English_bigram_training.txt', \
#                  'LangId.train.French_unigram_training.txt' , 'LangId.train.French_bigram_training.txt']


def evaluate():
    languages = ['Italian', 'English', 'French']
    lang_dictionary = {}
    for language in languages:
        lang_dictionary[language]={}
        for ngram in ['unigram_training.txt', 'bigram_training.txt']:
            read_file = open('LangId.train.' + language + "_" + ngram, "rb")
            if read_file.name.endswith('unigram_training.txt'):
                unigram_dict = pickle.load(read_file)
                ngram_dict =lang_dictionary[language]
                ngram_dict['unigrams'] =unigram_dict
            else:
                bigram_dict = pickle.load(read_file)
                ngram_dict = lang_dictionary[language]
                ngram_dict['bigrams'] = bigram_dict
            lang_dictionary[language] = ngram_dict
    output = predictions(lang_dictionary)
    compute_accuracy(output)


def compute_accuracy(output):
    solution_file = open('LangId.sol', 'r')
    solution_list = solution_file.readlines()
    solution_list = [sol.strip('\n') for sol in solution_list]
    output_list = output.split('\n')
    correct, incorrect =corectness_check(solution_list, output_list)
    accuracy = len(correct)*100/(len(correct) + len(incorrect))
    print("Accuracy =", accuracy)
    # print(solution_list[:10])
    # print(output_list[:10])


evaluate()
