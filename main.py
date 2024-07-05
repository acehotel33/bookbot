frankenstein = 'books/frankenstein.txt'

def main():
    open_frankenstein = open_book(frankenstein)
    chars_frankenstein = count_chars(open_frankenstein)
    words_frankenstein = count_words(open_frankenstein)
    report(open_frankenstein, words_frankenstein, chars_frankenstein)

def test():
    open_frankenstein = open_book(frankenstein)
    chars_frankenstein = count_chars(open_frankenstein)
    words_frankenstein = count_words(open_frankenstein)
    sorted_chars = sort_chars(chars_frankenstein)
    

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
        if ch.isalpha():
            if ch not in char_count:
                char_count[ch] = 1
            else:
                char_count[ch] += 1
    return char_count

def sort_chars(chars_dict):
    """
    input = {
            'a': 13, 
            'x': 12, 
            's':2, 
            'v': 5, 
            'o': 14
            }
    output = {
            'o': 14,
            'a': 13, 
            'x': 12, 
            'v': 5, 
            's':2, 
            }    
    """
    
    items = chars_dict.items()
    sorted_items = sorted(items, key=lambda item: item[1], reverse=True)
    sorted_dict = {key: value for key, value in sorted_items}
    return sorted_dict

def report(book, words, chars):
    sorted_chars = sort_chars(chars)
    print(f"--- Begin report of {frankenstein} ---")
    print(f"{words} words found in the document\n\n")

    for ch in sorted_chars:
        print(f"The '{ch}' character was found {sorted_chars[ch]} times")

# test()
main()