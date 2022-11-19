"""CP1404 - Prac 08 - Box layout demo"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Box layout demo"""
    def build(self):
        """Initialise box"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet user by name"""
        print("greet")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clear input and output fields"""
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
