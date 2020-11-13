from typing import List, Dict, Optional
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
  url: str


  # <!-- GETTERS | SETTERS
  # TODO
  # -->


@dataclass
class Product:

  barcode: int
  collections: List[str] = field(compare=False, default_factory=list)
  dataHistory: List[DataRecord] = field(compare=False, default_factory=list)


  # <!-- GETTERS | SETTERS
  @property
  def barcode(self) -> int:
    return self._barcode

  @barcode.setter
  def barcode(self, barcode: int) -> None:
    Validator.type(barcode, int)
    Validator.compare(barcode, '>=', 0)
    self._barcode = barcode

  # TODO self.collections GET SET

  # TODO self.dataHistory GET SET
  # -->


@dataclass
class Source:

  name: str
  logoImagePath: Optional[str]
  backgroundColor: str
  fontColor: str


  # <!-- GETTERS | SETTERS
  # TODO
  # -->