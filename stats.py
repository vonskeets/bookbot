def get_book_text(filepath):
    with open(filepath) as f:
        file = f.read()
        
    
    return file



def dictcount():
    bookText = (get_book_text("./books/frankenstein.txt"))
    char_counts = {}

    words = bookText.lower()
    
    for char in words:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def main():
    bookText = get_book_text("./books/frankenstein.txt")

    bookCharcount = dictcount()
    
    words = bookText.split()

    count = len(words)


    print(f"{count} words found in the document.")
    print(f"{bookCharcount}")

    
main()
