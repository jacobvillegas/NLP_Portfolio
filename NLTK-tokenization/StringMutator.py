from collections import UserString
# GOOD TO USE

""" Simple Class to Mutate a String as Strings are Immutable
Extra Functions added to Change
TODO : Eventually turn into a decorator
"""


class StringMutator(UserString):
    def __setitem__(self, index, value):
        letter_list = list(self.data)
        letter_list[index] = value
        self.data = "".join(letter_list)

    def does_letter_exist(self, letter):
        for char in self:
            if char == letter:
                return True
            else:
                return False


"""ASSOCIATED FUNCTIONS OUTSIDE OF CLASS SCOPE"""


# ENCRYPTING FUNCTION TO  ADD A BLANK(" - ") CHARACTER TO A STRING
def encrypt(word_to_encrypt):
    word_index = len(word_to_encrypt) - 1
    while word_index >= 0:
        word_to_encrypt[word_index] = '_'
        word_index -= 1
    return word_to_encrypt


# generator function to remove blanks with a letter in a word
def decrypt(word, letter, blocked_word):
    for index, elem in enumerate(word):
        if elem == letter:
            blocked_word[index] = letter
    return blocked_word


# generator function to obtain all the indices of the letter
def find_all_indexes(word, letter):
    for index, elem in enumerate(word):
        if elem == letter:
            yield index


# Added function to place required spaces in hidden word
def add_spaces(StringMut):
    bag_of_letters = list(StringMut.data)
    spaced_string = " ".join(bag_of_letters)
    print(spaced_string)


# My personal Sanity check
# my_string = "alphabet"
# my_mutated = StringMutator(my_string)
#
# hidden_word = encrypt(my_mutated)
# print(hidden_word)
# print(hidden_word)
#
# add_spaces(hidden_word)
# print(hidden_word)