from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
import os, sys

class HelloLabel(Label):
    pass


class HelloView(GridLayout):
    counter = 0
    def __init__(self, **kwargs):
        super(HelloView, self).__init__(**kwargs)

    def echo_text_input(self, instance):
        self.counter += 1
        self.ids.input_counter_label.text = "Input: {0}".format(self.counter)
        sys.stdout.write("\ron_press counter: {0}".format(self.counter))
        sys.stdout.flush()

    def choose_dir_path(self, instance):
        selection = instance.selection[0]

class HelloApp(App):
    def build(self):
        Config.set('kivy', 'exit_on_escape', 0)
        Config.set('graphics', 'height', 900)
        Config.set('graphics', 'width', 1200)
        return HelloView()


if __name__ in ('__main__', '__osx__'):
    HelloApp().run()

