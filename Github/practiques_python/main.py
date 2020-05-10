from kivy.app import App
"""Widgets are elements of a graphical user interface that form part of 
the User Experience. The kivy.uix module contains classes for creating 
and managing Widgets. Please refer to the Widget class documentation for further information."""
# BoxLayout arranges children in a vertical or horizontal box.
from kivy.uix.boxlayout import BoxLayout
"""The App class is the base for creating Kivy applications. 
Think of it as your main entry point into the Kivy 
run loop. In most cases, you subclass this class 
and make your own app. You create an instance of your 
specific app class and then, when you are ready to 
start the application’s life cycle, you call your 
instance’s App.run() method."""


class Calculator(BoxLayout):
    label = ''

    def delete(self, instance):
        self.display.text = instance[:0]

    def del1(self, instance):
        self.display.text = instance[:-1]

    def calc(self, instance):
        try:  # The try block lets you test a block of code for errors.
            # realitza els calculs amb eval method
            self.display.text = str(eval(instance))
            self.result.text = str(eval(instance))
        except Exception:  # The except block lets you handle the error.
            self.display.text = '0'
            self.result.text = 'ERROR'


class CalculatorApp(App):
    trigger = False
    triggerC = False
    triggerD = False

    def build(self):
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()
