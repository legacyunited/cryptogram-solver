from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main(App):
    def build(self):
        return MDLabel(text='Hello World',halign='center')

Main().run()