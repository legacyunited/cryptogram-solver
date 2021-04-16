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

global number
number = 0

class HomeScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        #timestr = time.strftime("%Y%m%d_%H%M%S")
        #camera.export_to_png("IMG_{}.png".format(timestr))
        camera.export_to_png(f"IMG_{number}.png")
        Clock.schedule_once(self.next_screen)

    def next_screen(self,dt):
        self.manager.current = 'transition'       

class TransitionScreen(Screen):
    def on_enter(self):
        global number
        self.ids.image.source = f'IMG_{number}.png'
        number += 1

class ResultScreen(Screen):       
    def on_enter(self):
        self.ids.spinner.active = True
        global number
        print('uploading image')
        self.ids.label.text = f"Uploading Image - IMG_{number}.png"
        Clock.schedule_once(self.uploading, 4)

    def uploading(self,dt):
        print('extracting text')
        self.ids.label.text = "Image to Text Processingggggggggggggggggggggggggggggggggggggggggggggggggggggg"
        Clock.schedule_once(self.processed, 4)
        
    def processed(self,dt):
        print('downloading results')
        self.ids.label.text = "Downloading Results"
        self.ids.spinner.active = False
        self.ids.start_over.size_hint = (0.5,0.1)


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(TransitionScreen(name='transition'))
sm.add_widget(TransitionScreen(name='result'))

class Main(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    

Main().run()