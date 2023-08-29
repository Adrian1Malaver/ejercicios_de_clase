from conteo import *

class hallarbin(conteo):
    def get_value(self):
        return bin(self.value)[2:]