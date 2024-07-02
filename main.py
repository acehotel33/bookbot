frankenstein_path = 'books/frankenstein.txt'


def main():
    frankenstein = open_book(frankenstein_path)
    count = count_words(frankenstein)
    print(count)

def open_book(book_path):
    with open(book_path) as f:
        contents = f.read()
        return contents
    
def count_words(book):
    split_book = book.split()
    count_words = len(split_book)
    return count_words

main()