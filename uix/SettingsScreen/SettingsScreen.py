from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class SettingsScreen(BoxLayout):

    def onEnter(self):
        pass

    def onLeave(self):
        pass


Builder.load_file('./uix/SettingsScreen/SettingsScreen.kv')
