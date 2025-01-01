from stockitem import StockItem

class NavSys(StockItem):
    def __init__(
        self,
        name = "",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "", 
        brand = "N/A", 
        vat = 17.5
    ):
        super().__init__(name, quantity, price, description, item_type, brand, vat)
        self.name = "Navigation System"
        self.description = "GeoVision Sat Nav"

    def get_stock_details(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "description": self.description,
            "item_type": self.item_type,
            "brand": self.brand,
            "vat": self.vat
        }