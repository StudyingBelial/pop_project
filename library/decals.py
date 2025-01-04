from stockitem import StockItem
from enum import Enum

class Decal(StockItem):
    
    class DecalType(Enum):
        UNDEFINED = auto()
        PAINT = auto()
        STICKER = auto()
        TINT = auto()

    def __init__(
        self,
        id="N/A",
        name="",
        quantity=0,
        price=0.0,
        description="",
        item_type="Decal",
        brand="N/A",
        vat=17.5,
        decal_type=DecalType.UNDEFINED,
        decal_size=ItemSize.UNDEFINED,
        warrenty_type = Warranty.Type.NONE,
        warrenty_duration = Warranty.Duration.NONE
    ):
        super().__init__(id, name, quantity, price, description, item_type, brand, vat)
        self.constructor_validation(decal_type, decal_size)
        self.decal_type = decal_type
        self.decal_size = decal_size

    def constructor_validation(self, decal_type, decal_size):
        type_checker(decal_type, self.DecalType, "DecalType")
        type_checker(decal_size, ItemSize, "ItemSize")

    def set_decal_type(self, decal_type):
        type_checker(decal_type, self.DecalType, "DecalType")
        self.decal_type = decal_type

    def set_decal_size(self, decal_size):
        type_checker(decal_size, ItemSize, "ItemSize")
        self.decal_size = decal_size