from typing import List, Optional, Any
from dataclasses import dataclass, field

from libs.validator import Validator


@dataclass
class Date:

    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    # <!-- GETTERS | SETTERS
    # TODO
    # -->


@dataclass
class DataRecord:

    date: Date
    source: str
    fields: dict
    mode: str
    URL: str

    # <!-- GETTERS | SETTERS
    # TODO
    # -->


@dataclass
class Product:

    barcode: str
    imagePath: str = field(compare=False)
    categories: List[str] = field(compare=False)
    dataHistory: List[DataRecord] = field(compare=False)

    # <!-- GETTERS | SETTERS
    @property
    def barcode(self) -> str:
        return self._barcode

    @barcode.setter
    def barcode(self, barcode: str) -> None:
        Validator.type(barcode, str)
        self._barcode = barcode

    @property
    def imagePath(self) -> str:
        return self._imagePath

    @imagePath.setter
    def imagePath(self, imagePath: str) -> None:
        Validator.type(imagePath, str)
        self._imagePath = imagePath

    @property
    def categories(self) -> List[str]:
        return self._categories

    @categories.setter
    def categories(self, categories: List[str]) -> None:
        Validator.listOf(categories, str)
        self._categories = categories

    @property
    def dataHistory(self) -> List[DataRecord]:
        return self._dataHistory

    @dataHistory.setter
    def dataHistory(self, dataHistory: List[DataRecord]) -> None:
        Validator.listOf(dataHistory, DataRecord)
        self._dataHistory = dataHistory
    # -->

    def getNewestField(self, fieldName: str) -> Any:
        for dataRecord in self.dataHistory:
            if fieldName in dataRecord.fields.keys():
                return dataRecord.fields[fieldName]

        return None


@dataclass
class Source:

    name: str
    imagePath: Optional[str] = field(compare=False)

    # <!-- GETTERS | SETTERS
    # TODO
    # -->


@dataclass
class Category:

    name: str
    icon: str = field(compare=False)

    # <!-- GETTERS | SETTERS
    # TODO
    # -->
