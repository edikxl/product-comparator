from typing import Any, Union, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod
import json
import os

from libs.validator import Validator
from libs.product import Product, Price

Array = Union[list, dict, set, tuple]
FileData = Union[str, bytes]
ID = Union[str, int]

class IEncoder(ABC):
  @staticmethod
  @abstractmethod
  def encode(array: Array) -> FileData: pass
  @staticmethod
  @abstractmethod
  def decode(fileData: FileData) -> Array: pass

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
  def normalize(obj: object) -> Array: pass
  @staticmethod
  @abstractmethod
  def denormalize(array: Array) -> object: pass

class ProductNormalizer(INormalizer):
  @staticmethod
  def normalize(product: Product) -> Array: pass
  @staticmethod
  def denormalize(array: Array) -> Product: pass

@dataclass
class Serializer:
  encoder: IEncoder
  normalizer: INormalizer

  # <!-- SETTERS | GETTERS
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

@dataclass
class IDataSource(ABC):
  serializer: Serializer

  # <!-- SETTERS | GETTERS
  @property
  def serilizer(self) -> Serializer:
    return self._serilizer
  @serilizer.setter
  def serilizer(self, serilizer: Serializer) -> None:
    Validator.type(serilizer, Serializer)
    self._serilizer = serilizer
  # -->

  @abstractmethod
  def read(self) -> object: pass
  @abstractmethod
  def write(self, data: object) -> None: pass

class FileDS(IDataSource):
  def __init__(self, filePath: str, serializer: Serializer) -> None:
    IDataSource.__init__(self, serializer)
    self.filePath = filePath # TODO GET SET

  def read(self) -> object:
    try:
      with open(self.filePath, 'r') as file:
        return self.serializer.deserialize(file.read())
    except UnicodeDecodeError: # FIX Something quite strange happening there with encodings
      with open(self.filePath, 'rb') as file:
        fileData = file.read().decode('utf-8-sig').encode('utf8')
        #print(fileData)
        return self.serializer.deserialize(fileData)

  def write(self, data: object) -> None:
    with open(self.filePath, 'w') as file:
      file.write(self.serializer.serialize(data))

@dataclass
class DataBase:
  source: IDataSource
  data: Array = None

  def load(self):
    self.data = self.source.read()

  def field(self, id_: ID, value: Any = None) -> Any:
    if value is None: # FIX If user wants to set field value to None he or she won't be able
      return self.data[id_]
    self.data[id_] = value
    self.save()

  def save(self):
    self.source.write(self.data)