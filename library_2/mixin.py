class BaseMixin:
    # Base Constructor to prevent initalization
    def __init__(self, *args, **kwargs):
        raise TypeError(f"Cannot Instantiate {self.__class__.__name__}")

    # Function that can check the types of varaibles in the child class
    def mixin_type_check(self, variable, types, variable_name):
        if not isinstance(variable, types):
            raise TypeError(f"{variable_name} must be of type {types}")

class ChassisMixin(BaseMixin):
    def set_suspension_type(self, suspension_type):
        self.mixin_type_check(suspension_type, str, "suspension_type")
        self.suspension_type = suspension_type

    def set_material(self, material):
        self.mixin_type_check(material, str, "material")
        self.material = material

    def set_weight(self, weight):
        self.mixin_type_check(weight, (int, float), "weight")
        if (weight <= 0):
            raise ValueError("Weight cannot be Zero or negative")
        self.weight = weight

    def get_suspension_type(self):
        return getattr(self, "suspension_type", None)

    def get_material(self):
        return getattr(self, "material", None)

    def get_weight(self):
        return getattr(self, "weight", None)

class DetailingMixin:
    def set_primary_color(self, primary_color):
        self.mixin_type_check(primary_color, str, "primary_color")
        self.primary_color = primary_color

    def set_secondary_color(self, secondary_color):
        self.mixin_type_check(secondary_color, str, "secondary_color")
        self.secondary_color = secondary_color

    def set_finish_type(self, finish_type):
        self.mixin_type_check(finish_type, str, "finish_type")
        self.finish_type = finish_type

    def get_primary_color(self):
        return getattr(self, 'primary_color', None)

    def get_secondary_color(self):
        return getattr(self, 'secondary_color', None)

    def get_finish_type(self):
        return getattr(self, "finish_type", None)

class PowerChainMixin(BaseMixin):
    def set_horsepower(self, horsepower):
        self.mixin_type_check(horsepower, (int, float), "horsepower")
        if (horsepower <= 0):
            raise ValueError("Horsepower must be greater than zero")
        self.horsepower = horsepower

    def set_torque(self, torque):
        self.mixin_type_check(torque, (int, float), "torque")
        if (torque <= 0):
            raise ValueError("Torque must be greater than zero")
        self.torque = torque

    def set_fuel_type(self, fuel_type):
        self.mixin_type_check(fuel_type, str, "fuel_type")
        self.fuel_type = fuel_type

    def set_fuel_efficiency(self, fuel_efficiency):
        self.mixin_type_check(fuel_efficiency, (int, float), "fuel_efficiency")
        if (fuel_efficiency <= 0):
            raise ValueError("Fuel efficiency must be greater than zero")
        self.fuel_efficiency = fuel_efficiency

    def set_transmission_type(self, transmission_type):
        self.mixin_type_check(transmission_type, str, "transmission_type")
        self.transmission_type = transmission_type

    def get_horsepower(self):
        return getattr(self, "horsepower", None)

    def get_torque(self):
        return getattr(self, "torque", None)

    def get_fuel_type(self):
        return getattr(self, "fuel_type", None)

    def get_fuel_efficiency(self):
        return getattr(self, "fuel_efficiency", None)

    def get_transmission_type(self):
        return getattr(self, "transmission_type", None)

class ElectricalSystemMixin(BaseMixin):
    def set_battery_type(self, battery_type):
        self.mixin_type_check(battery_type, str, "battery_type")
        self.battery_type = battery_type

    def set_battery_voltage(self, battery_voltage):
        self.mixin_type_check(battery_voltage, (int, float), "battery_voltage")
        if (battery_voltage <= 0):
            raise ValueError("Battery voltage must be greater than zero")
        self.battery_voltage = battery_voltage

    def set_wiring_harness_type(self, wiring_harness_type):
        self.mixin_type_check(wiring_harness_type, str, "wiring_harness_type")
        self.wiring_harness_type = wiring_harness_type

    def set_display_type(self, display_type):
        self.mixin_type_check(display_type, str, "display_type")
        self.display_type = display_type

    def get_battery_type(self):
        return getattr(self, "battery_type", None)

    def get_battery_voltage(self):
        return getattr(self, "battery_voltage", None)

    def get_wiring_harness_type(self):
        return getattr(self, "wiring_harness_type", None)

    def get_display_type(self):
        return getattr(self, "display_type", None)

class WarrantyMixin(BaseMixin):
    def set_warranty_type(self, warranty_type):
        self.mixin_type_check(warranty_type, str, "warranty_type")
        self.warranty_type = warranty_type

    def set_warranty_duration(self, warranty_duration):
        self.mixin_type_check(warranty_duration, (int, float), "warranty_duration")
        if (warranty_duration <= 0):
            raise ValueError("Warranty duration must be greater than zero")
        self.warranty_duration = warranty_duration

    def get_warranty_type(self):
        return getattr(self, "warranty_type", None)

    def get_warranty_duration(self):
        return getattr(self, "warranty_duration", None)