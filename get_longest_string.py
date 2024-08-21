def get_longest_string(sentence=''):
    """
    Return longest word into input-sentence
    """
    words = sentence.split(" ")
    if len(words) == 1:
        return words
    else:
        max_length = 0
        result = ''
        for word in words:
            if len(word) > max_length:
                max_length = len(word)
                result = word
        return result


str_test = "NashTech Python Training Program XXXXXXXXXXXXXXXXXX"
print(get_longest_string(str_test))


def get_longest_list_string(sentence=''):
    """
    Return longest list of word into input-sentence
    """
    words = sentence.split(" ")
    if len(words) == 1:
        return words
    else:
        max_length = 0
        result = []
        for word in words:
            if len(word) > max_length:
                result.clear()
                max_length = len(word)
                result.append(word)
            elif len(word) == max_length:
                result.append(word)
        return result


str_test = "NashTech Python Training Program XXXXXXXXXXXXXXXXXX"
print(get_longest_list_string(str_test))
