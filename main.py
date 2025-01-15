def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = word_counter(text)
    char_dictionary = char_counter(text)
    char_list = make_list(char_dictionary)
    char_list.sort(reverse=True, key=sort_dict)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{count_words} words found in the document\n')


    for char in char_list:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print ("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def char_counter(text):
    char_dict = {}
    lower_text = text.lower()

    for i in lower_text:
        if i.isalpha():
            if i not in char_dict:
              char_dict[i] = 1
            else:
                char_dict[i] += 1
    return char_dict

def sort_dict(char_dictionary):
    return char_dictionary["num"]

def make_list(char_dictionary):
    char_list = []
    for char,num in char_dictionary.items():
        this_dict = {"char": char, "num": num}
        char_list.append(this_dict)
    return char_list

main()