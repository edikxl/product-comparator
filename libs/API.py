from typing import Any
from dataclasses import dataclass

import requests


class RequestToNonExistentMethod(Exception):

    def __init__(self, APIName: str, method: str) -> None:
        super().__init__(f'API {APIName} has no method {method}')


@dataclass
class API:

    name: str

    # TODO GET SET name

    def getMethods(self) -> list:
        methods = []

        for attribute in dir(self):
            if not attribute.startswith('__') and callable(getattr(self, attribute)):
                methods.append(attribute)

        return methods

    def request(self, methodName: str, *args: list, **kwargs: dict) -> Any:
        return getattr(self, methodName)(self, *args, **kwargs)


@dataclass
class NovusAPI(API):

    _url: str = 'https://novus.zakaz.ua/ru/products/'

    def price(self, barcode: int) -> dict:
        response = {'price': None}

        html = requests.get(self.url + barcode).text
        # ... TODO parsing price

        return response


class SilpoAPI(API):

    def price(self, barcode: int) -> dict:
        pass


class ListexAPI(API):

    def product(self, barcode: int) -> dict:
        pass

    def suggestions(self, brandName: str) -> dict:
        pass


class APIs:

    def __init__(self) -> None:
        self._APIs = [NovusAPI, SilpoAPI, ListexAPI]

    def getAPIByName(self, APIName: str) -> API:
        for API in self._APIs:
            if API.name == APIName:
                return API

        return None

    def request(self, APIName: str, method: str, *args: tuple) -> Any:
        API = self._APIs[APIName]
        if method in API.getMethods():
            return API.request(method, args)

        raise RequestToNonExistentMethod(APIName, method)

    def requestAll(self, method: str, *args: tuple) -> list:
        responses = []
        for API in self._APIs:
            responses.append(self.request(method, args, API.name))

        return responses


""" USAGE EXAMPLES
APIs.request('Novus', 'price', 4820226161653)
APIs.requestAll('price', 4820226161653)
APIs.request('Listex', 'product', 4820226161653)
APIs.request('Listex', 'suggestions', 'Біфідойогурт Чорниця-Інжир Активіа 270г')
"""
