# -*- coding: utf-8 -*-
"""
Created on Feb 5

@author: nicwainwright

BME547 Homework 4
Travis CI and Continuous Integration

test_file.py for unit testing
"""


import tachycardia
import math
import pytest
import mock


def testInput():
    with mock.patch.object(__builtins__, 'input', lambda: 'nicolas'):
        assert isinstance(tachycardia.getString(), str)