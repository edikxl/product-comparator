from typing import Union, Any
from dataclasses import dataclass

from libs.datasource import IDataSource

Array = Union[list, dict, set, tuple]
ID = Union[str, int]


@dataclass
class DataBase:

    source: IDataSource
    data: Array = None

    # <!-- GETTERS | SETTERS
    # TODO
    # -->

    def load(self) -> None:
        self.data = self.source.read()

    def getField(self, id_: ID) -> Any:
        return self.data[id_]

    def setField(self, id_: ID, value: Any) -> None:
        self.data[id_] = value

    def save(self) -> None:
        self.source.write(self.data)
