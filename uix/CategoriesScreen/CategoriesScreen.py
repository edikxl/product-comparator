from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder


class Category(OneLineAvatarIconListItem):
    pass


class CounterLabel(IRightBodyTouch, MDLabel):
    pass


class AveragePriceLabel(IRightBodyTouch, MDLabel):  # TODO Add this to the widget somehow
    pass


class CategoriesScreen(MDFloatLayout):

    def onEnter(self):
        self.clearCategories()
        self.addCategory('cart-outline', 'Все продукты', '13')
        self.addCategory('food-apple-outline', 'Фрукты', '8')
        self.addCategory('beer-outline', 'Соки', '5')

    def onLeave(self):
        self.clearCategories()

    def filterButtonCallback(self) -> None:
        pass

    def clearCategories(self):
        self.ids.categoryList.clear_widgets()

    def addCategory(self, icon: str, name: str, productNumber: str) -> None:
        category = Category()

        category.text = name
        category.ids.categoryIcon.icon = icon
        category.ids.productCounter.text = productNumber

        self.ids.categoryList.add_widget(category)


Builder.load_file('./uix/CategoriesScreen/CategoriesScreen.kv')
