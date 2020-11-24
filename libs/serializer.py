from typing import Union
from dataclasses import dataclass
from abc import ABC, abstractmethod
import json

from libs.validator import Validator
from libs.data import Product

Array = Union[list, dict, set, tuple]
FileData = Union[str, bytes]


class IEncoder(ABC):

    @staticmethod
    @abstractmethod
    def encode(array: Array) -> FileData:
        pass

    @staticmethod
    @abstractmethod
    def decode(fileData: FileData) -> Array:
        pass


class JSONEncoder(IEncoder):

    @staticmethod
    def encode(array: Array) -> FileData:
        return json.dumps(array)

    @staticmethod
    def decode(fileData: FileData) -> Array:
        return json.loads(fileData)


class INormalizer(ABC):

    @staticmethod
    @abstractmethod
    def normalize(obj: object) -> Array:
        pass

    @staticmethod
    @abstractmethod
    def denormalize(array: Array) -> object:
        pass


class ProductNormalizer(INormalizer):

    @staticmethod
    def normalize(product: Product) -> Array:
        pass

    @staticmethod
    def denormalize(array: Array) -> Product:
        pass


@dataclass
class Serializer:

    encoder: IEncoder
    normalizer: INormalizer

    # <!-- GETTERS | SETTERS
    @property
    def encoder(self) -> IEncoder:
        return self._encoder

    @encoder.setter
    def encoder(self, encoder: IEncoder) -> None:
        Validator.type(encoder, IEncoder)
        self._encoder = encoder

    @property
    def normalizer(self) -> INormalizer:
        return self._normalizer

    @normalizer.setter
    def normalizer(self, normalizer: INormalizer) -> None:
        Validator.type(normalizer, INormalizer)
        self._normalizer = normalizer
    # -->

    def serialize(self, obj: object) -> FileData:
        self.encoder.encode(self.normalizer.normalize(obj))

    def deserialize(self, fileData: FileData) -> object:
        self.normalizer.denormalize(self.encoder.decode(fileData))
