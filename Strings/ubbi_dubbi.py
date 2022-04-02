def ubbu_dubbi(word):
    """Returns a string, the words translation into `Ubbi Dubbi`
        Returns:
            if the function is called with `octopus`,
            the function will return the string `uboctubopubus`
    """

    output = []
    for letter in word:
        if letter in "aeiou":
            output.append(f"u{letter}")
        else:
            output.append(letter)
    return "".join(output)
