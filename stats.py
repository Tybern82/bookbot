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

def charsorter(items):
    return items["num"]

def sorted_characters(char_counts):
    unsorted_counts = []
    for ch in char_counts:
        unsorted_counts.append({"char": ch, "num": char_counts[ch]})
    unsorted_counts.sort(reverse=True, key=charsorter)
    return unsorted_counts
