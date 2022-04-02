def ubbu_dubbi(word):
    """Returns a string, the words translation into `Ubbi Dubbi`
        Returns:
            if the function is called with `octopus`,
            the function will return the string `uboctubopubus`
    """

    output = []
    for letter in word:
        if letter.isupper():
            if letter in "aeiou".upper():
                output.append(f"Ub{letter.lower()}")

        elif letter in "aeiou":
            output.append(f"ub{letter}")
        else:
            output.append(letter)
    return "".join(output)


print(ubbu_dubbi("octopus"))
