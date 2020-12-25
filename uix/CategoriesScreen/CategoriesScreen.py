from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty
from kivy.lang import Builder


class Category(OneLineAvatarIconListItem, TouchBehavior):
    name = StringProperty()
    icon = StringProperty()
    productsNumber = StringProperty()

    dialog = None

    def on_release(self):
        if not self.dialog:
            self.openCategory()

    def on_long_touch(self, *args):
        title = 'Удалить категорию?'
        text = f'Это безвозвратно удалит \'{self.name}\'!'

        dismissButton = MDFlatButton(
            text='Нет',
            on_release=self.onDialogDismiss,
            text_color=self.theme_cls.primary_color
        )
        acceptButton = MDFlatButton(
            text='Да',
            on_release=self.onDialogAccept,
            text_color=self.theme_cls.primary_color
        )
        buttons = [dismissButton, acceptButton]

        self.dialog = MDDialog(title=title, text=text, buttons=buttons, on_pre_dismiss=self.deleteDialog)

        self.dialog.open()

    def deleteDialog(self, *args):
        self.dialog = None

    def onDialogDismiss(self, *args):
        self.dialog.dismiss()

    def onDialogAccept(self, *args):
        self.deleteCategory()
        self.dialog.dismiss()

    def deleteCategory(self):
        App = MDApp.get_running_app()
        categoriesDB = App.categoriesDB

        for category in categoriesDB.data:
            if category.name == self.name:
                categoriesDB.data.remove(category)

        categoriesDB.save()

        self.parent.remove_widget(self)

    def openCategory(self):
        App = MDApp.get_running_app()

        App.screenManager.transition.direction = 'left'
        App.screenManager.current = 'category'
        screen = App.screenManager.current_screen
        screen.categoryName = self.name
        screen.categoryIcon = self.icon
        screen.categoryProductsNumber = self.productsNumber
        screen.loadProducts()


class CounterLabel(IRightBodyTouch, MDLabel):
    pass


class AveragePriceLabel(IRightBodyTouch, MDLabel):  # TODO Add this to the widget somehow
    pass


class CategoriesScreen(MDFloatLayout):

    def on_pre_enter(self):
        self.clearCategories()
        self.loadCategories()

    def on_pre_leave(self):
        self.clearCategories()

    def filterButtonCallback(self) -> None:
        pass

    def clearCategories(self):
        self.ids.categoryList.clear_widgets()

    def loadCategories(self):
        App = MDApp.get_running_app()

        categoriesDB = App.categoriesDB
        productsDB = App.productsDB

        for category in categoriesDB.getCategories():
            name = category.name
            icon = category.icon
            productsNumber = len(productsDB.getProductsWithCategoryName(category.name))

            self.addCategory(name, icon, str(productsNumber))

        '''
        self.addCategory('cart-outline', 'Все продукты', '13')
        self.addCategory('food-apple-outline', 'Фрукты', '8')
        self.addCategory('beer-outline', 'Соки', '5')
        '''

    def addCategory(self, name: str, icon: str, productsNumber: str) -> None:
        category = Category()

        category.name = name
        category.icon = icon
        category.productsNumber = productsNumber

        self.ids.categoryList.add_widget(category)

    def changeScreenToAddCategory(self):
        App = MDApp.get_running_app()

        App.screenManager.transition.direction = 'left'
        App.screenManager.current = 'add-category'


Builder.load_file('./uix/CategoriesScreen/CategoriesScreen.kv')
