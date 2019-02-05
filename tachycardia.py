# -*- coding: utf-8 -*-
"""
Created on Feb 5

@author: nicwainwright

BME547 Homework 4
Travis CI and Continuous Integration
"""
from difflib import SequenceMatcher


def getString():
    string = input("Please enter your word:\n")

    # check to be sure the input is a string, which should be hard to mess up
    if not isinstance(string, str):
        print("This is not a string, please try again.")
        getString()
    else:
        return string


# strip the string of punctuation and make lowercase
def stripString(string):
    # define punctuation
    punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    strippedString = ""
    for char in string:
        if char not in punctuations:
            strippedString = strippedString + char
    return strippedString.lower()


def is_tachycardic(string):
    string = stripString(string)
    expected = "tachycardia"
    ratio = SequenceMatcher(None, string, expected).ratio()
    print(ratio)
    if expected in string or ratio > 0.75:
        result = True
    else:
        print("Failed with ratio:", ratio)
        result = False

    return string, result


def main():
    originalString = getString()
    string, result = is_tachycardic(originalString)
    if result is True:
        print("The string:", string, ", resembles 'tachcycardia.'")
    else:
        print("The string:", string, ", does not resemble 'tachcycardia.'")


if __name__ == "__main__":
    main()
