from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class HelloWorld( App ):
    def build(self):
        return Button(
            text = "Hello World",
            color="purple",
            font_size="50px")


HelloWorld().run()