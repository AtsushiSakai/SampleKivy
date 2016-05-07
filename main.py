# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    __BRAND_FONT = "fonts/ipaexg"

    def build(self):
        return Label(text=u'こんにちは Kivy', font_name=self.__BRAND_FONT, font_size="64px")


TestApp().run()
