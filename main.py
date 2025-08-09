# main.py
from stats import count_words, letter_counts, sort_counts_desc

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    # Compute stats
    total_words = count_words(text)
    counts_sorted = sort_counts_desc(letter_counts(text))

    # Report – matches the structure boot.dev expects
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for ch, n in counts_sorted:
        print(f"{ch}: {n}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
