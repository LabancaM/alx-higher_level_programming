#!/usr/bin/python3

"""indentation"""


def text_indentation(text):
    """ test indentation

    Args
        text: string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text[1] == " " or text[-1] == " ":
        text = text.strip()
    length = len(text)
    start = 0
    for i in range(length):
        if text[i] == '\n':
            print()
        if text[i] in ".?:":
            print(text[start: i + 1].strip())
            print()
            start = i + 1
    if start != length:
        print(text[start:].strip())
