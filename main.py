from typing import Any

from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window  # Delete later
Window.size = (300, 100)  # Delete later

from libs.validator import Validator, ValidationError  # noqa: E402


class ExceptionTest(BoxLayout):

    @staticmethod
    def validatePrice(instance: object, value: Any) -> None:
        try:
            Validator.digit(value)
        except ValidationError:
            instance.foreground_color = [1, 0, 0, 1]
        else:
            instance.foreground_color = [0, 0, 0, 1]


class MainApp(App):

    def build(self) -> Layout:
        self.title = 'Product Comporator'
        return ExceptionTest()


if __name__ == '__main__':
    MainApp().run()
