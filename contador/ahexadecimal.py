from conteo import *

class hallarhex(conteo):
    def get_value(self):
        return hex(self.value)[2:]
