def pig_latin(word):
    """Takes a string as input, and return the translation of this word in Pig Latin"""

    word = word.lower()
    if word[0] in "aeiou":
        return (f"{word}way")

    return f"{word[1:]}{word[0]}ay"


print(pig_latin("python"))
