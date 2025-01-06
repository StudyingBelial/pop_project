from material import MaterialProperty
from stockitem import StockItem

class PowerChain(MaterialProperty):
    def __init__(
        self,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        torque = 0.0,
        horsepower = 0.0,
        fuel_type = None,
        fuel_efficiency = None,
        engine_type = None,
        transimission_type = None
        ):
        self.set_weight(weight)
        self.set_dimensions(dimensions)
        self.set_composition(composition)
        self.set_durability(durability)
        self.set_torque(torque)
        self.set_horsepower(horsepower)
        self.set_fuel_type(fuel_type)
        self.set_fuel_efficiency(fuel_efficiency)
        self.set_engine_type(engine_type)
        self.set_transimission_type(transimission_type)

    def set_torque(self, torque):
        self.material_type_check(torque, (int, float), "torque in Nm")
        self.torque = torque

    def set_horsepower(self, horsepower):
        self.material_type_check(horsepower, (int, float), "horsepower in HP")
        self.horsepower = horsepower

    def set_fuel_type(self, fuel_type):
        self.material_type_check(fuel_type, (str, type(None)), "fuel_type")
        self.fuel_type = fuel_type

    def set_fuel_efficiency(self, fuel_efficiency):
        self.material_type_check(fuel_efficiency, (int, float, type(None)), "fuel_efficiency in kWh")
        self.fuel_efficiency = fuel_efficiency

    def set_engine_type(self, engine_type):
        self.material_type_check(engine_type, (str, type(None)), "engine_type")
        self.engine_type = engine_type

    def set_transimission_type(self, transimission_type):
        self.material_type_check(transimission_type, (str, type(None)), "transimission_type")
        self.transimission_type = transimission_type

    def get_torque(self):
        return getattr(self, "torque", None)

    def get_horsepower(self):
        return getattr(self, "horsepower", None)

    def get_fuel_type(self):
        return getattr(self, "fuel_type", None)

    def get_fuel_efficiency(self):
        return getattr(self, "fuel_efficiency", None)

    def get_engine_type(self):
        return getattr(self, "engine_type", None)

    def get_transimission_type(self):
        return getattr(self, "transimission_type", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "torque": self.get_torque(),
            "horsepower": self.get_horsepower(),
            "fuel_type": self.get_fuel_type(),
            "fuel_efficiency": self.get_fuel_efficiency(),
            "engine_type": self.get_engine_type(),
            "transimission_type": self.get_transimission_type()
        }
        base.update(added)
        return base

class Engine:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "engine", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        torque = 0.0,
        horsepower = 0.0,
        fuel_type = "petrol",
        fuel_efficiency = 0.0,
        engine_type = "undefined"
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = PowerChain(weight, dimensions, composition, durability, torque, horsepower, fuel_type, engine_type)

    def get_engine_stock(self):
        return self.part_stock.get_stock_details()

    def get_engine_property(self):
        return self.part_property.get_material_property()

    def get_complete_engine_details(self):
        stock = self.get_engine_stock()
        quality = self.get_engine_property()
        stock.update(quality)
        return stock

class Transmission:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "transmission", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        torque = 0.0,
        horsepower = 0.0,
        transimission_type = undefined
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = PowerChain(weight, dimensions, composition, durability, torque, horsepower, transimission_type)

    def get_transmission_stock(self):
        return self.part_stock.get_stock_details()

    def get_transmission_property(self):
        return self.part_property.get_material_property()

    def get_complete_transmission_details(self):
        stock = self.get_transmission_stock()
        quality = self.get_transmission_property()
        stock.update(quality)
        return stock