from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Delete later

from uix import (CategoriesScreen, SourcesScreen, AddProductScreen,  # noqa: F401
                NotificationsScreen, SettingsScreen)  # noqa: E128, F401
# from libs.database import Database


class Menu(BoxLayout):
    pass


class MainApp(MDApp):

    def build(self):
        self.title = 'Product Comporator'
        return Menu()

    def on_start(self):
        self.root.ids.categoriesScreen.onEnter()

        # self.db = Database()

    def on_stop(self):
        pass

    def on_resume(self):
        pass

    def on_pause(self):
        pass


if __name__ == '__main__':
    Window.size = (360, 600)  # Delete later
    MainApp().run()
