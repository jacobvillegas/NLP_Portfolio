import sys



def open_read(file):
    with open(file, 'r') as document:
        text = document.read()
    return text


def file_sys_arg():
    """Allows for user to input a text file name:
        - reads txt if present
        - displays warning and exits no sys.argv
    """

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        # print('Retrieving: ', filename)
        # with open(filename, 'r') as f:
        #     print(f.read())
        document = open_read(filename)

    else:
        print('File Does not exit--Exiting Program')
        quit()
    return document


# ___if name__= main.
if __name__ == '__main__':

    # allow to import txt file from command line
    corpus = file_sys_arg()
    print(corpus)

