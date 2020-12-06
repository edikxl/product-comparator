from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder


class CounterLabel(IRightBodyTouch, MDLabel):
    pass


class AveragePriceLabel(IRightBodyTouch, MDLabel):
    pass


class ProductsScreen(MDFloatLayout):
    pass


Builder.load_file('./uix/ProductsScreen/ProductsScreen.kv')
