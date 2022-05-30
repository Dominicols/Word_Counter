from pathlib import Path
import string
import sys

TOP_TEN_WORDS = 10

path_check= False

# Check if user added a path to the text file
if len(sys.argv) == 1:
    print('USAGE: python word_counter.py <txt file>')
else:
    path = Path(sys.argv[1])
    path_check = True



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


# Main Function that opens given file and reads it. Reformats the words into a list and 
# calls the custom sort function with a dictionary of counted words. Prints results. 
def word_count(path):
    word_count = dict()
    total_counter = 0

    with open(path, 'rt') as file:
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
                    if word != '':
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

# Checks if file is given and if it exists and calls the main function
if path_check != False:
    if path.exists():
        print(word_count(path))
    else:
        print('File does not exist')
else: 
    print("File was not given")