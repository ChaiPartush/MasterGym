# from kivy.uix.textinput import TextInput
# from kivy.uix.gridlayout import GridLayout
# from cProfile import run
# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# import cv2
# from matplotlib.widgets import Widget
# import mediapipe as mp
# import numpy as np
# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
# from kivy.uix.image import Image

from tkinter import Frame
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
import cv2
from kivy.clock import Clock


class MyApp(MDApp):

    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        self.image = Image()
        layout.add_widget(self.image)
        layout.add_widget(MDRaisedButton(
            text="CLICK ME",
            pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(None, None))
        )
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/30.0)

        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        self.image_frame = frame
        buffer = cv2.flip(frame, 0).tostring()
        texture = Texture.create(
            size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture


if __name__ == '__main__':
    MyApp().run()
