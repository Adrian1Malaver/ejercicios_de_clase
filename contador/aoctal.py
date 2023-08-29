from conteo import *

class hallaroct(conteo):
    def get_value(self):
        return oct(self.value)[2:]
