def main():
    frankenstein = open_frankenstein()
    count = count_words(frankenstein)
    print(count)

def open_frankenstein():
    with open('books/frankenstein.txt') as f:
        contents = f.read()
        return contents
    
def count_words(book):
    split_book = book.split()
    count_words = len(split_book)
    return count_words

main()