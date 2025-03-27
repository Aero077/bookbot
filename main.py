from sys import argv, exit
from stats import get_num_words, count_characters, sort_character_count

def get_book_text(path_to_file):
    # Read the contents of a book from a file and return the text as a string.
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_help():
    # Print the help message.
    print("Usage: python3 main.py <path_to_book>")
    return

def main():
    if len(argv) > 1:
        if argv[1] == "-h" or argv[1] == "--help":
            print_help()
            exit(1)
        else:
            bookpath = argv[1]
    else: # CH3:L2
        print_help()
        exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {bookpath}...")
    print("----------- Word Count ----------")
    get_num_words(bookpath)   
    print("--------- Character Count -------")
    for c in sort_character_count(count_characters(bookpath)):
        print(f"{c[0]}: {c[1]}")
    print("============= END ===============")
    return

main()