from kivy.app import App
from kivy.lang import Builder


class MilesToKilometre(App):
    def build(self):
        self.title = "Miles To Kilometre"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_up_key(self, value):
        result = value + 1
        self.root.ids.display_label.text = str(result)

    def handle_down_key(self, value):
        result = value - 1
        self.root.ids.display_label.text = str(result)

MilesToKilometre().run()