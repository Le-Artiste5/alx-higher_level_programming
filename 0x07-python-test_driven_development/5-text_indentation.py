#!/usr/bin/python3
"""

This module prints a text with 2 new lines after each of these characters: ., ? and :

"""

def text_indentation(text):
    """ This function prints a text with two linesafter some special characters

    Args:
        text: The texts to be used

    Return:
        Doesn't return anything

    Raise: 
        TypeError: This comes up when the entered text is not a string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    o = text[:]

    for c in ".?:":
        list_text = o.split(c)
        o = ""
        for k in list_text:
            k = k.strip(" ")
            o = k + c if o is "" else o + "\n\n" + k + c
    print(o[:-3], end="")
