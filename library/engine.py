from stockitem import StockItem
from enum import Enum, auto
from global_enums import ItemSize, Warranty

class Engine(StockItem):

    # Ennumeration class for the types of Engines

    class EngineType(Enum):
        UNDEFINED = auto()
        PETROL = auto()
        DISEL = auto()
        ELECTRIC = auto()
        HYBRID = auto()

    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "Engine", 
        brand = "N/A", 
        vat = 17.5,
        item_size = ItemSize.UNDEFINED,
        warrenty_type = Warranty.Type.NONE,
        warrenty_duration = Warranty.Duration.NONE,
        engine_type = EngineType.UNDEFINED
    ):
        super().__init__(self, id, name, quantity, price, description, item_type, brand, vat, item_size, warrenty_type, warrenty_duration)
        self.constructor_validation(engine_type)
        self.engine_type = engine_type

    # Function that calls the validator function for each Class Specific Variable

    def constructor_validation(self, engine_type):
        self.type_checker(engine_type, self.EngineType, "Engine Type")

    # Setter Functions for the Class Specific Variables

    def set_engine_type(self, engine_type):
        self.type_checker(engine_type, self.EngineType, "Engine Type")
        self.engine_type = engine_type

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
            "engine_type": self.engine_type
        }