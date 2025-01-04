from stockitem import StockItem
from enum import Enum

class Tool(StockItem):

    class ToolType(Enum):
        UNDEFINED = auto()
        HAND_TOOL = auto()
        POWER_TOOL = auto()
        MEASURING_TOOL = auto()
    
    def __init__(
        self,
        id = "N/A",
        name = "",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "Tool", 
        brand = "N/A", 
        vat = 17.5,
        tool_type = ToolType.UNDEFINED,
        tool_size = ItemSize.UNDEFINED,
        warrenty_type = Warranty.Type.NONE,
        warrenty_duration = Warranty.Duration.NONE
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)
        self.constructor_validation(tool_type, tool_size)
        self.tool_type = tool_type
        self.tool_size = tool_size

        def constructor_validation(self, tool_type, tool_size):
            type_checker(tool_type, self.ToolType, "ToolType")
            type_checker(tool_size, ItemSize, "ItemSize")
        
        def set_tool_type(self, tool_type):
            type_checker(tool_type, self.ToolType, "ToolType")
            self.tool_type = tool_type

        def set_tool_size(self, tool_size):
            type_checker(tool_size, ItemSize, "ItemSize")
            self.tool_size = tool_size