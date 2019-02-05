# -*- coding: utf-8 -*-
"""
Created on Feb 5

@author: nicwainwright

BME547 Homework 4
Travis CI and Continuous Integration
"""


def getString():
    string = input("Please enter your word:\n")
    return string

def stripString(string):
    # define punctuation
    punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    strippedString = ""
    for char in string:
        if char not in punctuations:
            strippedString = strippedString + char
    return strippedString.lower()

def is_tachycardic():
    string = stripString(getString())
    return string, True

    
def main():
    string, result = is_tachycardic()    
    if result == True:
        print("The string:", string, ", resembles 'tachcycardia.'")
    else:
        print("The string:", string, ", does not resemble 'tachcycardia.'")


if __name__ == "__main__":
    main()