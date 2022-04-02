
def word_per_line(filename):
    """Given a text file, return a sentence from the nth
word for line n, for each of the first 10 lines.
"""
    output = []

    for n, one_line in enumerate(open(filename)):
        words = one_line.split()

        if not words:
            continue

        if n >= 10:
            break

        if n >= len(words):
            output.append(words[-1])
        else:
            output.append(words[n])

    return ' '.join(output)
