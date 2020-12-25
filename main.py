from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window  # Delete later

from uix import (  # noqa: F401
    CategoriesScreen, SourcesScreen, AddProductScreen,
    NotificationsScreen, SettingsScreen, AddCategoryScreen,
    CategoryScreen, ProductScreen)
from libs.serializer import (
    Serializer, JSONEncoder, ProductsNormalizer,
    SourcesNormalizer, CategoriesNormalizer
)
from libs.datasource import FileDS
from libs.database import (
    DataBase, CategoriesDBDecorator, ProductsDBDecorator, SourcesDBDecorator
)
from libs.API import APIs


class Menu(MDScreen):
    pass


class MainApp(MDApp):

    def build(self):
        self.title = 'Product Comporator'

        self.screenManager = ScreenManager(transition=SlideTransition())
        self.menu = Menu(name='menu')
        self.screenManager.add_widget(self.menu)
        # Сделать для каждого экрана back экран и автоматизировать это дело
        self.screenManager.add_widget(AddCategoryScreen(name='add-category'))
        self.screenManager.add_widget(CategoryScreen(name='category'))
        self.screenManager.add_widget(ProductScreen(name='product'))

        return self.screenManager

    def on_start(self):
        self.categoriesDB = DataBase(FileDS('data/categories.json', Serializer(JSONEncoder(list), CategoriesNormalizer())))
        self.categoriesDB.load()
        self.categoriesDB = CategoriesDBDecorator(self.categoriesDB)

        self.productsDB = DataBase(FileDS('data/products.json', Serializer(JSONEncoder(list), ProductsNormalizer())))
        self.productsDB.load()
        self.productsDB = ProductsDBDecorator(self.productsDB)

        self.sourcesDB = DataBase(FileDS('data/sources.json', Serializer(JSONEncoder(list), SourcesNormalizer())))
        self.sourcesDB.load()
        self.sourcesDB = SourcesDBDecorator(self.sourcesDB)

        self.APIs = APIs()

        print(f'{self.categoriesDB.data = }')
        print(f'{self.productsDB.data = }')
        print(f'{self.sourcesDB.data = }')

        self.menu.ids.categoriesScreen.on_pre_enter()

    def on_stop(self):
        pass

    def on_pause(self):
        pass

    def on_resume(self):
        pass


if __name__ == '__main__':
    Window.size = (360, 600)  # Delete later
    MainApp().run()
