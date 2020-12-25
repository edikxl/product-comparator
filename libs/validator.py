from typing import Any, List, Union
import re


class ValidationError(Exception):
    def __init__(self, errorMessage):
        Exception.__init__(self, errorMessage)


class Validator:

    URLRegex: re.Pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    @staticmethod
    def type(data: Any, type_: type) -> None:
        if not isinstance(data, type_):
            raise TypeError(f'Data is {type(data).__name__} while should be {type_.__name__}\nData = {data}')

    @staticmethod
    def keys(dictionary: dict, keys: List[str]) -> None:
        if not all([key in dictionary for key in keys]):
            missingKeys = [key for key in keys if not(key in dictionary)]
            raise ValueError(f'Dictionary misses such keys: {str(missingKeys)[1:-1]}')

    @staticmethod
    def compare(data: Union[int, float], operator: str, dataToCompare: Union[int, float]) -> None:
        comparisons = (
            {'operator': '>', 'text': 'bigger than', 'func': lambda: data > dataToCompare},
            {'operator': '>=', 'text': 'bigger or equal to', 'func': lambda: data >= dataToCompare},
            {'operator': '=', 'text': 'equal to', 'func': lambda: data == dataToCompare},
            {'operator': '!=', 'text': 'not equal to', 'func': lambda: data != dataToCompare},
            {'operator': '<', 'text': 'less than', 'func': lambda: data < dataToCompare},
            {'operator': '<=', 'text': 'less or equal to', 'func': lambda: data <= dataToCompare},
        )

        for comparison in comparisons:
            if comparison['operator'] == operator and not comparison['func']():
                raise ValueError(f'Data should be {comparison["text"]} {dataToCompare}\nData = {data}')

    @staticmethod
    def listOf(list_: list, object_: object) -> None:
        if not all([isinstance(element, object_) for element in list_]):
            raise ValueError(f'List containts not only objects of the class {object_.__name__}\nList = {list_}')

    @staticmethod
    def URL(cls, url: str) -> None:
        if re.match(cls.URLRegex, url) is None:
            raise ValueError(f'String {url} is not URL\nString = {url}')

    @staticmethod
    def digit(value: Any) -> None:
        type_ = type(value)
        if type_ != int and type_ != float:
            if type_ == str and not value.isdigit():
                raise ValidationError(f'Value {value} is not digit')
