# get words in a string (divided by a space)
def get_num_words(string):
    return len(string.split())


# get number of each character used in a string. not case sensitive. returns a dictionary
def get_num_chars(string):
    string = string.lower()
    total = {}
    for character in string:
        if character not in total:
            total[character] = 1
        else:
            total[character] += 1
    return total

# local function for use in sort_char_dict. key handle for sort()
def sort_on(dict):
    return dict["num"]

# create a sorted list of dictionaries from a character count dictionary input
def sort_char_count(char_dictionary):
    sorted_list = []
    for char in char_dictionary:
        sorted_list.append({"char": char, "num": char_dictionary[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list