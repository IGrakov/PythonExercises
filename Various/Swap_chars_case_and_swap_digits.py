# Write a function string_challenge(string) take the string parameter and swap the case of each character.
# Then, if a letter is between two numbers (without separation), switch the places of the two numbers.
# Examples
# Input: "6Hello4 -8World, 7 yes3"
# Output: "4hELLO6 -8wORLD, 7 YES3"
# Input: "Hello -5LOL6"
# Output: "hELLO -6lol5"
# Input: "2S 6 du5d4e"
# Output: "2s 6 DU4D5E"


def string_challenge(str_param: str) -> str:
    if type(str_param) != str:
        raise TypeError("Parameter must be of str type")

    words_list = str_param.split(" ")

    modified_words_list = []

    for word in words_list:
        word_as_list = list(word)
        first_idx = 0
        last_idx = len(word_as_list) - 1
        first_num = None
        last_num = None

        while first_idx < last_idx:
            if word_as_list[first_idx].isdigit():
                first_num = word_as_list[first_idx]
            else:
                first_idx += 1
            if word_as_list[last_idx].isdigit():
                last_num = word_as_list[last_idx]
            else:
                last_idx -= 1
            if first_num and last_num:
                word_as_list[first_idx] = last_num
                word_as_list[last_idx] = first_num
                last_num = None
                first_num = None
                first_idx += 1
                last_idx -= 1

        modified_words_list.append("".join(word_as_list))

    str_as_list = []

    for letter in " ".join(modified_words_list):
        if letter == letter.upper():
            str_as_list.append(letter.lower())
        else:
            str_as_list.append(letter.upper())

    return "".join(str_as_list)
