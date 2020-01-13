#!/usr/bin/python3
"""
This is the "5-text_indentation.py" module.

The 0-add_integer module functions: text_indentation(text).
"""


def text_indentation(text):
    """
    text_indentation: prints a text with 2 new lines after \
        each of these characters: ., ? and :
    Args:
        text (str): the size length of the square
    Returns:
        None
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    phrase = ''
    for c in text:
        if c in ['.', '?', ':']:
            phrase += c
            print(phrase.strip())
            print()
            phrase = ''
        else:
            phrase += c
    if phrase:
        print(phrase.strip())
