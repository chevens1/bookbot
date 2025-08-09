# main.py
from stats import count_words, letter_counts, sort_counts_desc
import sys

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with status code 1 to indicate incorrect usage

    path = sys.argv[1]  # Use the CLI argument instead of a hardcoded path
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
