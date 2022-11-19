"""CP1404 - Prac 08 - Miles to KM"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ Converts miles to kilometres """

    def build(self):
        """ Build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ Handle calculation - output to output_label"""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """ Handle incremental adjustment buttons - Calls calculate function to update output"""
        value = self.get_valid_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """ Get float value from text input with error checking"""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
