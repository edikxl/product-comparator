from abc import ABC, abstractmethod
from typing import List

class Price:
  def __init__(self, date: dict, store: str, value: int) -> None:
    self.date = date
    self.store = store
    self.value = value

  # <!-- SETTERS | GETTERS
  @property
  def date(self) -> dict:
    return self._date

  @date.setter
  def date(self, value: dict) -> None:
    assert isinstance(value, dict)
    assert all([key in value for key in ["day", "month", "year", "hours", "minutes", "seconds"]])
    self._date = value
  
  @property
  def store(self) -> str:
    return self._store

  @store.setter
  def store(self, value) -> None:
    assert isinstance(value, str)
    self._store = value  

  @property
  def value(self) -> int:
    return self._value

  @value.setter
  def value(self, val: int) -> None:
    assert isinstance(val, int)
    assert 0 <= val
    self._value = val
  # -->


class Product:
  def __init__(self, barcode: int, characteristics: dict, prices: List[Price]) -> None:
    self.barcode = barcode
    self.characteristics = characteristics
    self.prices = prices

  # <!-- SETTERS | GETTERS
  @property
  def barcode(self) -> int:
    return self._barcode

  @barcode.setter
  def barcode(self, value: int) -> None:
    assert isinstance(value, int)
    assert 0 <= value
    self._barcode = value

  @property
  def characteristics(self) -> dict:
    return self._characteristics

  @characteristics.setter
  def characteristics(self, value: dict) -> None:
    assert isinstance(value, dict)
    self._characteristics = value

  @property
  def prices(self) -> List[Price]:
    return self._prices

  @prices.setter
  def prices(self, value: List[Price]) -> None:
    assert isinstance(value, list)
    assert all([isinstance(element, Price) for element in value])
    self._prices = value
  # -->