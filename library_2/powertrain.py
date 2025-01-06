from stockitem import StockItem
from mixin import PowerChainMixin, WarrantyMixin

class Engine(StockItem, PowerChainMixin, WarrantyMixin):
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
        item_size = "",
        horsepower = 0,
        torque = 0,
        fuel_type = "",
        fuel_efficiency = ""
    ):
        StockItem.constructor_validation(self, id, name, quantity, price, description, item_type, brand, vat, item_size, warrenty_type, warrenty_duration)
        self.constructor_validation(self, horsepower, torque, fuel_type, fuel_efficiency)
        self.horsepower = horsepower
        self.torque = torque
        self.fuel_type = fuel_efficiency
        self.fuel_efficiency = fuel_efficiency

        def constructor_validation(self, horsepower, torque, fuel_type, fuel_efficiency):
            self.type_checker(horsepower,(int, float), "horsepower")
            self.type_checker(torque, (int, float), "torque")
            self.type_checker(fuel_type, str, "fuel_type")
            self.type_checker(fuel_efficiency, (int, float), "fuel_efficiency")

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
            "horsepower": self.horsepower,
            "torque": self.torque,
            "fuel_type": self.fuel_type,
            "fuel_efficiency": self.fuel_efficiency
        }

class Transmission(StockItem, PowerChainMixin, WarrantyMixin):
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
        item_size = "",
        fuel_type = "",
        transmission_type = ""
    ):
        StockItem.constructor_validation(self, id, name, quantity, price, description, item_type, brand, vat, item_size, warrenty_type, warrenty_duration)
        self.constructor_validation(fuel_type, transmission_type)
        self.fuel_type = fuel_type
        self.transmission_type = transmission_type

    def constructor_validation(self, fuel_type, fuel_efficiency):
        self.type_checker(fuel_type, str, "fuel_type")
        self.type_checker(transmission_type, str, "transmission_type")