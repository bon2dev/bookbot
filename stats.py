def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def count_chars(words):
    lower_word  = words.lower()
    char_count  = {}
    for w in lower_word:
        if w in char_count:
            char_count[w] += 1
        else:
            char_count[w] = 1
    return char_count

def chars_to_sorted_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    def sort_on(char_dict):
        return char_dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list
