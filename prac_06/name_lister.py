from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NameLister(App):
    def build(self):
        self.title = "Name Lister"
        self.root = Builder.load_file('name_lister.kv')
        self.list_names()
        return self.root

    def list_names(self):
        names = ["why", "are", "you", "this"]
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)


NameLister().run()
