class MedioTransporte:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print()

class Coche(MedioTransporte):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__("Coche", marca, modelo)
        self.num_puertas = num_puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de puertas: {self.num_puertas}")

class Bicicleta(MedioTransporte):
    def __init__(self, marca, modelo, tipo_bici):
        super().__init__("Bicicleta", marca, modelo)
        self.tipo_bici = tipo_bici

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de bicicleta: {self.tipo_bici}")

class Bus(MedioTransporte):
    def __init__(self, marca, modelo, capacidad_pasajeros):
        super().__init__("Bus", marca, modelo)
        self.capacidad_pasajeros = capacidad_pasajeros

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")

class Taxi(MedioTransporte):
    def __init__(self, marca, modelo, num_pasajeros):
        super().__init__("Taxi", marca, modelo)
        self.num_pasajeros = num_pasajeros

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de pasajeros: {self.num_pasajeros}")

# Crear instancias de diferentes medios de transporte
coche1 = Coche("Toyota", "Camry", 4)
bicicleta1 = Bicicleta("Giant", "Defy", "Montaña")
bus1 = Bus("Mercedes", "Sprinter", 20)
taxi1 = Taxi("Chevrolet", "Spark", 3)

# Mostrar información de los medios de transporte
coche1.mostrar_informacion()
bicicleta1.mostrar_informacion()
bus1.mostrar_informacion()
taxi1.mostrar_informacion()