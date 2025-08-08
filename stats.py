def count_word(a_book):
    words = a_book.split()
    length = len(words)
    return length

def return_counts(a_book):
    results = {}
    for character in a_book:
        char_lower = character.lower()
        if char_lower in results:
            results[char_lower] += 1
        else:
            results[char_lower] = 1
    return results