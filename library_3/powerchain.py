# from material.py import MaterialProperty
# from stockitem import StockItem

class StockItem:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "", 
        brand = "N/A", 
        vat = 17.5,
    ):
        self.set_id(id)
        self.set_name(name)
        self.set_quantity(quantity)
        self.set_price(price)
        self.set_description(description)
        self.set_item_type(item_type)
        self.set_brand(brand)
        self.set_vat(vat)

    def type_checker(self, variable, types, variable_name):
        if not isinstance(variable, types):
            raise TypeError(f"{variable_name} must be of type {types}")

    def set_id(self, id):
        self.type_checker(id, str, 'id')
        self.id = id

    def set_name(self, name):
        self.type_checker(name, str, 'name')
        self.name = name

    def set_quantity(self, quantity):
        self.type_checker(quantity, int, 'quantity')
        self.quantity = quantity

    def set_price(self, price):
        self.type_checker(price, (int, float), 'price')
        self.price = price

    def set_description(self, description):
        self.type_checker(description, str, 'description')
        self.description = description

    def set_item_type(self, item_type):
        self.type_checker(item_type, str, 'item_type')
        self.item_type = item_type

    def set_brand(self, brand):
        self.type_checker(brand, str, 'brand')
        self.brand = brand

    def set_vat(self, vat):
        self.type_checker(vat, (int, float), 'vat')
        self.vat = vat

    def increase_stock(self, change_amt):
        self.type_checker(change_amt, int, 'change_amt')
        self.quantity += change_amt
    
    def decrease_stock(self, change_amt):
        self.type_checker(change_amt, int, 'change_amt')
        if change_amt <= self.quantity:
            self.quantity -= change_amt
        else:
            raise ValueError("Cannot Decrease Stock more than What is available")

    def get_id(self):
        return getattr(self, "id", None)

    def get_name(self):
        return getattr(self, "name", None)

    def get_quantity(self):
        return getattr(self, "quantity", None)

    def get_price(self):
        return getattr(self, "price", None)

    def get_description(self):
        return getattr(self, "description", None)

    def get_item_type(self):
        return getattr(self, "item_type", None)

    def get_brand(self):
        return getattr(self, "brand", None)

    def get_vat(self):
        return getattr(self, "vat", None)

    def get_stock_details(self):
        return {
            "id": self.get_id(),
            "name": self.get_name(),
            "quantity": self.get_quantity(),
            "price": self.get_price(),
            "description": self.get_description(),
            "item_type": self.get_item_type(),
            "brand": self.get_brand(),
            "vat": self.get_vat()
        }

class MaterialProperty:
    def __init__(self, *args, **kwargs):
        raise TypeError(f"Cannot Instantiate {self.__class__.__name__}")

    def material_type_check(self, variable, types, variable_name):
        if not isinstance(variable, types):
            raise TypeError(f"{variable_name} must be of type {types}")

    def set_weight(self, weight):
        self.material_type_check(weight, (int, float), "weight")
        if (weight <= 0):
            raise ValueError("Weight cannot be Zero or negative")
        self.weight = weight

    def set_dimensions(self, dimension_tuple):
        self.material_type_check(dimension_tuple, tuple, "dimension_tuple")
        for value in dimension_tuple:
            self.material_type_check(value, (int, float), "dimension_value")
        if (len(dimension_tuple) != 3):
            raise ValueError("{dimension_tuple} can only have 3 values")
        self.dimensions = dimension_tuple

    def set_material_composition(self, composition_dict):
        self.material_type_check(composition_dict, dict, "composition_dict")
        for key, value in composition_dict.items():
            self.material_type_check(key, str, "material_type")
            self.material_type_check(value, (int, float), "material_proportion")
        self.composition = composition_dict

    def set_durability(self, durability):
        self.material_type_check(durability, str, "durability")
        if durability not in ["high", "medium", "low", "undefined"]:
            raise ValueError("Durability must be 'high', 'medium', 'low', or 'undefined'")
        self.durability = durability

    def get_weight(self):
        return getattr(self, "weight", None)

    def get_dimensions(self):
        return getattr(self, "dimensions", None)

    def get_material_composition(self):
        return getattr(self, "composition", None)

    def get_durability(self):
        return getattr(self, "durability", None)

    def get_material_property(self):
        return {
            "weight": self.get_weight(),
            "dimensions": self.get_dimensions(),
            "composition": self.get_material_composition(),
            "durability": self.get_durability()
        }

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
        self.set_material_composition(composition)
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
        weight = 1.0,
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
        self.part_property = PowerChain(weight, dimensions, composition, durability, torque, horsepower, fuel_type, fuel_efficiency,engine_type)

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
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        torque = 0.0,
        horsepower = 0.0,
        transimission_type = "undefined"
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