from material import MaterialProperty
from stockitem import StockItem

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