# -*- coding: utf-8 -*-
"""
Created on Feb 5

@author: nicwainwright

BME547 Homework 4
Travis CI and Continuous Integration

test_file.py for unit testing
"""


import tachycardia
import pytest
import mock


# test inputs that should yield similarities because they directly contain
# the word 'tachycardia' after removing punctuation
@pytest.mark.parametrize("string", [("tachycardia"), ("tachycar<>(*&^$d   ia"),
                                    ("      tachycardia    "),
                                    ("tachycardia    "), ("tachycardiaolas"),
                                    ("   tachycardia")])
def testTrue_Direct(string):
    myString, result = tachycardia.is_tachycardic(string)
    assert result is True


# test inputs that should yield similarities because they directly contain
# the word 'tachycardia' after removing punctuation
@pytest.mark.parametrize("string", [("nicolas"), ("1234"), (""),
                                    ("Ilove this place"),
                                    ("edm is blender music to some"),
                                    ("   "), ("")])
def testFalse_Direct(string):
    myString, result = tachycardia.is_tachycardic(string)
    assert result is False


# EXTRA CREDIT
# test strings that are similar to tachycardia, and thus should pass
@pytest.mark.parametrize("string", [("tchycrd"), ("taychar<>(*&^$d   ia"),
                                    ("      tachyracdia    "),
                                    ("tachycarida    "), ("tchycrd"),
                                    ("   aycaria")])
def testTrue_Similar_extraCredit(string):
    myString, result = tachycardia.is_tachycardic(string)
    assert result is True


# EXTRA CREDIT
# test strings that are similar to tachycardia, but different enough to fail
@pytest.mark.parametrize("string", [("bradycardia"), ("ardiatachy"),
                                    ("tchcrd")])
def testFalse_Similar_extraCredit(string):
    myString, result = tachycardia.is_tachycardic(string)
    assert result is False


# def testInput():
#    with mock.patch.object(__builtins__, 'input', lambda: 'nicolas'):
#        assert isinstance(tachycardia.getString(), str)
