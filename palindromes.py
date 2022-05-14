'''

 Author: Penny Enterline
 Class: CSC 120 Spring 2022
 Description: reads in two lines of input. the first is a file,
              the second is an integer or the word dump. dump
              prints out all the words in a file on separate
              lines. otherwise, the program prints out
              palindromes of 1-3 words and also up to length
              n, which depends on user input.

'''


def dict_to_set(dict_file):
    '''
    takes a file and turns it into a set
    returns a set of words from the file
    '''
    new_set = set()
    file_lines = dict_file.readlines()
    for line in file_lines:
        # cleans up the lines
        new_line = line.split()
        for word in new_line:
            # makes it lowercase
            new_set.add(word.lower())
    return new_set

def set_to_list(new_set):
    '''
    turns a previously created set into a
    sorted list
    new_set is a set
    '''
    sorted_list = sorted(new_set)
    temp_string = ''
    temp_set = set()
    for word in sorted_list:
        for letter in word:
            # checks if its a letter
            if letter.isalpha():
                temp_string += letter
        # makes it all lowercase
        lower_string = temp_string.lower()
        if len(lower_string) >= 2:
            temp_set.add(lower_string)
        temp_string = ''
    final_list = sorted(temp_set)
    return final_list

def palindrome_word_lengths(words):
    """
    find palindromes of length 1-3
    returns them in a dictionary
    words is a list from the user file
    """
    palindromes = {1: set(), 2: set()}
    # loops through each word in the set
    for word in words:
        for i in words:
            # checks the length
            if word == word[::-1]:
                palindromes[1].add(word)
            if (word + i) == (word + i)[::-1]:
                palindromes[2].add(word + i)
            for index in words:
                if (word + i + index) == (word + i + index)[::-1]:
                    palindromes[2].add(word + i + index)
    return palindromes


def data_structure_creation(num, words):
    """
    puts all of the words from the file
    into a dictionary
    puts each word in its proper set, based on its length
    num is user inputed integer
    words is a list from the file
    """
    num = num + 1
    word_dictionary = {}
    # building dictionary of sets
    for i in range(1, num):
        x = set()
        # loops through each word from the file
        for word in words:
            if len(word) == i:
                x.add(word)
        word_dictionary[i] = x
    # loops through the dictionary that was build
    for i in range(1, len(word_dictionary) + 1):
        final = set()
        cur = word_dictionary[i]
        print("PALINDROMES OF LENGTH " + str(i)
              + "    - length of candidate list: " + str(len(cur)))
        # passes through the current word
        for word in cur:
            # checks if palindrome
            if word == word[::-1]:
                final.add(word)
            else:
                for index in words:
                    # makes sure existing word isnt a palindrome
                    if index != index[::-1]:
                        temp = word + index
                        word_dictionary.setdefault(len(temp), set())
                        word_dictionary[len(temp)].add(temp)
        # prints everything out
        for t in sorted(final):
            print("  " + t)
        print()

def dump(sorted_list):
    '''
    dumps all the words in the file list
    prints them out on separate lines
    sorted_list is a list of words
    from the user file
    '''
    print('WORD LIST:')
    for item in sorted_list:
        print(item)

def main():
    '''
    opens user file and reads in the action typed
    closes if file isnt found
    calls the rest of the functions in the program
    '''
    # user input
    dict_file = input()
    action = input()
    # debugging
    try:
        opened_file = open(dict_file, 'r')
    except FileNotFoundError:
        print('ERROR: Could not open the input'
              ' file: BAD_FILENAME')
        return
    # converts file into a list in 2 parts
    # first converts to a set
    word_set = dict_to_set(opened_file)
    # converts that set into a list
    sorted_list = set_to_list(word_set)
    # if the action is a number
    if action.isnumeric():
        num = int(action)
        palindromes_word_lengths = palindrome_word_lengths(sorted_list)
        # prints out palindromes of length 1
        print("1-WORD PALINDROMES:")
        for i in sorted(palindromes_word_lengths[1]):
            print("  " + i)
        print()
        # prints out palindromes of length 2
        print("2-WORD AND 3-WORD PALINDROMES:")
        for i in sorted(palindromes_word_lengths[2]):
            print("  " + i)
        print()
        # prints out palindromes of length n
        data_structure_creation(num, sorted_list)
    # else if its dump
    elif action == 'dump':
        dump(sorted_list)

main()
