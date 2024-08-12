from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class HelloWorld( App ):
    def build(self):
        return TextInput(
            font_size="50px")


HelloWorld().run()