from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.window import Window  # Delete later

from libs.validator import Validator, ValidationError


class ExceptionTest(BoxLayout):

    def __init__(self, **kwargs):
        Window.size = (300, 100)  # Delete later

        super(ExceptionTest, self).__init__(**kwargs)
        self.orientation = 'vertical'

        productBox = BoxLayout(orientation='horizontal')
        productBox.add_widget(Label(text='Product Name'))
        productBox.product = TextInput(multiline=False)
        productBox.add_widget(productBox.product)

        priceBox = BoxLayout(orientation='horizontal')
        priceBox.add_widget(Label(text='Price'))
        priceBox.price = TextInput(multiline=False)
        priceBox.price.bind(text=self.validatePrice)
        priceBox.add_widget(priceBox.price)

        buttonBox = BoxLayout(orientation='horizontal')
        buttonBox.add_widget(Button(text='Add product'))

        self.add_widget(productBox)
        self.add_widget(priceBox)
        self.add_widget(buttonBox)

    # Check later
    # https://kivy.org/doc/stable/api-kivy.uix.textinput.html#filtering
    @staticmethod
    def validatePrice(instance, value):
        try:
            Validator.digit(value)
        except ValidationError:
            instance.foreground_color = [1, 0, 0, 1]
        else:
            instance.foreground_color = [0, 0, 0, 1]


class MainApp(App):

    def build(self):
        return ExceptionTest()


if __name__ == '__main__':
    MainApp().run()
