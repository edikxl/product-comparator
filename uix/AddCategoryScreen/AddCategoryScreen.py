from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
from kivy.lang import Builder

from libs.data import Category


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class AddCategoryScreen(MDScreen):

    def on_pre_enter(self):
        self.ids.nameField.text = ''
        self.ids.iconField.text = 'cart'

    def onBack(self):
        App = MDApp.get_running_app()

        App.screenManager.transition.direction = 'right'
        App.screenManager.current = 'menu'

    def onSave(self):
        App = MDApp.get_running_app()

        name = self.ids.nameField.text
        icon = self.ids.iconField.text

        # TODO Check if category already exists
        # TODO Check if fields aren't empty

        category = Category(name, icon)

        App.categoriesDB.data.append(category)
        App.categoriesDB.save()

        App.screenManager.transition.direction = 'right'
        App.screenManager.current = 'menu'
        App.menu.ids.categoriesScreen.on_pre_enter()

    def setIcon(self, iconName):
        self.ids.iconField.text = iconName

    def setListOfIcons(self, text='', search=False):

        def addIconItem(iconName):
            self.ids.rv.data.append(
                {
                    'viewclass': 'CustomOneLineIconListItem',
                    'icon': iconName,
                    'text': iconName,
                    'callback': lambda x: x,
                    'on_release': lambda: self.setIcon(iconName),
                }
            )

        self.ids.rv.data = []
        for iconName in md_icons.keys():
            if search:
                if text in iconName:
                    addIconItem(iconName)
            else:
                addIconItem(iconName)


Builder.load_file('./uix/AddCategoryScreen/AddCategoryScreen.kv')
