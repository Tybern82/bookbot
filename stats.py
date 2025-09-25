def count_words(text):
    return len(text.split())

def count_characters(text):
    lowertext = text.lower()
    char_counts = {}
    for ch in lowertext:
        if ch not in char_counts:
            char_counts[ch] = 1
        else:
            char_counts[ch] += 1
    return char_counts