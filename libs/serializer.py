from typing import Union, List
from dataclasses import dataclass
from abc import ABC, abstractmethod
import json

from libs.validator import Validator
from libs.data import Product, Date, DataRecord, Source, Category

Array = Union[list, dict, set, tuple]
FileData = Union[str, bytes]


class IEncoder(ABC):

    @abstractmethod
    def encode(self, array: Array) -> FileData:
        pass

    @abstractmethod
    def decode(self, fileData: FileData) -> Array:
        pass


class JSONEncoder(IEncoder):

    def __init__(self, defaultType: type):
        self._defaultType = defaultType

    def encode(self, array: Array) -> FileData:
        return json.dumps(array)

    def decode(self, fileData: FileData) -> Array:
        if not fileData:
            return self._defaultType()

        return json.loads(fileData)


class INormalizer(ABC):

    @abstractmethod
    def normalize(self, obj: object) -> Array:
        pass

    @abstractmethod
    def denormalize(self, array: Array) -> object:
        pass


class ProductsNormalizer(INormalizer):

    def normalize(self, products: List[Product]) -> list:
        array = []

        for product in products:
            barcode = product.barcode
            imagePath = product.imagePath
            categories = product.categories
            dataHistory = []
            for dataRecord in product.dataHistory:
                date = dataRecord.date

                dataHistory.append({
                    'date': {
                        'year': date.year,
                        'month': date.month,
                        'day': date.day,
                        'hour': date.hour,
                        'minute': date.minute,
                        'second': date.second
                    },
                    'source': dataRecord.source,
                    'fields': dataRecord.fields,
                    'mode': dataRecord.mode,
                    'URL': dataRecord.URL
                })

            array.append({
                'barcode': barcode,
                'imagePath': imagePath,
                'categories': categories,
                'dataHistory': dataHistory
            })

        return array

    def denormalize(self, array: list) -> List[Product]:
        products = []

        for product in array:
            barcode = product['barcode']
            imagePath = product['imagePath']
            categories = product['categories']
            dataHistory = product['dataHistory']
            for position, dataRecord in enumerate(dataHistory):
                date = dataRecord['date']
                year = date['year']
                month = date['month']
                day = date['day']
                hour = date['hour']
                minute = date['minute']
                second = date['second']

                date = Date(year, month, day, hour, minute, second)
                source = dataRecord['source']
                fields = dataRecord['fields']
                mode = dataRecord['mode']
                URL = dataRecord['URL']

                dataHistory[position] = DataRecord(date, source, fields, mode, URL)

            products.append(Product(barcode, imagePath, categories, dataHistory))

        return products


class SourcesNormalizer(INormalizer):

    def normalize(self, sources: List[Source]) -> list:
        raise NotImplementedError

    def denormalize(self, array: list) -> List[Source]:
        sources = []

        for source in array:
            name = source['name']
            imagePath = source['image-path']

            sources.append(Source(name, imagePath))

        return sources


class CategoriesNormalizer(INormalizer):

    def normalize(self, categories: List[Category]) -> list:
        array = []

        for category in categories:
            array.append({
                'name': category.name,
                'icon': category.icon,
            })

        return array

    def denormalize(self, array: list) -> List[Category]:
        categories = []

        for category in array:
            name = category['name']
            icon = category['icon']

            categories.append(Category(name, icon))

        return categories


class ListNormalizer(INormalizer):

    def normalize(self, list_: list) -> list:
        return list_

    def denormalize(self, list_: list) -> list:
        return list_


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
        return self.encoder.encode(self.normalizer.normalize(obj))

    def deserialize(self, fileData: FileData) -> object:
        return self.normalizer.denormalize(self.encoder.decode(fileData))
