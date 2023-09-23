from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.clock import Clock as c
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader

Builder.load_file('5.kv')

class Style(AnchorLayout):

    lbl=ObjectProperty()
    sound=SoundLoader.load('ms1.mp3')

    # def __init__(self,**kwargs):
    #     super(Style,self).__init__(**kwargs)

    def start(self):
        self.tstt=c.get_time()
        self.lbl.text='00 : 000'

    def stop(self):
        self.tstp=c.get_time()
        t=str(self.tstp-self.tstt)
        tt=t.split('.')
        s_1000=tt[1][:3]
        s=tt[0]

        self.lbl.text=s+' : '+s_1000

    def chap(self):
        print('\n... touch ...\n')

    def play(self):
        self.sound.play()
    def stopp(self):
        self.sound.stop()

class MyApp(App):

    def build(self):

        return Style()

MyApp().run()

