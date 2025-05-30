def word_count(text):
    word_list = text
    count = word_list.split()
    return len(count)

def char_count(text):
    char_dict = {}

    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dict(char_dict):
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)

