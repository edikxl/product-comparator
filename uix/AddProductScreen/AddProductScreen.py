from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.lang import Builder


class ScanerTab(MDBoxLayout, MDTabsBase):
    pass


class CustomTab(MDBoxLayout, MDTabsBase):
    pass


class AddProductScreen(MDBoxLayout):

    def onEnter(self):
        self.ids.camera.play = True

    def onLeave(self):
        self.ids.camera.play = False


Builder.load_file('./uix/AddProductScreen/AddProductScreen.kv')
