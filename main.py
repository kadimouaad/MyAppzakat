from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from core import GoldZakat, ZakatConfig, Unit, GoldType, AgricultureType, AgricultureZakat, SilverZakat, LiquidityZakat
from window import Application

Window.size = (339, 600)


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    Toggle_name = ""

    def on_state_1(self, toggle):
        if toggle.state == "down":
            self.Toggle_name = "Gold"
        else:
            self.Toggle_name = ""

    def on_state_2(self, toggle):
        if toggle.state == "down":
            self.Toggle_name = "Arg"
        else:
            self.Toggle_name = ""

    def on_state_3(self, toggle):
        if toggle.state == "down":
            self.Toggle_name = "Cattle"
        else:
            self.Toggle_name = ""

    def on_state_4(self, toggle):
        if toggle.state == "down":
            self.Toggle_name = "silver"
        else:
            self.Toggle_name = ""

    def on_state_5(self, toggle):
        if toggle.state == "down":
            self.Toggle_name = "liq"
        else:
            self.Toggle_name = ""

    def ToggleGoldType(self):  # Toggle for gold type
        pass

    def calculator(self):

        if self.Toggle_name == "Arg":
            agr = AgricultureZakat(int(self.ids.my_text_input.text), AgricultureType.NATURALLY_IRRIGATED)
            self.ids.my_result_label.text = str(agr.calculate())
        elif self.Toggle_name == "Gold":
            gold = GoldZakat(int(self.ids.my_text_input.text), GoldType.KIRAT_18)
            self.ids.my_result_label.text = str(gold.calculate())
        elif self.Toggle_name == "Silver":
            silver = SilverZakat(int(self.ids.my_text_input.text))
            self.ids.my_result_label.text = silver.calculate()
        elif self.Toggle_name == "liq":
            Liq = LiquidityZakat(int(self.ids.my_text_input.text))
            self.ids.my_result_label.text = Liq.calculate()


kv = Builder.load_file("zakat.kv")


class Application(App):
    def build(self):
        return kv


if __name__ == "__main__":
    Application().run()
