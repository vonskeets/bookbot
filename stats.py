import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file = f.read()
        
    
    return file



def dictcount(filepath):
    bookText = get_book_text(filepath)
    char_counts = {}

    words = bookText.lower()
    
    for char in words:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def dictsort(filepath):
    sortBook = []

    bookCharcount = dictcount(filepath)

    for char, count in bookCharcount.items():
        sortBook.append({"char": char, "num": count})

    sortBook.sort(reverse=True, key=lambda item: item["num"])

    return sortBook
    

def main():

    filepath = sys.argv[1]

    bookText = get_book_text(filepath)

    bookCharsort = dictsort(filepath)
  

    words = bookText.split()

    count = len(words)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in bookCharsort:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    
main()
