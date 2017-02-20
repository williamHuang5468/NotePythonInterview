
# string = "aba"
def get_none_repeat_letter_index(string):
    letterDict = {}
    for index in range(len(string)):
        if string[index] in letterDict.keys():
            letterDict.update({string[index]:letterDict[string[index]]+1})
        else:
            letterDict.update({string[index]:1})

    for index in range(len(string)):
        if letterDict[string[index]] is 1:
            return index
    return None

def get_none_repeat_letter_index_using_split(string):
    '''
    Another method using split string.
    '''
    for index in range(len(string)):
        if string[index] not in string[index+1:]:
            return index
    return None


def list_comprehesion(string):
    return ([index for index in range(len(string)) if string[index] not in string[index+1:]][0])


assert get_none_repeat_letter_index("aba") == 1
assert get_none_repeat_letter_index("abcgabc") == 3

assert get_none_repeat_letter_index_using_split("aba") == 1
assert get_none_repeat_letter_index_using_split("abcgabc") == 3

assert list_comprehesion("aba") == 1
assert list_comprehesion("abcgabc") == 3
