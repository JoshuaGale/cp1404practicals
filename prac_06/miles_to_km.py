from kivy.app import App
from kivy.lang import Builder


class MilesToKilometre(App):
    def build(self):
        self.title = "Miles To Kilometre"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self, increment):
        result = self.get_validated_miles() + increment
        self.root.ids.input_miles.text = str(result)

    def handle_miles_to_km(self):
        result = self.get_validated_miles() * 1.609344
        self.root.ids.display_label.text = "{:.3f}".format(result)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKilometre().run()
