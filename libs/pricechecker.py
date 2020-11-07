from typing import List

from abc import ABC, abstractmethod
import requests

import validators
from product import Price

class IPriceChecker(ABC):
  @abstractmethod
  def getPrice(self, barcode: int) -> Price: pass

class AWebPriceChecker(IPriceChecker):
  @abstractmethod
  def loadWebData(self) -> str: pass

  @staticmethod
  @abstractmethod
  def parsePrice(webData: str) -> Price: pass

  def getPrice(self, barcode: int) -> Price:
    return self.parsePrice( self.loadWebData(barcode) )

class NovusWPC(AWebPriceChecker):
  def __init__(self) -> None:
    self.url = 'https://novus.zakaz.ua/ru/products/'

  # <!-- SETTERS | GETTERS
  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, value: str) -> None:
    assert isinstance(value, str)
    assert validators.isURL(value)
    self._url = value
  # -->

  def loadWebData(self, barcode: int) -> str:
    return requests.get(self.url + barcode).text

  @staticmethod
  def parsePrice(webData: str) -> Price:
    html = webData
    # ... to be done
    date = { "day": 0, "month": 0, "year": 0, "hours": 0, "minutes": 0, "seconds": 0 }
    value = 0
    return Price( date, 'Novus', value)