from stockitem import StockItem
from enum import Enum, auto

class Battery(StockItem):
    
    class BatteryType(Enum):
        UNDEFINED = auto()
        LEAD_ACID = auto()
        LITHIUM_ION = auto()
        GEL_CELL = auto()

    def __init__(
        self,
        id = "N/A",
        name = "",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "Battery", 
        brand = "N/A", 
        vat = 17.5,
        battery_type = BatteryType.UNDEFINED,
        battery_size = ItemSize.UNDEFINED,
        warrenty_type = Warranty.Type.NONE,
        warrenty_duration = Warranty.Duration.NONE
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)
        self.constructor_validation(battery_type, battery_size)
        self.battery_type = battery_type
        self.battery_size = battery_size

    def constructor_validation(self, battery_type, battery_size):
        type_checker(battery_type, self.BatteryType, "BatteryType")
        type_checker(battery_size, ItemSize, "ItemSize")
        
    def set_battery_type(self, battery_type):
        type_checker(battery_type, self.BatteryType, "BatteryType")
        self.battery_type = battery_type

    def set_battery_size(self, battery_size):
        type_checker(battery_size, ItemSize, "ItemSize")
        self.battery_size = battery_size
