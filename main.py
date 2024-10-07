def get_file_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(character_string):
    character_counts = {}
    for x in character_string:
        char = x.lower()
        if char not in character_counts:
            character_counts[char] = 1
        else:
            character_counts.update({char: character_counts.get(char) + 1})
    return character_counts

def print_report(book_title, word_count, character_counts):
    list_of_dicts = []
    for char in character_counts:
        if char.isalpha():
            list_of_dicts.append({char: character_counts.get(char)})
    print(f"--- Begin report of {book_title} ---")
    print(f"{word_count} words found in the document")
    sorted_list = sorted(list_of_dicts, key=lambda x: list(x.values())[0],reverse=True)
    for char in sorted_list:
        key = list(char.keys())[0]
        value = char[key]
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def main():
    book_title = "./books/frankenstein.txt"
    print("Hello world")
    text = get_file_text(book_title)
    print(text)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    print_report(book_title,word_count,char_count)
main()
