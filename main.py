from stats import count_words
from stats import count_characters
from stats import sorted_characters

import sys

def get_book_text (filename):
    with open(filename) as f:
        file_contents = f.read()
        return file_contents
    
def print_report(filepath, word_count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")    
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in char_counts:
        print(F"{entry["char"]}: {entry["num"]}")
    
def main ():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    fkpath = sys.argv[1]
    # fkpath = "books/frankenstein.txt"
    fktext = get_book_text(fkpath)
    num_words = count_words(fktext)
    sorted_count = sorted_characters(count_characters(fktext))
    print_report(fkpath, num_words, sorted_count)

main()