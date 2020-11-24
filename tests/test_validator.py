import unittest

from tests.testlibs import Case, errorTest
from libs.validator import Validator


class TestValidator(unittest.TestCase):

    def testType(self):
        cases = [
            Case(True, {'day': 30}, dict),
            Case(True, '1', str),
            Case(False, {'day': 30}, list),
            Case(False, '1', int)
        ]

        errorTest(self, Validator.type, cases, TypeError)

    def testKeys(self):
        cases = [
            Case(True, {'day': 30, 'month': 10}, ['day', 'month']),
            Case(True, {'day': 30, 'month': 10, 'years': 20}, ['day', 'month']),
            Case(True, {'day': 30}, []),
            Case(True, {}, []),
            Case(False, {'day': 30}, ['day', 'month']),
            Case(False, {}, ['day', 'month'])
        ]

        errorTest(self, Validator.keys, cases, ValueError)

    def testCompare(self):
        cases = [
            Case(True, 5, '>', 2),
            Case(True, 5, '>=', 2),
            Case(True, 5, '>=', 5),
            Case(True, 5, '==', 5),
            Case(True, 5, '!=', 10),
            Case(True, 5, '<', 10),
            Case(True, 5, '<=', 5),
            Case(True, 5, '<=', 10),
            Case(False, 2, '>', 5),
            Case(False, 2, '>=', 5),
            Case(False, 5, '==', 10),
            Case(False, 5, '!=', 5),
            Case(False, 10, '<', 5),
            Case(False, 10, '<=', 5)
        ]

        errorTest(self, Validator.compare, cases, ValueError)

    def testListOf(self):
        cases = [
            Case(True, [1, 2, 3], int),
            Case(True, ['1', '2', '3'], str),
            Case(False, [1, '2', 3], int),
            Case(False, ['1', 2, '3'], str)
        ]

        errorTest(self, Validator.listOf, cases, ValueError)

    def testURL(self):
        cases = [
            Case(True, 'http://www.example.com'),
            Case(True, 'https://www.google.com'),
            Case(False, 'http//www.example.com'),
            Case(False, 'www.example.com')
        ]

        errorTest(self, Validator.URL, cases, ValueError)
