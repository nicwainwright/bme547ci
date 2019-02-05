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
@pytest.mark.parametrize("string", [("tachycardia"), ("tachycardiaolas"),
                                    ("tachycar<>(*&^$d   ia"),
                                    ("      tachycardia    "),
                                    ("tachycardia    "),
                                    ("   tachycardia")])
def testTrueDirect(string):
    myString, result = tachycardia.is_tachycardic(string)
    assert result is True


# EXTRA CREDIT
# test strings that are similar to tachycardia, and thus should pass
@pytest.mark.parametrize("string", [("tchycrd"), ("tachyardaiolas"),
                                    ("taychar<>(*&^$d   ia"),
                                    ("      tachyracdia    "),
                                    ("tachycarida    "),
                                    ("   aycaria")])
def testTrueSimilar_extraCredit(string):
    myString, result = tachycardia.is_tachycardic(string)
    assert result is True


# def testInput():
#    with mock.patch.object(__builtins__, 'input', lambda: 'nicolas'):
#        assert isinstance(tachycardia.getString(), str)
