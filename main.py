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
from solver import solve_cryptogram
from ocr import detect_text
import time
import os


#from kivy.core.window import Window
#Window.size = (360, 640)

class WelcomeScreen(Screen):
    pass

global timestr
timestr = None

class HomeScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        global timestr
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png(f"IMG_{timestr}.png")
        Clock.schedule_once(self.next_screen)

    def next_screen(self,dt):
        self.manager.current = 'transition'       

class TransitionScreen(Screen):
    def on_enter(self):
        global timestr
        self.ids.image.source = f'IMG_{timestr}.png'

class ResultScreen(Screen):  
    def on_pre_enter(self):
        #clearing text if any present
        self.ids.label2.text = ""
        self.ids.label3.text = ""
        self.ids.pb.value = 0

    def on_enter(self):
        global timestr
        self.ids.pb.value = 25
        self.ids.image.source = f'IMG_{timestr}.png'
        #self.ids.image.source = 'test_image_2.jpg'
        self.ids.label.text = f"Uploading Image"
        Clock.schedule_once(self.uploading,2)

    def uploading(self,dt):
        self.ids.pb.value = 50
        self.ids.label.text = "Image to Text Processing"
        self.image_text = detect_text(self.ids.image.source)
        #self.image_text = detect_text('test_image_2.jpg')
        self.ids.label2.text = self.image_text
        self.ids.label.text = "Waiting for User Input"

    def decrypt(self):
        self.ids.pb.value = 75
        self.ids.label.text = "Solving the Mystery"
        self.encrypted_text = solve_cryptogram()
        self.result = self.encrypted_text.solve(self.ids.label2.text)
        self.ids.label3.text = self.result
        Clock.schedule_once(self.processed)

    def processed(self,dt):
        self.ids.pb.value = 100
        self.ids.label.text = "Downloading Results"
        self.ids.start_over.size_hint = (0.35,0.06)
        self.ids.label.text = "Completed"


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