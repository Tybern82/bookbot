def get_book_text (filename):
    with open(filename) as f:
        file_contents = f.read()
        return file_contents

def main ():
    fkpath = "books/frankenstein.txt"
    fktext = get_book_text(fkpath)
    print(fktext)

main()