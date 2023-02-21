from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager






class WindowManger(ScreenManager):
    pass


class MainWindow(Screen):
    def calculate(self):
        pass


kv = Builder.load_file("window.kv")


class Application(App):
    def build(self):
        return kv


if __name__ == "__main__":
    Application().run()
