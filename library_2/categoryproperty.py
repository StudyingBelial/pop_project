from material import MaterialProperty

class PowerChain(MaterialProperty):
    def __init__(
        self,
        torque = 0.0,
        horsepower = 0.0,
        fuel_type = None,
        fuel_efficiency = None
        ):

        self.set_torque(torque)
        self.set_horsepower(horsepower)
        self.set_fuel_type(fuel_type)
        self.set_fuel_efficiency(fuel_efficiency)

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

    def get_torque(self):
        return getattr(self, "torque", None)

    def get_horsepower(self):
        return getattr(self, "horsepower", None)

    def get_fuel_type(self):
        return getattr(self, "fuel_type", None)

    def get_fuel_efficiency(self):
        return getattr(self, "fuel_efficiency", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "torque": self.get_torque(),
            "horsepower": self.get_horsepower(),
            "fuel_type": self.get_fuel_type(),
            "fuel_efficiency": self.get_fuel_efficiency(),
        }
        base.update(added)
        return base

class Chassis(MaterialProperty):
    def __init__(
        self,
        load_capacity = 0.0,
        max_strain = None,
        max_stress = None,
    ):
        self.set_load_capacity(load_capacity)
        self.set_max_strain(max_strain)
        self.set_max_stress(max_stress)

    def set_load_capacity(self, load_capacity):
        self.material_type_check(load_capacity, (int, float), "load_capacity in kg")
        self.load_capacity = load_capacity

    def set_max_strain(self, max_strain):
        self.material_type_check(max_strain, (int, float, type(None)), "max_strain in numeric SI")
        self.max_strain = max_strain

    def set_max_stress(self, max_stress):
        self.material_type_check(max_stress, (int, float, type(None)), "max_stress in numeric SI")
        self.max_stress = max_stress

    def get_load_capacity(self):
        return getattr(self, "load_capacity", None)

    def get_max_strain(self):
        return getattr(self, "max_strain", None)

    def get_max_stress(self):
        return getattr(self, "max_stress", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "load_capacity": self.get_load_capacity(),
            "max_strain": self.get_max_strain(),
            "max_stress": self.get_max_stress(),
        }
        base.update(added)
        return base

class Detailing(MaterialProperty):
    def __init__(
        self,
        primary_color = "",
        secondary_color = "",
        finish = "",
        texture = None,
        protection_type = None
    ):
        self.set_primary_color(primary_color)
        self.set_secondary_color(secondary_color)
        self.set_finish(finish)
        self.set_texture(texture)
        self.set_protection_type(protection_type)

    def set_primary_color(self, primary_color):
        self.material_type_check(primary_color, str, "primary_color")
        self.primary_color = primary_color

    def set_secondary_color(self, secondary_color):
        self.material_type_check(secondary_color, str, "secondary_color")
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

class ElectricalSystem(MaterialProperty):
    def __init__(
        self, 
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        temperature_rating = None,
        avg_lifespan = None
    ):
        self.set_voltage(voltage)
        self.set_amperage(amperage)
        self.set_power_inout(power_inout)
        self.set_temperature_rating(temperature_rating)
        self.set_avg_lifespan(avg_lifespan)
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
        self.material_type_check(avg_lifespan, (int, float, type(None)), "avg_lifespan in hours")
        self.avg_lifespan = avg_lifespan

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
            "power_efficiency": self.get_power_efficiency()
        }
        base.update(added)
        return base