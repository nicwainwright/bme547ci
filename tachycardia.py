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
    # calculate the similarity ratio of the two strings
    ratio = SequenceMatcher(None, string, expected).ratio()
    # if the string contains tachycardia exactly or a relatively similar
    # string based on ratio, return True
    if expected in string or ratio > 0.75:
        result = True
    else:
        result = False

    return string, result, ratio


def main():
    originalString = getString()
    string, result, ratio = is_tachycardic(originalString)
    if result is True:
        print("The string:", string, ", DOES resemble 'tachcycardia' with "
              "similarity ratio", ratio)
    else:
        print("The string:", string, ", DOES NOT resemble 'tachcycardia' with"
              " similarity ratio", ratio)


if __name__ == "__main__":
    main()
