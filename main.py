from stats import word_count, count_chars, chars_to_sorted_list

def get_book_text(input_path):
    with open(input_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count_result = word_count(file_contents)
    char_counts = count_chars(file_contents)
    sorted_chars = chars_to_sorted_list(char_counts)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()

