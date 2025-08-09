# stats.py

def count_words(text):
    """
    Count total words by splitting on whitespace.
    This matches boot.dev's expected total for Frankenstein.
    """
    return len(text.split())

def letter_counts(text):
    """
    Count only alphabetic characters (Unicode-aware).
    Use .casefold() so accented letters normalize (e.g., É == é).
    """
    results = {}
    for ch in text:
        if ch.isalpha():
            key = ch.casefold()
            results[key] = results.get(key, 0) + 1
    return results

def sort_counts_desc(counts):
    """
    Sort by:
      1) count descending (using -count)
      2) letter ascending as a stable tie-break
    """
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
