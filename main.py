from kivy.app import App
from kivy.uix.button import Button
 
class MainApp(App):
    def build(self):
        return Button(text="Press me :3")

MainApp().run()