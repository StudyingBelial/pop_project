from global_enums import ItemSize, Warranty

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
        item_size = ItemSize.UNDEFINED,
        warrenty_type = Warranty.Type.NONE,
        warrenty_duration = Warranty.Duration.NONE
    ):
        StockItem.constructor_validation(self, id, name, quantity, price, description, item_type, brand, vat, item_size, warrenty_type, warrenty_duration)
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.description = description
        self.item_type = item_type
        self.brand = brand
        self.vat = vat
        self.item_size = item_size
        self.warrenty_type = warrenty_type
        self.warrenty_duration = warrenty_duration

    def constructor_validation(self, id, name, quantity, price, description, item_type, brand, vat, item_size, warrenty_type, warrenty_duration):
        self.type_checker(id, str, 'id')
        self.type_checker(name, str, 'name')
        self.type_checker(quantity, int, 'quantity')
        self.type_checker(price, (int, float), 'price')
        self.type_checker(description, str, 'description')
        self.type_checker(item_type, str, 'item_type')
        self.type_checker(brand, str, 'brand')
        self.type_checker(vat, (int, float), 'vat')
        self.type_checker(item_size, ItemSize, 'ItemSize')
        self.type_checker(warrenty_type, Warranty.Type, 'Warranty.Type')
        self.type_checker(warrenty_duration, Warranty.Duration, 'Warranty.Duration')


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

    def set_item_size(self, item_size):
        
        self.item_size = item_size

    def set_warrenty_type(self, warrenty_type):
        self.type_checker(warrenty_type, Warranty.Type, 'Warranty.Type')
        self.warrenty_type = warrenty_type

    def set_warrenty_duration(self, warrenty_duration):
        self.type_checker(warrenty_duration, Warranty.Duration, 'Warranty.Duration')
        self.warrenty_duration = warrenty_duration

    def increase_stock(self, change_amt):
        self.type_checker(change_amt, int, 'change_amt')
        self.quantity += change_amt
    
    def decrease_stock(self, change_amt):
        self.type_checker(change_amt, int, 'change_amt')
        if change_amt <= self.quantity:
            self.quantity -= change_amt
        else:
            raise ValueError("Cannot Decrease Stock more than What is available")

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
            "warranty_duration": self.warrenty_duration
        }