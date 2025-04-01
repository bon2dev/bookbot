def get_book_text(input_path):
    with open(input_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()

