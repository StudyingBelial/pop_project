class StockItem:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "", 
        brand = "N/A", 
        vat = 17.5,
    ):
        self.set_id(id)
        self.set_name(name)
        self.set_quantity(quantity)
        self.set_price(price)
        self.set_description(description)
        self.set_item_type(item_type)
        self.set_brand(brand)
        self.set_vat(vat)

    def type_checker(self, variable, types, variable_name):
        if not isinstance(variable, types):
            raise TypeError(f"{variable_name} must be of type {types}")

    def set_id(self, id):
        self.type_checker(id, str, 'id')
        self.id = id

    def set_name(self, name):
        self.type_checker(name, str, 'name')
        self.name = name

    def set_quantity(self, quantity):
        self.type_checker(quantity, int, 'quantity')
        self.quantity = quantity

    def set_price(self, price):
        self.type_checker(price, (int, float), 'price')
        self.price = price

    def set_description(self, description):
        self.type_checker(description, str, 'description')
        self.description = description

    def set_item_type(self, item_type):
        self.type_checker(item_type, str, 'item_type')
        self.item_type = item_type

    def set_brand(self, brand):
        self.type_checker(brand, str, 'brand')
        self.brand = brand

    def set_vat(self, vat):
        self.type_checker(vat, (int, float), 'vat')
        self.vat = vat

    def increase_stock(self, change_amt):
        self.type_checker(change_amt, int, 'change_amt')
        self.quantity += change_amt
    
    def decrease_stock(self, change_amt):
        self.type_checker(change_amt, int, 'change_amt')
        if change_amt <= self.quantity:
            self.quantity -= change_amt
        else:
            raise ValueError("Cannot Decrease Stock more than What is available")

    def get_id(self):
        return getattr(self, "id", None)

    def get_name(self):
        return getattr(self, "name", None)

    def get_quantity(self):
        return getattr(self, "quantity", None)

    def get_price(self):
        return getattr(self, "price", None)

    def get_description(self):
        return getattr(self, "description", None)

    def get_item_type(self):
        return getattr(self, "item_type", None)

    def get_brand(self):
        return getattr(self, "brand", None)

    def get_vat(self):
        return getattr(self, "vat", None)

    def get_stock_details(self):
        return {
            "id": self.get_id(),
            "name": self.get_name(),
            "quantity": self.get_quantity(),
            "price": self.get_price(),
            "description": self.get_description(),
            "item_type": self.get_item_type(),
            "brand": self.get_brand(),
            "vat": self.get_vat()
        }