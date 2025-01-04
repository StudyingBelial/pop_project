from stockitem import StockItem
from enum import Enum

class Tire(StockItem):

    # Enummeration Class for the types of Tires

    class TireType(Enum):
        UNDEFINED = auto()
        SUMMER = auto()
        WINTER = auto()
        ALL_SEASON = auto()
        RUN_FLAT = auto()
        FOUR_BY_FOUR = auto()

    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "Tire", 
        brand = "N/A", 
        vat = 17.5,
        item_size = ItemSize.UNDEFINED,
        warrenty_type = Warranty.Type.NONE,
        warrenty_duration = Warranty.Duration.NONE,
        tire_type = TireType.UNDEFINED
    ):
        super().__init__(self, id, name, quantity, price, description, item_type, brand, vat, item_size, warrenty_type, warrenty_duration)
        self.constructor_validation(tire_type)
        self.tire_type = tire_type

    # Function that calls the validator function for each Class Specific Variable

    def constructor_validation(self, tire_type):
        self.type_checker(tire_type, self.TireType, "Tire Type")

    # Setter Functions for the Class Specific Variables

    def set_tire_type(self, tire_type):
        self.type_checker(tire_type, self.TireType, "Tire Type")
        self.tire_type = tire_type

    def get_stock_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "description": self.description,
            "item_type": self.item_type,
            "brand": self.brand,
            "vat": self.vat,
            "item_size": self.item_size,
            "warranty_type": self.warrenty_type,
            "warranty_duration": self.warrenty_duration,
            "tire_type": self.tire_type
        }