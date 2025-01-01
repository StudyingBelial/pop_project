class StockItem:
    def __init__(
        self, 
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "", 
        brand = "N/A", 
        vat = 17.5,
        name = "Unknown Stock Name"):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.description = description
        self.item_type = item_type
        self.brand = brand
        self.vat = vat

    def set_name(self, name):
        self.name = name

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_price(self, price):
        self.price = price

    def set_description(self, description):
        self.description = description

    def set_item_type(self, item_type):
        self.item_type = item_type

    def set_brand(self, brand):
        self.brand = brand

    def set_vat(self, vat):
        self.vat = vat

    def increase_stock(self, change_amt):
        self.quantity += added_amt
    
    def decrease_stock(self, change_amt):
        if (change_amt <= self.quantity):
            self.quantity -= change_amt
        else:
            raise ValueError("Cannot Decrease Stock more than What is availaible")

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