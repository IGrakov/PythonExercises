# Write a function that checks whether all characters in a given string are unique

def are_all_characters_unique(src_str):

    if type(src_str) != str:
        raise TypeError("Argument must be of string type")

    return len(src_str) == len(set(src_str))
