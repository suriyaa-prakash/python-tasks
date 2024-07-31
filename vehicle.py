class Vehicle:
    def __init__(self, brand, model,color):
        self.brand = brand
        self.model = model
        self.color = color
    def display_properties(self):
        print("Brand:",(self.brand))
        print("Model:",(self.model))
        print("Color:",(self.color))
    def drive(self):
        print("Vroom! The vehicle is moving.")

class Twowheeler(Vehicle):
    def __init__(self,brand,model,color,engine_capacity):
        super().__init__(brand,model,color)
        self.engine_capacity = engine_capacity
    def display_properties(self):
        super().display_properties()
        print("Engine Capacity:",(self.engine_capacity))

class FourWheeler(Vehicle):
    def __init__(self,brand,model,color,engine_capacity):
        super().__init__(brand,model,color)
        self.engine_capacity = engine_capacity
    def display_properties(self):
        super().display_properties()
        print("Engine Capacity:",(self.engine_capacity))

twowheeler = Twowheeler("bajaj","ns200","Red",200)
twowheeler.display_properties()
twowheeler.drive()

fourwheeler = FourWheeler("Toyota","Glanza","Silver",2500)
fourwheeler.display_properties()
fourwheeler.drive()
