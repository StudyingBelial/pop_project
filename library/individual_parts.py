from stockitem import StockItem
from enum import Enum, auto
from global_enums import ItemSize

class NavSys(StockItem):
    def __init__(
        self,
        id = "N/A",
        name = "Navigation System",
        quantity = 0, 
        price = 0.0, 
        description = "GeoVision Sat Nav", 
        item_type = "Navigation System", 
        brand = "N/A", 
        vat = 17.5
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)
        

class Engine(StockItem):

    class EngineType(Enum):
        UNDEFINED = auto()
        PETROL = auto()
        DISEL = auto()
        ELECTRIC = auto()
        HYBRID = auto()

    def __init__(
        self,
        id = "N/A",
        name = "",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "Engine", 
        brand = "N/A", 
        vat = 17.5,
        engine_type = EngineType.UNDEFINED,
        engine_size = ItemSize.UNDEFINED
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)
        self.constructor_validation(engine_type, engine_size)
        self.engine_type = engine_type
        self.engine_size = engine_size

    def constructor_validation(self, engine_type, engine_size):
        self.type_checker(engine_type, self.EngineType, "Engine Type")
        self.type_checker(engine_size, ItemSize, "Item Size")

class Tire(StockItem):

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
        name = "",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "Tire", 
        brand = "N/A", 
        vat = 17.5,
        tire_type = TireType.UNDEFINED,
        tire_size = ItemSize.UNDEFINED
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)
        self.constructor_validation(tire_type, tire_size)

    def constructor_validation(self, tire_type, tire_size):
        self.type_checker(tire_type, self.TireType, "Tire Type")
        self.type_checker(tire_size, self.ItemSize, "Tire Size")
        

class Battery(StockItem):
    # ENUM CLASS HERE
     def __init__(
        self,
        id = "N/A",
        name = "",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "Battery", 
        brand = "N/A", 
        vat = 17.5
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)
        

class Tools(StockItem):
    # ENUM CLASS HERE
     def __init__(
        self,
        id = "N/A",
        name = "",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "", 
        brand = "N/A", 
        vat = 17.5
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)
        

class Decals(StockItem):
    # ENUM CLASS HERE
     def __init__(
        self,
        id = "N/A",
        name = "",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "", 
        brand = "N/A", 
        vat = 17.5
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)