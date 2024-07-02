frankenstein_path = 'books/frankenstein.txt'

def main():
    frankenstein = open_book(frankenstein_path)
    count = count_words(frankenstein)
    char_dict = count_chars(frankenstein)
    print(char_dict)

def open_book(book_path):
    with open(book_path) as f:
        contents = f.read()
        return contents
    
def count_words(book):
    split_book = book.split()
    count_words = len(split_book)
    return count_words

def count_chars(string):
    lower_string = string.lower()
    char_count = {}
    for ch in lower_string:
        if ch not in char_count:
            char_count[ch] = 1
        else:
            char_count[ch] += 1
    return char_count

def test():
    test_str = "Hey my name is Vakho!"
    print(count_chars(test_str))

# test()
main()