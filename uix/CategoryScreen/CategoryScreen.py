from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivy.properties import StringProperty
from kivy.lang import Builder


class ProductItem(OneLineAvatarIconListItem, TouchBehavior):

    product = None
    name = StringProperty()
    imagePath = StringProperty()
    averagePrice = StringProperty()

    dialog = None

    def on_release(self):
        if not self.dialog:
            self.openProduct()

    def openProduct(self):
        App = MDApp.get_running_app()

        App.screenManager.transition.direction = 'left'
        App.screenManager.current = 'product'
        App.screenManager.current_screen.product = self.product
        App.screenManager.current_screen.loadProduct()


class PriceLabel(IRightBodyTouch, MDLabel):
    pass


class CategoryScreen(MDScreen):

    categoryName = StringProperty()
    categoryIcon = StringProperty()
    categoryProductsNumber = StringProperty()

    def on_pre_enter(self):
        pass

    def on_pre_leave(self):
        self.clearProductList()

    def onBack(self):
        App = MDApp.get_running_app()

        App.screenManager.transition.direction = 'right'
        App.screenManager.current = 'menu'

    def loadProducts(self):
        App = MDApp.get_running_app()
        productsDB = App.productsDB

        products = productsDB.getProductsWithCategoryName(self.categoryName)

        for product in products:
            self.addProduct(product)

    def addProduct(self, productObject):
        name = productObject.getNewestField('name')
        imagePath = productObject.imagePath
        averagePrice = productObject.getNewestField('price')  # TODO ADD AVERAGE PRICE

        product = ProductItem()
        product.product = productObject
        product.name = str(name)
        product.imagePath = str(imagePath)
        product.averagePrice = str(averagePrice)

        self.ids.productList.add_widget(product)

    def clearProductList(self):
        self.ids.productList.clear_widgets()


Builder.load_file('./uix/CategoryScreen/CategoryScreen.kv')
