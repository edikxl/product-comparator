from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Delete later

from uix import (ProductsScreen, SourcesScreen, AddProductScreen,  # noqa: F401
                NotificationsScreen, SettingsScreen)  # noqa: E128, F401


class Menu(BoxLayout):
    pass


class MainApp(MDApp):

    def build(self):
        self.title = 'Product Comporator'
        return Menu()


if __name__ == '__main__':
    Window.size = (360, 600)  # Delete later
    MainApp().run()
