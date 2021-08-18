import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder

kv = Builder.load_file("menu.kv")
class MyLayout(Widget):
    def spinner_clicked(self, value):
        self.ids.click_label.text =f'you selected: {value}'

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()