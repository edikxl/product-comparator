#from abc import ABC, abstractmethod
from kivy.app import App
from kivy.uix.button import Button
 
class MainApp(App):
    def build(self):
        return Button(text = "Press me :3")

MainApp().run()

# | TODO Asserts removing |
# Убрать все assert-ы которые проверяют валидность данных
# Вместо них сделать библиотеку валидатор что и будет готовой лабой