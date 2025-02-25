import sys
from stats import get_text_count, unique_char_count, sort_on

def get_book_text(f):
    with open(f) as file:
        return file.read()

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(file_path)
    count = get_text_count(text)
    char_count = unique_char_count(text)
    char_sorted = sort_on(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char, count in char_sorted:
        if char.isalpha():
            print(f"{char}: {count}")
if __name__ == "__main__":
    main()

