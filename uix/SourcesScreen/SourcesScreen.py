from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder


class Source(OneLineAvatarIconListItem):
    pass


class CounterLabel(IRightBodyTouch, MDLabel):
    pass


class SourcesScreen(MDFloatLayout):

    def onEnter(self):
        self.clearSources()
        self.addSource('data/sources/Novus.jpeg', 'NOVUS', '10')
        self.addSource('data/sources/Silpo.png', 'Сiльпо', '6')
        self.addSource('data/sources/Listex.png', 'Listex', '15')

    def onLeave(self):
        self.clearSources()

    def clearSources(self):
        self.ids.sourceList.clear_widgets()

    def addSource(self, imageSource: str, name: str, productNumber: str) -> None:
        source = Source()

        source.text = name
        source.ids.image.source = imageSource
        source.ids.productCounter.text = productNumber

        self.ids.sourceList.add_widget(source)


Builder.load_file('./uix/SourcesScreen/SourcesScreen.kv')
