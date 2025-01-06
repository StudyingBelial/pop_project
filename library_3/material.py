

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