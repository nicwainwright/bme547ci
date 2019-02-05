# Homework 5: Unit Testing and Continuous Integration
This repository was created on Feb 5th, 2019 for Duke BME547's fourth homework assignment.

## Usage
Please call this program in a terminal. 
- In Git BASH window, type ```python tachycardia.py```.
It will prompt the user to input their **string**

## Output
```tachycardia.py``` will calculate whether or not the inputted string is similar to the word *tachycardia* and output:
+ whether or not the string resembles *tachycardia*
+ what the similarity ratio of the inputted and expected strings are

### Function
```tachycardia.py``` first removes all punctuation and whitespace from the string. It then compares it directly to *tachycardia*. It uses the ```SequenceMatcher``` function to also allow almost-similar string to pass as **True**