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

class Chassis(MaterialProperty):
    def __init__(
        self,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        load_capacity = 0.0,
        max_strain = None,
        max_stress = None,
        tire_type = None,
        suspension_type = None,
        brake_type = None
    ):
        self.set_weight(weight)
        self.set_dimensions(dimensions)
        self.set_composition(composition)
        self.set_durability(durability)
        self.set_load_capacity(load_capacity)
        self.set_max_strain(max_strain)
        self.set_max_stress(max_stress)
        self.set_tire_type(tire_type)
        self.set_suspension_type(suspension_type)
        self.set_brake_type(brake_type)

    def set_load_capacity(self, load_capacity):
        self.material_type_check(load_capacity, (int, float), "load_capacity in kg")
        self.load_capacity = load_capacity

    def set_max_strain(self, max_strain):
        self.material_type_check(max_strain, (int, float, type(None)), "max_strain in numeric SI")
        self.max_strain = max_strain

    def set_max_stress(self, max_stress):
        self.material_type_check(max_stress, (int, float, type(None)), "max_stress in numeric SI")
        self.max_stress = max_stress

    def set_tire_type(self, tire_type):
        self.material_type_check(tire_type, (str, type(None)), "tire_type")
        self.tire_type = tire_type

    def set_suspension_type(self, suspension_type):
        self.material_type_check(suspension_type, (str, type(None)), "suspension_type")
        self.suspension_type = suspension_type

    def set_brake_type(self, brake_type):
            self.material_type_check(brake_type, (str, type(None)), "brake_type")
            self.brake_type = brake_type

    def get_load_capacity(self):
        return getattr(self, "load_capacity", None)

    def get_max_strain(self):
        return getattr(self, "max_strain", None)

    def get_max_stress(self):
        return getattr(self, "max_stress", None)

    def get_tire_type(self):
        return getattr(self, "tire_type", None)

    def get_suspension_type(self):
        return getattr(self, "suspension_type", None)

    def get_brake_type(self):
        return getattr(self, "brake_type", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "load_capacity": self.get_load_capacity(),
            "max_strain": self.get_max_strain(),
            "max_stress": self.get_max_stress(),
            "tire_type": self.get_tire_type(),
            "suspension_type": self.get_suspension_type(),
            "brake_type": self.get_brake_type()
        }
        base.update(added)
        return base

class Tire:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "tire", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        load_capacity = 0.0,
        max_stress = 0.0,
        tire_type = "undefined"
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = Chassis(weight, dimensions, composition, durability, load_capacity, max_stress, tire_type)

    def get_tire_stock(self):
        return self.part_stock.get_stock_details()

    def get_tire_property(self):
        return self.part_property.get_material_property()

    def get_complete_tire_details(self):
        stock = self.get_tire_stock()
        quality = self.get_tire_property()
        stock.update(quality)
        return stock

class Brake:
    class Brake:
        def __init__(
            self,
            id = "N/A",
            name = "Unknown Stock Name",
            quantity = 0, 
            price = 0.0, 
            description = "", 
            item_type = "brake", 
            brand = "N/A", 
            vat = 17.5,
            weight = 0.0,
            dimensions = (0.0,0.0,0.0),
            composition = {"undefined": 0},
            durability = "undefined",
            max_stress = 0.0,
            brake_type = "undefined"
        ):
            self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
            self.part_property = Chassis(weight, dimensions, composition, durability, max_stress, brake_type)

        def get_brake_stock(self):
            return self.part_stock.get_stock_details()

        def get_brake_property(self):
            return self.part_property.get_material_property()

        def get_complete_brake_details(self):
            stock = self.get_brake_stock()
            quality = self.get_brake_property()
            stock.update(quality)
            return stock

class Suspension:
    class Suspension:
        def __init__(
            self,
            id = "N/A",
            name = "Unknown Stock Name",
            quantity = 0, 
            price = 0.0, 
            description = "", 
            item_type = "suspension", 
            brand = "N/A", 
            vat = 17.5,
            weight = 0.0,
            dimensions = (0.0,0.0,0.0),
            composition = {"undefined": 0},
            durability = "undefined",
            max_stress = 0.0,
            suspension_type = "undefined"
        ):
            self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
            self.part_property = Chassis(weight, dimensions, composition, durability, max_stress, suspension_type)

        def get_suspension_stock(self):
            return self.part_stock.get_stock_details()

        def get_suspension_property(self):
            return self.part_property.get_material_property()

        def get_complete_suspension_details(self):
            stock = self.get_suspension_stock()
            quality = self.get_suspension_property()
            stock.update(quality)
            return stock

class Detailing(MaterialProperty):
    def __init__(
        self,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        primary_color = "",
        secondary_color = None,
        finish = "",
        texture = None,
        protection_type = None
    ):
        self.set_weight(weight)
        self.set_dimensions(dimensions)
        self.set_composition(composition)
        self.set_durability(durability)
        self.set_primary_color(primary_color)
        self.set_secondary_color(secondary_color)
        self.set_finish(finish)
        self.set_texture(texture)
        self.set_protection_type(protection_type)

    def set_primary_color(self, primary_color):
        self.material_type_check(primary_color, str, "primary_color")
        self.primary_color = primary_color

    def set_secondary_color(self, secondary_color):
        self.material_type_check(secondary_color, (str, type(None)), "secondary_color")
        self.secondary_color = secondary_color

    def set_texture(self, texture):
        self.material_type_check(texture, (str, type(None)), "texture")
        self.texture = texture

    def set_protection_type(self, protection_type):
        self.material_type_check(protection_type, (str, type(None)), "protection_type")
        self.protection_type = protection_type

    def get_primary_color(self):
        return getattr(self, "primary_color", None)

    def get_secondary_color(self):
        return getattr(self, "secondary_color", None)

    def get_finish(self):
        return getattr(self, "finish", None)

    def get_texture(self):
        return getattr(self, "texture", None)

    def get_protection_type(self):
        return getattr(self, "protection_type", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "primary_color": self.get_primary_color(),
            "secondary_color": self.get_secondary_color(),
            "finish": self.get_finish(),
            "texture": self.get_texture(),
            "protection_type": self.get_protection_type(),
        }
        base.update(added)
        return base

class Paint:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "paint", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        primary_color = "",
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = Chassis(weight, dimensions, composition, durability, primary_color)

    def get_paint_stock(self):
            return self.part_stock.get_stock_details()

    def get_paint_property(self):
        return self.part_property.get_material_property()

    def get_complete_paint_details(self):
        stock = self.get_suspension_stock()
        quality = self.get_suspension_property()
        stock.update(quality)
        return stock

class SeatAndCover:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "seatandcover", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0, 0.0, 0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        primary_color = "",
        secondary_color = "",
        finish = "",
        protection_type = "",
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = Detailing(weight, dimensions, composition, durability, primary_color, secondary_color, finish, protection_type)

    def get_seats_and_covers_stock(self):
        return self.part_stock.get_stock_details()

    def get_seats_and_covers_property(self):
        return self.part_property.get_material_property()

    def get_complete_seats_and_covers_details(self):
        stock = self.get_seats_and_covers_stock()
        quality = self.get_seats_and_covers_property()
        stock.update(quality)
        return stock

class DecalAndTint:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "decalandtint", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0, 0.0, 0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        primary_color = "",
        secondary_color = "",
        finish = "",
        protection_type = "",
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = Detailing(weight, dimensions, composition, durability, primary_color, secondary_color, finish, protection_type)

    def get_decal_and_tint_stock(self):
        return self.part_stock.get_stock_details()

    def get_decal_and_tint_property(self):
        return self.part_property.get_material_property()

    def get_complete_decal_and_tint_details(self):
        stock = self.get_decal_and_tint_stock()
        quality = self.get_decal_and_tint_property()
        stock.update(quality)
        return stock

class ElectricalSystem(MaterialProperty):
    def __init__(
        self, 
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        avg_lifespan = 0,
        temperature_rating = None,
        battery_type = None,
        display_type = None
    ):
        self.set_weight(weight)
        self.set_dimensions(dimensions)
        self.set_composition(composition)
        self.set_durability(durability)
        self.set_voltage(voltage)
        self.set_amperage(amperage)
        self.set_power_inout(power_inout)
        self.set_temperature_rating(temperature_rating)
        self.set_avg_lifespan(avg_lifespan)
        self.set_battery_type(battery_type)
        self.set_display_type(display_type)
        self.get_power_efficiency()

    def set_voltage(self, voltage):
        self.material_type_check(voltage, (int, float), "voltage in V")
        self.voltage = voltage

    def set_amperage(self, amperage):
        self.material_type_check(amperage, (int, float), "amperage in A")
        self.amperage = amperage

    def set_power_inout(self, power_inout):
        self.material_type_check(power_inout, (int, float), "power_inout in W")
        self.power_inout = power_inout

    def set_temperature_rating(self, temperature_rating):
        self.material_type_check(temperature_rating, (int, float, type(None)), "temperature_rating in C")
        self.temperature_rating = temperature_rating

    def set_avg_lifespan(self, avg_lifespan):
        self.material_type_check(avg_lifespan, int, "avg_lifespan in hours")
        self.avg_lifespan = avg_lifespan

    def set_battery_type(self, battery_type):
        self.material_type_check(battery_type, (str, type(None)), "battery_type")
        self.battery_type = battery_type

    def set_display_type(self, display_type):
        self.material_type_check(display_type, (str, type(None)), "display_type")
        self.display_type = display_type

    def get_voltage(self):
        return getattr(self, "voltage", None)

    def get_amperage(self):
        return getattr(self, "amperage", None)

    def get_power_inout(self):
        return getattr(self, "power_inout", None)

    def get_temperature_rating(self):
        return getattr(self, "temperature_rating", None)

    def get_avg_lifespan(self):
        return getattr(self, "avg_lifespan", None)

    def get_battery_type(self):
        return getattr(self, "battery_type", None)

    def get_display_type(self):
        return getattr(self, "display_type", None)

    def get_power_efficiency(self):
        if (self.power_inout != 0 and self.voltage != 0 and self.amperage != 0):
            self.power_efficiency = (self.power_inout / (self.voltage * self.amperage)) * 100
            return self.power_efficiency
        else:
            return 0

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "voltage": self.get_voltage(),
            "amperage": self.get_amperage(),
            "power_inout": self.get_power_inout(),
            "temperature_rating": self.get_temperature_rating(),
            "avg_lifespan": self.get_avg_lifespan(),
            "power_efficiency": self.get_power_efficiency(),
            "battery_type": self.battery_type,
            "display_type": self.display_type
        }
        base.update(added)
        return base

class Battery:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "battery", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        avg_lifespan = 0,
        temperature_rating = 50.0,
        battery_type = ""
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = Chassis(weight, dimensions, composition, durability, voltage, amperage, power_inout, avg_lifespan, temperature_rating, battery_type)

    def get_battery_stock(self):
        return self.part_stock.get_stock_details()

    def get_battery_property(self):
        return self.part_property.get_material_property()

    def get_complete_battery_details(self):
        stock = self.get_battery_stock()
        quality = self.get_battery_property()
        stock.update(quality)
        return stock

class WiringHarness:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "wiringharness", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        avg_lifespan = 0,
        temperature_rating = 50.0
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = ElectricalSystem(weight, dimensions, composition, durability, voltage, amperage, power_inout, avg_lifespan, temperature_rating)

    def get_wiring_harness_stock(self):
        return self.part_stock.get_stock_details()

    def get_wiring_harness_property(self):
        return self.part_property.get_material_property()

    def get_complete_wiring_harness_details(self):
        stock = self.get_wiring_harness_stock()
        quality = self.get_wiring_harness_property()
        stock.update(quality)
        return stock

class Infotainment:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "infotainment", 
        brand = "N/A", 
        vat = 17.5,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        avg_lifespan = 0,
        temperature_rating = 50.0,
        display_type = ""
    ):
        self.part_stock = StockItem(id, name, quantity, price, description, item_type, brand, vat)
        self.part_property = ElectricalSystem(weight, dimensions, composition, durability, voltage, amperage, power_inout, avg_lifespan, temperature_rating, display_type)

    def get_infotainment_stock(self):
        return self.part_stock.get_stock_details()

    def get_infotainment_property(self):
        return self.part_property.get_material_property()

    def get_complete_infotainment_details(self):
        stock = self.get_infotainment_stock()
        quality = self.get_infotainment_property()
        stock.update(quality)
        return stock