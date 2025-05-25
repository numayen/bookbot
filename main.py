from stats import get_num_words
from stats import get_num_chars
from stats import sort_char_count
import sys

# open book file and return as a string
def get_book_text(filepath):
    with open(filepath) as book:
        content_as_string = book.read()
    return content_as_string

# print a report of the book analysis
def print_report(filepath, word_count, character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in character_count:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


def main():
    # check input
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    word_count = get_num_words(book)
    character_count = sort_char_count(get_num_chars(book))
    print_report(filepath, word_count, character_count)




main()