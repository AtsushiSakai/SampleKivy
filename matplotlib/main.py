from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
import numpy as np
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
# from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas, NavigationToolbar2Kivy
import matplotlib.pyplot as pl
import sys, os

class TitleLabel(Label):
    pass

class GraphView(BoxLayout):
    def __init__(self, **kwargs):
        super(GraphView, self).__init__(**kwargs)
        self.add_widget(self.graph_plot_sample())

    def graph_plot_sample(self):
        self.fig, ax = pl.subplots()
        x = np.linspace(-np.pi, np.pi)
        y = np.sin(x)
        ax.set_xlabel("X label")
        ax.set_ylabel("Y label")
        pl.title("TITLE")
        pl.axis('equal')
        ax.plot(x, y)
        return self.fig.canvas

    def graph_save(self, instance):
        print "graph save!"
        pl.savefig("hello.pdf")

class GraphApp(App):

    def build(self):
        height = 300
        Config.set('graphics', 'height', height)
        Config.set('graphics', 'width', height * 2)
        return GraphView()

if __name__ == '__main__':
    GraphApp().run()