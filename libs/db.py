from typing import Any, Union
from abc import ABC, abstractmethod
import json
import os

FileData = Union[str, bytes]
Array = Union[list, dict]

class IDataSource(ABC):
  def __init__(self, serializer: Serializer) -> None:
    self.serializer = serializer

  @abstractmethod
  def read(self) -> object: pass
  @abstractmethod
  def write(self, data: object) -> None: pass

class FileDS(IDataSource):
  def __init__(self, filePath: str, serializer: Serializer) -> None:
    IDataSource.__init__(self, serializer)
    self.filePath = filePath

  def read(self) -> object:
    with open(self.filePath, 'r') as file:
      return self.serializer.deserialize(file.read())

  def write(self, data: object) -> None:
    with open(self.filePath, 'w') as file:
      file.write(self.serializer.serialize(data))

class IEncoder(ABC):
  def encode(array: Array) -> FileData: pass
  def decode(fileData: FileData) -> Array: pass

class INormalizer(ABC):
  def normalize(obj: object) -> Array: pass
  def denormalize(array: Array) -> object: pass

class Serializer():
  def __init__(self, encoder: IEncoder, normalizer: INormalizer) -> None:
    self.encoder = encoder
    self.normalizer = normalizer

  def serialize(self, obj: object) -> FileData:
    self.encoder.encode(self.normalizer.normalize(obj))

  def deserialize(self, fileData: FileData) -> object:
    self.normalizer.denormalize(self.encoder.decode(fileData))

class JSONSerializer(ISerializer): pass # TODO

# SHIT'S BELOW

class IDataBase(ABC):
  @abstractmethod
  def read(self) -> Union[str, bytes]: pass
  @abstractmethod
  def write(self, data: Union[str, bytes]) -> None: pass
  @abstractmethod
  def load(self) -> None: pass
  @abstractmethod
  def save(self) -> None: pass

class ALocalDB(IDataBase):
  def __init__(self, dbPath: str) -> None:
    self.dbPath = dbPath

  # <!-- SETTERS | GETTERS
  @property
  def dbPath(self) -> str:
    return self._dbPath

  @dbPath.setter
  def dbPath(self, value: str) -> None:
    assert isinstance(value, str)
    assert os.path.exists(value)
    self._dbPath = value
  # -->

  def read(self) -> Union[str, bytes]:
    with open(self.dbPath, 'r') as file:
      return file.read()

  def write(self, data: Union[str, bytes]) -> None:
    with open(self.dbPath, 'w') as file:
      file.write(data)

class AJsonDB(IDataBase):
  def __init__(self) -> None:
    self.data = {}

  # <!-- SETTERS | GETTERS
  @property
  def data(self) -> dict:
    return self._data

  @data.setter
  def data(self, value: dict) -> None:
    assert isinstance(value, dict)
    self._data = value
  # -->

  def load(self) -> None:
    self.data = json.loads(self.read())

  def save(self) -> None:
    self.write(json.dumps(self.data))

class LocalJsonDB(ALocalDB, AJsonDB):
  def __init__(self, dbPath: str) -> None:
    ALocalDB.__init__(self, dbPath)
    AJsonDB.__init__(self)