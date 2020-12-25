from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.lang import Builder

from libs.data import Product


class ProductScreen(MDScreen):

    product = Product('', '', [], [])
    productName = StringProperty('')
    barcode = StringProperty('')
    price = StringProperty('')
    imagePath = StringProperty('')
    ingridients = StringProperty('')
    collections = StringProperty('')
    dataHistory = StringProperty('')

    def onBack(self):
        App = MDApp.get_running_app()

        App.screenManager.transition.direction = 'right'
        App.screenManager.current = 'menu'

    def loadProduct(self):
        self.productName = self.product.getNewestField('name')
        self.barcode = self.product.barcode
        self.price = self.product.getNewestField('price')
        self.imagePath = self.product.imagePath
        self.ingridients = self.product.getNewestField('ingridients')
        # self.collections = self.product.getNewestField('name')
        # self.dataHistory = self.product.getNewestField('name')

    def updateProductData(self):  # VIA API
        raise NotImplementedError


Builder.load_file('./uix/ProductScreen/ProductScreen.kv')
