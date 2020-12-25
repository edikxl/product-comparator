from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.lang import Builder


class Source(OneLineAvatarIconListItem, TouchBehavior):

    name = StringProperty()
    imagePath = StringProperty()
    productsNumber = StringProperty()

    dialog = None

    def on_long_touch(self, *args):
        title = 'Удалить магазин (базу товаров)?'
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

        self.dialog = MDDialog(
            title=title,
            text=text,
            buttons=buttons,
            on_pre_dismiss=self.deleteDialog
        )

        self.dialog.open()

    def deleteDialog(self, *args):
        self.dialog = None

    def onDialogDismiss(self, *args):
        self.dialog.dismiss()

    def onDialogAccept(self, *args):
        self.deleteSource()
        self.dialog.dismiss()

    def deleteSource(self):
        App = MDApp.get_running_app()
        sourcesDB = App.sourcesDB

        for category in sourcesDB.data:
            if category.name == self.name:
                sourcesDB.data.remove(category)

        sourcesDB.save()

        self.parent.remove_widget(self)


class CounterLabel(IRightBodyTouch, MDLabel):
    pass


class ImageField(MDIconButton, Image):
    pass


class AddSourceDialogContent(MDBoxLayout):

    fileManager = None
    fileManagerStartingFolder = '/Users\\Edvein\\Downloads'
    imagePath = StringProperty()
    sourceName = StringProperty()

    def chooseImage(self):
        self.createFileManager()
        self.fileManager.show(self.fileManagerStartingFolder)

    def createFileManager(self):
        if not self.fileManager:
            self.fileManager = MDFileManager(
                exit_manager=self.onFileManagerExit,
                select_path=self.onFileManagerSelectPath,
                # preview=True
                # I HATE KIVYMD
                # https://github.com/kivymd/KivyMD/issues/531
            )

    def onFileManagerExit(self, *args):
        self.fileManager.close()

    def onFileManagerSelectPath(self, path):
        self.onFileManagerExit()
        # TODO Check if path is image and file at all
        print(path)
        self.imagePath = path
        self.ids.imageField.icon = ''
        self.ids.imageField.source = path


class SourcesScreen(MDFloatLayout):

    dialog = None

    def on_pre_enter(self):
        self.clearSources()
        self.addSources()

    def on_pre_leave(self):
        self.clearSources()

    def clearSources(self):
        self.ids.sourceList.clear_widgets()

    def addSources(self):
        App = MDApp.get_running_app()

        sourcesDB = App.sourcesDB
        productsDB = App.productsDB

        for source in sourcesDB.getSources():
            name = source.name
            imagePath = source.imagePath
            productsNumber = 0  # TODO NOT IMPLEMENTED len(productsDB.getProductsWithSourceName(source.name))

            self.addSource(name, imagePath, str(productsNumber))

        '''
        self.addSource('NOVUS', 'data/sources/Novus.jpeg', '10')
        self.addSource('Сiльпо', 'data/sources/Silpo.png', '6')
        self.addSource('Listex', 'data/sources/Listex.png', '15')
        '''

    def addSource(self, name: str, imagePath: str, productsNumber: str) -> None:
        source = Source()

        source.name = name
        source.imagePath = imagePath
        source.productsNumber = productsNumber

        self.ids.sourceList.add_widget(source)

    def openDialogToAddSource(self):
        title = 'Добавить новый магазин'
        content = AddSourceDialogContent()

        dismissButton = MDFlatButton(
            text='Отмена',
            on_release=self.onDialogDismiss,
            # text_color=self.theme_cls.primary_color
        )
        acceptButton = MDFlatButton(
            text='Добавить',
            on_release=self.onDialogAccept,
            # text_color=self.theme_cls.primary_color
        )
        buttons = [dismissButton, acceptButton]

        self.dialog = MDDialog(
            title=title,
            type='custom',
            content_cls=content,
            buttons=buttons,
            on_pre_dismiss=self.deleteDialog
        )

        self.dialog.open()

    def deleteDialog(self, *args):
        self.dialog = None

    def onDialogDismiss(self, *args):
        self.dialog.dismiss()

    def onDialogAccept(self, *args):
        # TODO Check if source with such a name already exists
        # TODO Check if fields aren't empty
        print('Dialog accept')
        self.dialog.dismiss()


Builder.load_file('./uix/SourcesScreen/SourcesScreen.kv')
