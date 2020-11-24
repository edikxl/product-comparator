from typing import Callable, List
from dataclasses import dataclass
from unittest import TestCase

from libs.validator import Validator


@dataclass(init=False)
class Case:
    
    expectedResult: bool
    args: tuple

    def __init__(self, expectedResult: bool, *args: list) -> None:
        self.expectedResult = expectedResult
        self.args = tuple(args)

    # <!-- SETTERS | GETTERS
    @property
    def expectedResult(self) -> bool:
        return self._expectedResult

    @expectedResult.setter
    def expectedResult(self, expectedResult: bool):
        Validator.type(expectedResult, bool)
        self._expectedResult = expectedResult

    @property
    def args(self) -> tuple:
        return self._args

    @args.setter
    def args(self, args: tuple):
        Validator.type(args, tuple)
        self._args = args
    # -->


def errorTest(self: TestCase, function: Callable, cases: List[Case], error: Exception) -> None:
    for case in cases:
        try:
            function(*case.args)
        except error:
            if case.expectedResult:
                self.fail(error.__name__)
