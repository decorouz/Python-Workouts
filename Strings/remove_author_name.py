# importing relevant libraries
import pytest


def author_name_remover(sentence: str) -> str:
    """
    remove given author names from given sentence
    :param sentence: a string , given plain english sentence
                    containing author names
    :return: a string, author names removed string
    """
    author_names = ["john", "alex", "jodd", "taylor"]
    new_sentence = []
    for word in sentence.split():
        if word in author_names:
            new_sentence.append("_")
        else:
            new_sentence.append(word)
    return " ".join(new_sentence)


test_data = [("Hello john , How are you alex ? Nice to meet you jodd . goodbye taylor",
              "Hello _ , How are you _ ? Nice to meet you _ . goodbye _")]


@pytest.mark.parametrize("given, expected", test_data)
def test_author_name_remover(given, expected):
    assert author_name_remover(given) == expected
