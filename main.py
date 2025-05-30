import sys
from stats import word_count
from stats import char_count
from stats import sort_dict

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read();
    except FileNotFoundError:
        return "File Not Found!"
    return file_contents



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    words = get_book_text(sys.argv[1])
    num_words = word_count(words)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    char_counts = char_count(words)
    sorted_counts = sort_dict(char_counts)

    for char, count in sorted_counts:
        print(f"{char}: {count}")

    print("============= END ===============")

 



main()