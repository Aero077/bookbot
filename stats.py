from string import ascii_lowercase

def get_num_words(path_to_file):
    # Count the number of words in a document.
    words = []
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = 0
        for word in words:
            num_words += 1
    print(f"Found {num_words} total words")
    return

def count_characters(path_to_file):
    # Count the number of times each character appears in a document.
    character_list = []
    character_count = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        character_list = file_contents.lower()
        for character in character_list:
            if (character not in character_count) and (character in ascii_lowercase):
                # Example report format included non ascii characters, but the check was only for ascii characters and the spirit of the task was to count only ascii characters.
                character_count[character] = 0
            if character in character_count:
                character_count[character] += 1
    return character_count

def sort_on(dict):
    # Sort the character count dictionary by the number of times each character appears.
    # Although the description specified two keys, the function only uses one.
    # As there wasn't any clear reason to use a second key, I decided to use only one.
    return dict[1]

def sort_character_count(character_count):
    # Sort the character count dictionary by the number of times each character appears.
    sorted_characters = sorted(character_count.items(), key=sort_on, reverse=True)
    return sorted_characters