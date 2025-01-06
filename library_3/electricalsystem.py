from material import MaterialProperty
from stockitem import StockItem

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