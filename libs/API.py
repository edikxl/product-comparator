from abc import ABC, abstractmethod
import datetime

import requests
from bs4 import BeautifulSoup

from libs.data import Product, DataRecord, Date


class API(ABC):

    @abstractmethod
    def getFields(self) -> dict:
        pass


class NovusAPI(API):

    URL = 'https://novus.zakaz.ua/ru/products/'

    def getFields(self, barcode: str):
        URL = self.URL + str(barcode)
        html = requests.get(URL).text
        soup = BeautifulSoup(html, 'html.parser')

        fields = {
            'URL': URL,
            'imageURL': self.parseImageURL(soup),
            'name': self.parseName(soup),
            'price': self.parsePrice(soup),
            'weight': self.parseWeight(soup),
            'ingridients': self.parseIngridients(soup),
        }

        return fields

    def parseImageURL(self, soup: BeautifulSoup) -> str:
        return soup.select_one('.ZooomableImageSwitcher__smallImg')['src']

    def parseName(self, soup: BeautifulSoup) -> str:
        return soup.select_one('.big-product-card__title').text

    def parsePrice(self, soup: BeautifulSoup) -> float:
        return soup.select_one('.Price__value_title').text

    def parseWeight(self, soup: BeautifulSoup) -> str:
        return soup.select_one('.big-product-card__amount').text

    def parseIngridients(self, soup: BeautifulSoup) -> str:
        wrapper = soup.select_one('.big-product-card__ingredients')
        innerContent = wrapper.select_one('.big-product-card__long-text')

        ingridients = innerContent.text

        return ingridients


class SilpoAPI(API):

    getPriceURL = ''

    def getFields(self, barcode: str):
        raise NotImplementedError


class ListexAPI(API):

    def getFields(self, barcode: str) -> dict:
        return self.product(barcode)  # ?

    def product(self, barcode: str) -> dict:
        raise NotImplementedError

    def suggestions(self, brandName: str) -> dict:
        raise NotImplementedError


class APIs:

    def __init__(self) -> None:
        self._APIs = {
            'Novus': NovusAPI(),
            # 'Silpo': SilpoAPI(),
            # 'Listex': ListexAPI(),
        }

    def get(self, name: str) -> API:
        return self._APIs[name]

    def getAll(self) -> dict:
        return self._APIs.copy()  # TODO WARNING POTENTIAL DEEP BUG

    def getFields(self, barcode: int) -> dict:
        fields = {}

        for APIName, API in self._APIs.items():
            fields[APIName] = API.getFields(barcode)

        return fields

    def getProductFromBarcode(self, barcode: int) -> dict:
        allFields = self.getFields(barcode)

        imageURL = allFields['Novus']['imageURL']
        imagePath = 'data/products/' + barcode + '.jpg'  # TODO CHECK IF DATA FORMAT IS NOT JPG
        # https://www.tutorialspoint.com/downloading-files-from-web-using-python
        with open(imagePath, 'wb') as imageFile:
            imageFile.write(requests.get(imageURL).content)

        categories = []
        dataHistory = []

        for APIFieldsName, APIFields in allFields.items():
            today = datetime.date.today()
            now = datetime.datetime.now()
            date = Date(today.year, today.month, today.day, now.hour, now.minute, now.second)

            source = APIFieldsName
            fields = APIFields
            mode = 'API'
            URL = APIFields['URL']

            dataHistory.insert(0, DataRecord(date, source, fields, mode, URL))

        return Product(barcode, imagePath, categories, dataHistory)


'''
APIs = APIs()

APIs.get('Novus').getFields()
APIs.get('Novus').price(4820226161653)
APIs.get('Listex').suggestions('Йогурт')
'''
