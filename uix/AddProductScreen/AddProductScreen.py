from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder


class ScanerTab(MDBoxLayout, MDTabsBase):
    pass


class CustomTab(MDBoxLayout, MDTabsBase):
    pass


class AddProductScreen(MDBoxLayout):

    def on_pre_enter(self):
        pass
        # self.ids.camera.play = True

    def on_pre_leave(self):
        pass
        # self.ids.camera.play = False

    def addProductByBarcode(self, barcode):
        App = MDApp.get_running_app()

        product = App.APIs.getProductFromBarcode(barcode)
        App.productsDB.addProduct(product)

        App.screenManager.transition.direction = 'left'
        App.screenManager.current = 'product'
        App.screenManager.current_screen.product = product
        App.screenManager.current_screen.loadProduct()


Builder.load_file('./uix/AddProductScreen/AddProductScreen.kv')
