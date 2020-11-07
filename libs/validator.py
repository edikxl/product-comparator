from typing import Any, List, Union

class Validator:
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
  def notNegative(data: Union[int, float]) -> None:
    if data < 0:
      raise ValueError(f'Data is negative\nData = {data}')

  @staticmethod
  def listOf(list_: list, object_: object) -> None:
    if not all([isinstance(element, object_) for element in list_]):
      raise ValueError(f'List containts not only objects of the class {object_.__name__}')