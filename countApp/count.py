from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class CountView(BoxLayout):
    def __init__(self, **kwargs):
        super(CountView, self).__init__(**kwargs)

    def count_up(self):
        current_val = int(self.ids.total_count_view.text)
        self.ids.total_count_view.text = str(current_val + 1)

    def count_down(self):
        current_val = int(self.ids.total_count_view.text)
        self.ids.total_count_view.text = str(current_val - 1)


class CountApp(App):
    def build(self):
        return CountView()


if __name__ in ('__main__', '__osx__'):
    CountApp().run()
