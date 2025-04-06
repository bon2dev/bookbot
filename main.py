# Import specific utility functions from the stats module
from stats import word_count, count_chars, chars_to_sorted_list

# Import the sys module to access command-line arguments
import sys

# Function to read the entire contents of a file
def get_book_text(input_path):
    # Open the file at the given path and read its contents
    with open(input_path) as f:
        file_contents = f.read()
    # Return the full text of the file
    return file_contents

# The main function that orchestrates the analysis
def main():
    # Check if the user provided a file path as a command-line argument
    if len(sys.argv) < 2:
        # Print usage instructions if no argument is given
        print("Usage: python3 main.py <path_to_book>")
        # Exit the program with an error code
        sys.exit(1)

    # Get the path to the book file from the command-line arguments
    path_to_book = sys.argv[1]

    # Read the content of the book from the specified file
    file_contents = get_book_text(sys.argv[1])

    # Count the number of words in the text
    word_count_result = word_count(file_contents)
    # Count the frequency of each character in the text
    char_counts = count_chars(file_contents)
    # Sort the character counts into a list of dictionaries
    sorted_chars = chars_to_sorted_list(char_counts)

    # Display the analysis results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    
    # Print the total word count
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    
    # Print the character frequency table
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        # Only display alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

# Call the main function to start the program
main()

