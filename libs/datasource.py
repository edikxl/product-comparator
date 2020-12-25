from dataclasses import dataclass
from abc import ABC, abstractmethod

from libs.serializer import Serializer
from libs.validator import Validator


@dataclass
class ADataSource(ABC):

    serializer: Serializer

    # <!-- GETTERS | SETTERS
    @property
    def serializer(self) -> Serializer:
        return self._serializer

    @serializer.setter
    def serializer(self, serializer: Serializer) -> None:
        Validator.type(serializer, Serializer)
        self._serializer = serializer
    # -->

    @abstractmethod
    def read(self) -> object:
        pass

    @abstractmethod
    def write(self, data: object) -> None:
        pass


class FileDS(ADataSource):

    def __init__(self, filePath: str, serializer: Serializer) -> None:
        ADataSource.__init__(self, serializer)
        self.filePath = filePath

    # <!-- GETTERS | SETTERS
    # TODO
    # -->

    def read(self) -> object:
        try:
            with open(self.filePath, 'a+') as file:
                file.seek(0)
                return self.serializer.deserialize(file.read())

        # FIX Something quite strange happening there with encodings
        except UnicodeDecodeError:
            with open(self.filePath, 'rb+') as file:
                fileData = file.read().decode('utf-8-sig').encode('utf8')
                # print(fileData)
                return self.serializer.deserialize(fileData)

    def write(self, data: object) -> None:
        with open(self.filePath, 'w') as file:
            file.write(self.serializer.serialize(data))
