from stats import count_word, return_counts


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main():
    a_book = get_book_text("books/frankenstein.txt")
    inventory = return_counts(a_book)
    print(f"{count_word(a_book)} words found in the document")

    print(f"Character counts: {inventory}")
main()

