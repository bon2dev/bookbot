def get_book_text(input_path):
    with open(input_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num = word_count(file_contents)
    print(f"{num} words found in the document")

main()

