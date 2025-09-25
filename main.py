def get_book_text (filename):
    with open(filename) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    return len(text.split())

def main ():
    fkpath = "books/frankenstein.txt"
    fktext = get_book_text(fkpath)
    num_words = count_words(fktext)
    print(f"Found {num_words} total words")

main()