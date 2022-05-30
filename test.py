import unittest
from pathlib import Path
import string

TOP_TEN_WORDS = 10

# Custom reverse sort function for dictionaries | Returns reversed dictionary
def dict_reverse_sort(d):
    dict = d
    length = len(dict)
    list_values = list()
    list_keys = list()
    sorted_dict = {}

    # Checking if the length of dict is null or 1, in which case return it
    if length <= 1:
        return dict

    # Getting list of values from the dictionary
    for x,y in dict.items():
        list_values.append(y)
    
    # Reversing order of the list 
    for i in range(length):
        for j in range(0, length-i-1):
            if list_values[j] < list_values[j+1]:
                list_values[j], list_values[j+1] = list_values[j+1], list_values[j]

    count = 0
    # Iterating through the values of list_values, appending the key(word) to list_keys and removing the key/value pair from our dictionary.
    for i in list_values:
        key = list(dict.keys())[list(dict.values()).index(list_values[count])]
        list_keys.append(key)
        dict.pop(key)
        count += 1
    
    # Resetting counter
    count=0
    # Iterating through our list of keys and using both our lists of values and keys to add the values/keys to our final sorted_dict
    for i in list_keys:
        sorted_dict[list_keys[count]] = list_values[count]
        count += 1

    return sorted_dict

def word_count(path):
    word_count = dict()
    total_counter = 0

    with open(path, 'r') as file:
        for line in file:
            # Reformat words of text file.
            line = line.strip()
            line = line.lower()
            line = line.translate(line.maketrans("", "", string.punctuation))
            words = line.split(" ")
            #

            # Counts each word. If it is a new word(key) it adds it and gives it a count of 1. If it is an existing word(key) it adds 1 to the count(value)
            # Also counts the total number of words
            for word in words:
                total_counter += 1
                if word in word_count:
                    word_count[word] = word_count[word] + 1
                else:
                    word_count[word] = 1

            
        final_dict = dict_reverse_sort(word_count)
        top_ten_string = ""
        c = 0
        for x,y in final_dict.items():
            if c < TOP_TEN_WORDS:
                top_ten_string += str(x) + ' ' + str(y) + '\n'
                c +=1

        return 'Top 10 words: ' + '\n' + str(top_ten_string) + 'Total Words: '+ str(total_counter)

class TestCases(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(dict_reverse_sort({ 5: 25, 2: 4, 1: 1,  4: 16, 3: 9}), {5: 25, 4: 16, 3: 9, 2: 4, 1: 1 })
        self.assertEqual(dict_reverse_sort({'': 1, 'it': 1, 'was': 2, 'an': 1, 'astounding': 1, 'discovery': 1, 'the': 4, 'mountain': 1, 'more': 1, 'than': 1, '150': 1, 'miles': 1, 'from': 1, 'nearest': 1, 'settlement': 1, 'in': 2, 'a': 1, 'spot': 1, 'that': 1, 'had': 2, 'never': 1, 'been': 1, 'explored': 1, 'soviet': 1, 'authorities': 1, 'no': 1, 'records': 1, 'of': 1, 'anyone': 1, 'living': 1, 'district': 1})
        , {'the': 4, 'was': 2, 'in': 2, 'had': 2, '': 1, 'it': 1, 'an': 1, 'astounding': 1, 'discovery': 1, 'mountain': 1, 'more': 1, 'than': 1, '150': 1, 'miles': 1, 'from': 1, 'nearest': 1, 'settlement': 1, 'a': 1, 'spot': 1, 'that': 1, 'never': 1, 'been': 1, 'explored': 1, 'soviet': 1, 'authorities': 1, 'no': 1, 'records': 1, 'of': 1, 'anyone': 1, 'living': 1, 'district': 1})
        self.assertEqual(dict_reverse_sort({ 5: 25, 2: 4, 1: 1, 4: 16, 3: 9, 'and': 2, 'an': 3})
        ,{5: 25, 4: 16, 3: 9, 2: 4, 'an': 3, 'and': 2, 1: 1 })

    def test_wordcount(self):
        self.assertMultiLineEqual(word_count('test.txt'),'Top 10 words: \nthis 1\nis 1\na 1\ntest 1\nTotal Words: 4')

if __name__ == '__main__':
    unittest.main()