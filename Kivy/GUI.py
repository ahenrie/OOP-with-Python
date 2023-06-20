#pip install kivy
"""
    Application class: The main class that defines the application’s behavior and initializes the Kivy framework.
    Kv language: A domain-specific language for designing user interfaces. Kv files are separate from Python code and define the application’s appearance and layout.

"""

from kivy.app import App
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        return Label(text='Hello, World!')

if __name__ == '__main__':
    HelloWorldApp().run()

    
BoxLayout:
    orientation: 'vertical'

    Label:
        text: 'Enter your name:'

    TextInput:
        id: user_input
        multiline: False

    Button:
        text: 'Greet'
        on_press: output_label.text = 'Hello, ' + user_input.text

    Label:
        id: output_label
        text: 'Welcome!'
