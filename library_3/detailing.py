from material import MaterialProperty
from stockitem import StockItem

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