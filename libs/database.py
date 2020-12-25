from typing import Union, Any, List
from dataclasses import dataclass

from libs.datasource import ADataSource
from libs.data import Category, Source, Product

Array = Union[list, dict, set, tuple]
ID = Union[str, int]


@dataclass
class IDataBase():

    def load(self) -> None:
        pass

    def getField(self, id_: ID) -> Any:
        pass

    def setField(self, id_: ID, value: Any) -> None:
        pass

    def save(self) -> None:
        pass


@dataclass
class DataBase(IDataBase):

    source: ADataSource
    data: Array = None

    # <!-- GETTERS | SETTERS
    # TODO
    # -->

    def load(self) -> None:
        self.data = self.source.read()

    def getField(self, id_: ID) -> Any:
        return self.data[id_]

    def setField(self, id_: ID, value: Any) -> None:
        self.data[id_] = value
        self.save()

    def save(self) -> None:
        self.source.write(self.data)


class DBDecorator(IDataBase):

    _db: IDataBase = None

    def __init__(self, db: IDataBase) -> None:
        self._db = db
        self.source = self._db.source
        self.data = self._db.data

    def load(self) -> None:
        self._db.load()

    def getField(self, id_: ID) -> str:
        return self._db.getField(id_)

    def setField(self, id_: ID, value: Any) -> None:
        self._db.setField(id_, value)

    def save(self) -> None:
        self._db.save()


class CategoriesDBDecorator(DBDecorator):

    def getCategory(self, categoryName: str) -> Category:
        if categoryName == 'Все продукты':
            return Category('Все продукты', 'cart')
        else:
            for category in self.data:
                if category.name == categoryName:
                    return category

    def getCategories(self) -> List[Category]:
        categories = self.data.copy()  # TODO WARNING POTENTIAL DEEP BUG
        categories.insert(0, Category('Все продукты', 'cart'))

        return categories


class ProductsDBDecorator(DBDecorator):

    def addProduct(self, product: Product):
        self.data.insert(0, product)
        self.save()

    def getProducts(self):
        return self.data.copy()  # TODO WARNING POTENTIAL DEEP BUG

    def getProductsWithCategoryName(self, categoryName: str) -> str:
        products = []
        for product in self.getProducts():
            if categoryName in product.categories or categoryName == 'Все продукты':
                products.append(product)

        return products

    def getProductsWithSourceName(self, sourceName: str) -> str:
        raise NotImplementedError


class SourcesDBDecorator(DBDecorator):

    def getSource(self, sourceName: str) -> Source:
        raise NotImplementedError

    def getSources(self) -> List[Source]:
        sources = self.data.copy()  # TODO WARNING POTENTIAL DEEP BUG
        # TODO AUTOMATE IT VIA APIS
        sources.insert(0, Source('Listex', 'data/sources/Listex.png'))
        sources.insert(0, Source('Сiльпо', 'data/sources/Silpo.png'))
        sources.insert(0, Source('NOVUS', 'data/sources/Novus.jpeg'))

        return sources
