from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


class SettingsScreen(BoxLayout):

    def on_pre_enter(self):
        pass

    def on_pre_leave(self):
        pass


Builder.load_file('./uix/SettingsScreen/SettingsScreen.kv')
