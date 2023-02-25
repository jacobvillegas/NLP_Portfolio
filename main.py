from text_processing import *


if __name__ == '__main__':
    files = []
    counter = 0
    while counter <= 15:
        file_name = 'file-number' + str(counter) + '.txt'
        files.append(file_name)
        counter += 1
    print(files)
    corpus_dictionary = {}
    for index in range(len(files)):
        with open(files[index]) as corpus:
            text = corpus.read()
            corpus_dictionary[file_name] = text.lower()

    td_idf_score = obtain_tfidf(corpus_dictionary.values())


