# Function to count the number of words in the text
def word_count(file_contents):
    # Split the text into a list of words using whitespace as the separator
    words = file_contents.split()
    # Return the total number of words
    return len(words)

# Function to count the frequency of each character in the text
def count_chars(words):
    # Convert all characters to lowercase for case-insensitive counting
    lower_word = words.lower()
    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Iterate over each character in the lowercase string
    for w in lower_word:
        # If the character is already in the dictionary, increment its count
        if w in char_count:
            char_count[w] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_count[w] = 1

    # Return the dictionary containing character counts
    return char_count

# Function to convert a character count dictionary to a sorted list of dictionaries
def chars_to_sorted_list(char_count):
    # Create an empty list to hold character data as dictionaries
    char_list = []

    # Convert the character count dictionary into a list of dictionaries
    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    # Helper function to specify sorting by count value
    def sort_on(char_dict):
        return char_dict["count"]

    # Sort the list of character dictionaries in descending order by count
    char_list.sort(reverse=True, key=sort_on)

    # Return the sorted list
    return char_list

