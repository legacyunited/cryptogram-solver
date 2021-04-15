from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from screen_nav import screen_helper
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivymd.uix.progressbar import ProgressBar
from kivy.cache import Cache
import time
import os


from kivy.core.window import Window
Window.size = (360, 640)


class WelcomeScreen(Screen):
    pass

class HomeScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        #timestr = time.strftime("%Y%m%d_%H%M%S")
        #camera.export_to_png("IMG_{}.png".format(timestr))
        camera.export_to_png("IMG.png")
        Clock.schedule_once(self.next_screen)

    def next_screen(self,dt):
        self.manager.current = 'transition'       

class TransitionScreen(Screen):
    def on_enter(self):
        Cache.remove('image')
        self.ids.image.source = 'IMG.png'

class LoadingScreen(Screen):
    def next_screen(self):
        self.manager.current = 'result'

class ResultScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(TransitionScreen(name='transition'))
sm.add_widget(TransitionScreen(name='loading'))
sm.add_widget(TransitionScreen(name='result'))

class Main(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    

Main().run()