from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from screen_nav import screen_helper

from kivy.core.window import Window
Window.size = (360, 640)

class WelcomeScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(HomeScreen(name='home'))

class Main(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        
        #wimage = Image(source="media/wallpaper.jpg")
        return screen

Main().run()