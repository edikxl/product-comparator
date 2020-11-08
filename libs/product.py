from typing import List
from dataclasses import dataclass, field

from libs.validator import Validator

URL = str

@dataclass
class Price:
  date: dict
  store: str
  value: float

  # <!-- SETTERS | GETTERS
  @property
  def date(self) -> dict:
    return self._date
  @date.setter
  def date(self, date: dict) -> None:
    Validator.type(date, dict)
    Validator.keys(date, ["day", "month", "year", "hour", "minute", "second"])
    self._date = date

  @property
  def store(self) -> str:
    return self._store
  @store.setter
  def store(self, store) -> None:
    Validator.type(store, str)
    self._store = store  

  @property
  def value(self) -> float:
    return self._value
  @value.setter
  def value(self, value: float) -> None:
    Validator.type(value, float)
    Validator.compare(value, '>=', 0)
    self._value = value
  # -->

@dataclass
class Product:
  barcode: int
  characteristics: dict
  categories: List[str] = field(compare=False)
  links: List[URL] = field(compare=False)
  prices: List[Price] = field(compare=False)

  # <!-- SETTERS | GETTERS
  @property
  def barcode(self) -> int:
    return self._barcode
  @barcode.setter
  def barcode(self, barcode: int) -> None:
    Validator.type(barcode, int)
    Validator.compare(barcode, '>=', 0)
    self._barcode = barcode

  @property
  def characteristics(self) -> dict:
    return self._characteristics
  @characteristics.setter
  def characteristics(self, characteristics: dict) -> None:
    Validator.type(characteristics, dict)
    self._characteristics = characteristics

  @property
  def categories(self) -> List[str]:
    return self._categories
  @categories.setter
  def categories(self, categories: List[str]) -> None:
    Validator.type(categories, list)
    Validator.listOf(categories, str)
    self._categories = categories

  @property
  def links(self) -> List[URL]:
    return self._links
  @links.setter
  def links(self, links: List[URL]) -> None:
    Validator.type(links, list)
    map(Validator.URL, links)
    self._links = links

  @property
  def prices(self) -> List[Price]:
    return self._prices
  @prices.setter
  def prices(self, prices: List[Price]) -> None:
    Validator.type(prices, list)
    Validator.listOf(prices, Price)
    self._prices = prices
  # -->