

def make_files(string, files):
    new_file = open(files, 'x')
    for text in string:
        new_file.write(text)
    new_file.close()
    return new_file


def batch_file_names(number):
    list_of_files =[]
    while number > 0:
        file = 'file-number' + str(number) + '.txt'
        list_of_files.append(file)
        number -= 1
    return list_of_files


def create_txt_file(string, counter):
    files = 'file-number' + str(counter) + '.txt'
    new_file = open(files, 'x')
    for text in string:
        new_file.write(text)
    new_file.close()
    return new_file
