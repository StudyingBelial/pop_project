import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import pandas as pd

class Visualizers:
    def __init__(
        self, 
        file_path = ""
    ):
        self.file_path = file_path
        self.__df__ = self.__df_creator__(file_path)

    def __df_creator__(self, file_path):
        try:
            data_frame = pd.read_csv(file_path, index_col="id")
            return data_frame
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return render_template("server_crash.html")
        except Exception as e:
            print(f"An error occurred: {e}")
            return render_template("server_crash.html")
        finally:
            print(f"{file_path} has been passed")

    def sales_over_time(self):
        df = self.__df__

        # converting the stored format into valid and usuable time
        df["time_stamp"] = pd.to_datetime(df["time_stamp"])
        #extracting individual dates: y-m-d
        df["date"] = df["time_stamp"].dt.date
        # grouping data by the individual days
        group = df.groupby("date")
        #extracting the total sales of each day
        daily_sales = group["item_total"].sum()

        # plotting the figure
        plt.figure(figsize=(12, 6))
        plt.plot(daily_sales.index, daily_sales.values, marker='o', color='blue')
        
        # adding labels and title
        plt.xlabel("Date")
        plt.ylabel("Total Sales In Revenue")
        plt.title("Revenue History")

        # proper formatting
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout() # stops overlapping values and keys

        # saving to path
        plt.savefig(".\\app_\\static\\visuals\\SaleOverTime.png", dpi =300)#file path

    def sale_per_transaction(self):
        df = self.__df__

        # group df by item_type
        group = df.groupby("item_type")
        # extract item_total from each group
        item_total_group = group["item_total"]
        # Calculates the sum item_total of each group
        sales = item_total_group.sum()

        # plotting the figure
        plt.figure(figsize=(12, 6))
        sales.plot(kind="bar", color="skyblue")

        # adding labels and title
        plt.xlabel("Item Type")
        plt.ylabel("Total Sales")
        plt.title("Sales per tranasaction per Item Type")

        # proper formatting
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout() # stops overlapping values and keys

        # saving to path
        plt.savefig(".\\app_\\static\\visuals\\SalePerTransaction.png", dpi =300)#file path

    def quantity_sold_overtime(self):
        df = self.__df__

        # converting the stored format into valid and usuable time
        df["time_stamp"] = pd.to_datetime(df["time_stamp"])
        # adding a new col to the df with dates: y-m-d
        df["date"] = df["time_stamp"].dt.date

        #group df of quantity and date
        group = df.groupby("date")["quantity"]
        #calculating the sum
        quantity = group.sum()

        #plotting the figure
        plt.figure(figsize=(12, 6))
        quantity.plot(kind="line", marker='o',color="skyblue", linewidth=2)

        #adding the labels and title
        plt.xlabel("Date")
        plt.ylabel("Quantity Sold")
        plt.title("Quantity Sold Over Time by Item Type")

        #proper formatting
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()# stops overlapping values and keys
        # saving to path
        plt.savefig(".\\app_\\static\\visuals\\QuantityOverTime.png", dpi =300)#file path

    def revenue_by_type(self):
        df = self.__df__

        # grouping by item_type
        group = df.groupby("item_type")
        # summing up the revenue by item_type
        revenue = group["item_total"].sum()

        #plotting the figure
        plt.figure(figsize=(10,10))
        revenue.plot(kind="pie", legend=True, autopct="%1.1f%%", cmap="tab20")
        plt.legend(title="Item Type", loc="lower left")
        plt.tight_layout()# stops overlapping values and keys
        #saving to path
        plt.savefig(".\\app_\\static\\visuals\\RevenueType.png", dpi =300)#file path

class StockItem:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "Unknown Stock Description", 
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

    def __type_checker__(self, variable, types, variable_name):
        if not isinstance(variable, types):
            raise TypeError(f"{variable_name} must be of type {types}")

    def set_id(self, id):
        self.__type_checker__(id, str, 'id')
        self.__id = id

    def set_name(self, name):
        self.__type_checker__(name, str, 'name')
        self.__name = name

    def set_quantity(self, quantity):
        self.__type_checker__(quantity, int, 'quantity')
        self.__quantity = quantity

    def set_price(self, price):
        self.__type_checker__(price, (int, float), 'price')
        self.__price = price

    def set_description(self, description):
        self.__type_checker__(description, str, 'description')
        self.__description = description

    def set_item_type(self, item_type):
        self.__type_checker__(item_type, str, 'item_type')
        self.__item_type = item_type

    def set_brand(self, brand):
        self.__type_checker__(brand, str, 'brand')
        self.__brand = brand

    def set_vat(self, vat):
        self.__type_checker__(vat, (int, float), 'vat')
        self.__vat = vat

    def increase_stock(self, change_amt):
        self.__type_checker__(change_amt, int, 'change_amt')
        self.__quantity += change_amt
    
    def decrease_stock(self, change_amt):
        self.__type_checker__(change_amt, int, 'change_amt')
        if change_amt <= self.__quantity:
            self.__quantity -= change_amt
        else:
            raise ValueError("Cannot Decrease Stock more than What is available")

    def get_id(self):
        return getattr(self, "_StockItem__id", None)

    def get_name(self):
        return getattr(self, "_StockItem__name", None)

    def get_quantity(self):
        return getattr(self, "_StockItem__quantity", None)

    def get_price(self):
        return getattr(self, "_StockItem__price", None)

    def get_description(self):
        return getattr(self, "_StockItem__description", None)

    def get_item_type(self):
        return getattr(self, "_StockItem__item_type", None)

    def get_brand(self):
        return getattr(self, "_StockItem__brand", None)

    def get_vat(self):
        return getattr(self, "_StockItem__vat", None)

    def __str__(self):
        return (
            f"""
            ID: {self.get_id()}
            Name: {self.get_name()}
            Quantity: {self.get_quantity()}
            Price: {self.get_price()}
            Description: {self.get_description()}
            Item Type: {self.get_item_type()}
            Brand: {self.get_brand()}
            VAT: {self.get_vat()}
            """
        )

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

class MaterialProperty:
    def __init__(self, *args, **kwargs):
        raise TypeError(f"Cannot Instantiate {self.__class__.__name__}")

    def __material_type_check__(self, variable, types, variable_name):
        if not isinstance(variable, types):
            raise TypeError(f"{variable_name} must be of type {types}")

    def set_weight(self, weight):
        self.__material_type_check__(weight, (int, float), "weight")
        if (weight <= 0):
            raise ValueError("Weight cannot be Zero or negative")
        self.__weight = weight

    def set_dimensions(self, dimension_tuple):
        self.__material_type_check__(dimension_tuple, tuple, "dimension_tuple")
        for value in dimension_tuple:
            self.__material_type_check__(value, (int, float), "dimension_value")
        if (len(dimension_tuple) != 3):
            raise ValueError("{dimension_tuple} can only have 3 values")
        self.__dimensions = dimension_tuple

    def set_material_composition(self, composition_dict):
        self.__material_type_check__(composition_dict, dict, "composition_dict")
        for key, value in composition_dict.items():
            self.__material_type_check__(key, str, "material_type")
            self.__material_type_check__(value, (int, float), "material_proportion")
        self.__composition = composition_dict

    def set_durability(self, durability):
        self.__material_type_check__(durability, str, "durability")
        if durability not in ["high", "medium", "low", "undefined"]:
            raise ValueError("Durability must be 'high', 'medium', 'low', or 'undefined'")
        self.__durability = durability

    def get_weight(self):
        return getattr(self, "_MaterialProperty__weight", None)

    def get_dimensions(self):
        return getattr(self, "_MaterialProperty__dimensions", None)

    def get_material_composition(self):
        return getattr(self, "_MaterialProperty__composition", None)

    def get_durability(self):
        return getattr(self, "_MaterialProperty__durability", None)

    def get_material_property(self):
        return {
            "weight": self.get_weight(),
            "dimensions": self.get_dimensions(),
            "composition": self.get_material_composition(),
            "durability": self.get_durability()
        }

class PowerChain(MaterialProperty):
    def __init__(
        self,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        torque = 0.0,
        horsepower = 0.0,
        fuel_type = None,
        fuel_efficiency = None,
        engine_type = None,
        transmission_type = None
        ):
        self.set_weight(weight)
        self.set_dimensions(dimensions)
        self.set_material_composition(composition)
        self.set_durability(durability)
        self.set_torque(torque)
        self.set_horsepower(horsepower)
        self.set_fuel_type(fuel_type)
        self.set_fuel_efficiency(fuel_efficiency)
        self.set_engine_type(engine_type)
        self.set_transmission_type(transmission_type)

    def set_torque(self, torque):
        self.__material_type_check__(torque, (int, float, str), "torque in Nm")
        self.__torque = torque

    def set_horsepower(self, horsepower):
        self.__material_type_check__(horsepower, (int, float, str), "horsepower in HP")
        self.__horsepower = horsepower

    def set_fuel_type(self, fuel_type):
        self.__material_type_check__(fuel_type, (str, type(None)), "fuel_type")
        self.__fuel_type = fuel_type

    def set_fuel_efficiency(self, fuel_efficiency):
        self.__material_type_check__(fuel_efficiency, (str, int, float, type(None)), "fuel_efficiency in kWh")
        self.__fuel_efficiency = fuel_efficiency

    def set_engine_type(self, engine_type):
        self.__material_type_check__(engine_type, (str, type(None)), "engine_type")
        self.__engine_type = engine_type

    def set_transmission_type(self, transmission_type):
        self.__material_type_check__(transmission_type, (str, type(None)), "transmission_type")
        self.__transmission_type = transmission_type

    def get_torque(self):
        return getattr(self, "_PowerChain__torque", None)

    def get_horsepower(self):
        return getattr(self, "_PowerChain__horsepower", None)

    def get_fuel_type(self):
        return getattr(self, "_PowerChain__fuel_type", None)

    def get_fuel_efficiency(self):
        return getattr(self, "_PowerChain__fuel_efficiency", None)

    def get_engine_type(self):
        return getattr(self, "_PowerChain__engine_type", None)

    def get_transmission_type(self):
        return getattr(self, "_PowerChain__transmission_type", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "torque": self.get_torque(),
            "horsepower": self.get_horsepower(),
            "fuel_type": self.get_fuel_type(),
            "fuel_efficiency": self.get_fuel_efficiency(),
            "engine_type": self.get_engine_type(),
            "transmission_type": self.get_transmission_type()
        }
        base.update(added)
        return base

class Engine:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "engine", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        torque = 0.0,
        horsepower = 0.0,
        fuel_type = "petrol",
        fuel_efficiency = 0.0,
        engine_type = "undefined"
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = PowerChain(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            torque=torque, 
            horsepower=horsepower, 
            fuel_type=fuel_type, 
            fuel_efficiency=fuel_efficiency,
            engine_type=engine_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Torque: {self.part_property.get_torque()}
            Horsepower: {self.part_property.get_horsepower()}
            Fuel Type: {self.part_property.get_fuel_type()}
            Fuel Efficiency: {self.part_property.get_fuel_efficiency()}
            Engine Type: {self.part_property.get_engine_type()}
            Transmission Type: {self.part_property.get_transmission_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class Transmission:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "transmission", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        torque = 0.0,
        horsepower = 0.0,
        transmission_type = "undefined"
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = PowerChain(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            torque=torque, 
            horsepower=horsepower, 
            transmission_type=transmission_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Torque: {self.part_property.get_torque()}
            Horsepower: {self.part_property.get_horsepower()}
            Transmission Type: {self.part_property.get_transmission_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class Chassis(MaterialProperty):
    def __init__(
        self,
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        load_capacity = 0.0,
        max_strain = None,
        max_stress = None,
        tire_type = None,
        suspension_type = None,
        brake_type = None
    ):
        self.set_weight(weight)
        self.set_dimensions(dimensions)
        self.set_material_composition(composition)
        self.set_durability(durability)
        self.set_load_capacity(load_capacity)
        self.set_max_strain(max_strain)
        self.set_max_stress(max_stress)
        self.set_tire_type(tire_type)
        self.set_suspension_type(suspension_type)
        self.set_brake_type(brake_type)

    def set_load_capacity(self, load_capacity):
        self.__material_type_check__(load_capacity, (int, float, str), "load_capacity in kg")
        self.__load_capacity = load_capacity

    def set_max_strain(self, max_strain):
        self.__material_type_check__(max_strain, (int, float, str, type(None)), "max_strain in numeric SI")
        self.__max_strain = max_strain

    def set_max_stress(self, max_stress):
        self.__material_type_check__(max_stress, (int, float, str, type(None)), "max_stress in numeric SI")
        self.__max_stress = max_stress

    def set_tire_type(self, tire_type):
        self.__material_type_check__(tire_type, (str, type(None)), "tire_type")
        self.__tire_type = tire_type

    def set_suspension_type(self, suspension_type):
        self.__material_type_check__(suspension_type, (str, type(None)), "suspension_type")
        self.__suspension_type = suspension_type

    def set_brake_type(self, brake_type):
        self.__material_type_check__(brake_type, (str, type(None)), "brake_type")
        self.__brake_type = brake_type

    def get_load_capacity(self):
        return getattr(self, "_Chassis__load_capacity", None)

    def get_max_strain(self):
        return getattr(self, "_Chassis__max_strain", None)

    def get_max_stress(self):
        return getattr(self, "_Chassis__max_stress", None)

    def get_tire_type(self):
        return getattr(self, "_Chassis__tire_type", None)

    def get_suspension_type(self):
        return getattr(self, "_Chassis__suspension_type", None)

    def get_brake_type(self):
        return getattr(self, "_Chassis__brake_type", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "load_capacity": self.get_load_capacity(),
            "max_strain": self.get_max_strain(),
            "max_stress": self.get_max_stress(),
            "tire_type": self.get_tire_type(),
            "suspension_type": self.get_suspension_type(),
            "brake_type": self.get_brake_type()
        }
        base.update(added)
        return base

class Tire:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "tire", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        load_capacity = 0.0,
        max_stress = 0.0,
        tire_type = "undefined"
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = Chassis(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            load_capacity=load_capacity, 
            max_stress=max_stress, 
            tire_type=tire_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Load Capacity: {self.part_property.get_load_capacity()}
            Max Stress: {self.part_property.get_max_stress()}
            Tire Type: {self.part_property.get_tire_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class Brake:
    def __init__(
            self,
            id = "N/A",
            name = "Unknown Stock Name",
            quantity = 0, 
            price = 0.0, 
            description = "", 
            item_type = "brake", 
            brand = "N/A", 
            vat = 17.5,
            weight = 1.0,
            dimensions = (0.0,0.0,0.0),
            composition = {"undefined": 0},
            durability = "undefined",
            max_stress = 0.0,
            brake_type = "undefined"
        ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = Chassis(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            max_stress=max_stress, 
            brake_type=brake_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Max Stress: {self.part_property.get_max_stress()}
            Brake Type: {self.part_property.get_brake_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class Suspension:
    def __init__(
            self,
            id = "N/A",
            name = "Unknown Stock Name",
            quantity = 0, 
            price = 0.0, 
            description = "", 
            item_type = "suspension", 
            brand = "N/A", 
            vat = 17.5,
            weight = 1.0,
            dimensions = (0.0,0.0,0.0),
            composition = {"undefined": 0},
            durability = "undefined",
            max_stress = 0.0,
            suspension_type = "undefined"
        ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = Chassis(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            max_stress=max_stress, 
            suspension_type=suspension_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Max Stress: {self.part_property.get_max_stress()}
            Suspension Type: {self.part_property.get_suspension_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class Detailing(MaterialProperty):
    def __init__(
        self,
        weight = 0.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        primary_color = "",
        secondary_color = None,
        finish = "",
        texture = None,
        protection_type = None
    ):
        self.set_weight(weight)
        self.set_dimensions(dimensions)
        self.set_material_composition(composition)
        self.set_durability(durability)
        self.set_primary_color(primary_color)
        self.set_secondary_color(secondary_color)
        self.set_finish(finish)
        self.set_texture(texture)
        self.set_protection_type(protection_type)

    def set_finish(self, finish):
        self.__material_type_check__(finish, str, "finish")
        self.__finish = finish

    def set_primary_color(self, color):
        self.__material_type_check__(color, str, "primary_color")
        self.__primary_color = color

    def set_secondary_color(self, color):
        self.__material_type_check__(color, (str, type(None)), "secondary_color")
        self.__secondary_color = color

    def set_texture(self, texture):
        self.__material_type_check__(texture, (str, type(None)), "texture")
        self.__texture = texture

    def set_protection_type(self, protection_type):
        self.__material_type_check__(protection_type, (str, type(None)), "protection_type")
        self.__protection_type = protection_type

    def get_primary_color(self):
        return getattr(self, "_Detailing__primary_color", None)

    def get_secondary_color(self):
        return getattr(self, "_Detailing__secondary_color", None)

    def get_finish(self):
        return getattr(self, "_Detailing__finish", None)

    def get_texture(self):
        return getattr(self, "_Detailing__texture", None)

    def get_protection_type(self):
        return getattr(self, "_Detailing__protection_type", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "primary_color": self.get_primary_color(),
            "secondary_color": self.get_secondary_color(),
            "finish": self.get_finish(),
            "texture": self.get_texture(),
            "protection_type": self.get_protection_type(),
        }
        base.update(added)
        return base

class Paint:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "paint", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        primary_color = "",
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = Detailing(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            primary_color=primary_color
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Primary Color: {self.part_property.get_primary_color()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class SeatAndCover:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "seatandcover", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0, 0.0, 0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        primary_color = "",
        secondary_color = "",
        finish = "",
        protection_type = "",
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = Detailing(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            primary_color=primary_color, 
            secondary_color=secondary_color, 
            finish=finish, 
            protection_type=protection_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Primary Color: {self.part_property.get_primary_color()}
            Secondary Color: {self.part_property.get_secondary_color()}
            Finish: {self.part_property.get_finish()}
            Protection Type: {self.part_property.get_protection_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class DecalAndTint:
    def __init__(
        self,
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "decalandtint", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0, 0.0, 0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        primary_color = "",
        secondary_color = "",
        finish = "",
        protection_type = "",
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = Detailing(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            primary_color=primary_color, 
            secondary_color=secondary_color, 
            finish=finish, 
            protection_type=protection_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Primary Color: {self.part_property.get_primary_color()}
            Secondary Color: {self.part_property.get_secondary_color()}
            Finish: {self.part_property.get_finish()}
            Protection Type: {self.part_property.get_protection_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class ElectricalSystem(MaterialProperty):
    def __init__(
        self, 
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        avg_lifespan = 0,
        temperature_rating = None,
        battery_type = None,
        display_type = None,
    ):
        self.set_weight(weight)
        self.set_dimensions(dimensions)
        self.set_material_composition(composition)
        self.set_durability(durability)
        self.set_voltage(voltage)
        self.set_amperage(amperage)
        self.set_power_inout(power_inout)
        self.set_temperature_rating(temperature_rating)
        self.set_avg_lifespan(avg_lifespan)
        self.set_battery_type(battery_type)
        self.set_display_type(display_type)

    def set_voltage(self, voltage):
        self.__material_type_check__(voltage, (int, float, str), "voltage in V")
        self.__voltage = voltage

    def set_amperage(self, amperage):
        self.__material_type_check__(amperage, (int, float, str), "amperage in A")
        self.__amperage = amperage

    def set_power_inout(self, power_inout):
        self.__material_type_check__(power_inout, (int, float, str), "power_inout in W")
        self.__power_inout = power_inout

    def set_temperature_rating(self, temperature_rating):
        self.__material_type_check__(temperature_rating, (int, float, str, type(None)), "temperature_rating in C")
        self.__temperature_rating = temperature_rating

    def set_avg_lifespan(self, avg_lifespan):
        self.__material_type_check__(avg_lifespan, int, "avg_lifespan in hours")
        self.__avg_lifespan = avg_lifespan

    def set_battery_type(self, battery_type):
        self.__material_type_check__(battery_type, (str, type(None)), "battery_type")
        self.__battery_type = battery_type

    def set_display_type(self, display_type):
        self.__material_type_check__(display_type, (str, type(None)), "display_type")
        self.__display_type = display_type

    def get_voltage(self):
        return getattr(self, "_ElectricalSystem__voltage", None)

    def get_amperage(self):
        return getattr(self, "_ElectricalSystem__amperage", None)

    def get_power_inout(self):
        return getattr(self, "_ElectricalSystem__power_inout", None)

    def get_temperature_rating(self):
        return getattr(self, "_ElectricalSystem__temperature_rating", None)

    def get_avg_lifespan(self):
        return getattr(self, "_ElectricalSystem__avg_lifespan", None)

    def get_battery_type(self):
        return getattr(self, "_ElectricalSystem__battery_type", None)

    def get_display_type(self):
        return getattr(self, "_ElectricalSystem__display_type", None)

    def get_material_property(self):
        base = MaterialProperty.get_material_property(self)
        added = {
            "voltage": self.get_voltage(),
            "amperage": self.get_amperage(),
            "power_inout": self.get_power_inout(),
            "temperature_rating": self.get_temperature_rating(),
            "avg_lifespan": self.get_avg_lifespan(),
            "battery_type": self.get_battery_type(),
            "display_type": self.get_display_type()
        }
        base.update(added)
        return base

class Battery:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "battery", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        avg_lifespan = 0,
        temperature_rating = 50.0,
        battery_type = ""
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = ElectricalSystem(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            voltage=voltage, 
            amperage=amperage, 
            power_inout=power_inout, 
            avg_lifespan=avg_lifespan, 
            temperature_rating=temperature_rating, 
            battery_type=battery_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Voltage: {self.part_property.get_voltage()}
            Amperage: {self.part_property.get_amperage()}
            Power In/Out: {self.part_property.get_power_inout()}
            Average Lifespan: {self.part_property.get_avg_lifespan()}
            Temperature Rating: {self.part_property.get_temperature_rating()}
            Battery Type: {self.part_property.get_battery_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class WiringHarness:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "wiringharness", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        avg_lifespan = 0,
        temperature_rating = 50.0
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = ElectricalSystem(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            voltage=voltage, 
            amperage=amperage, 
            power_inout=power_inout, 
            avg_lifespan=avg_lifespan, 
            temperature_rating=temperature_rating
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Voltage: {self.part_property.get_voltage()}
            Amperage: {self.part_property.get_amperage()}
            Power In/Out: {self.part_property.get_power_inout()}
            Average Lifespan: {self.part_property.get_avg_lifespan()}
            Temperature Rating: {self.part_property.get_temperature_rating()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

class Infotainment:
    def __init__(
        self, 
        id = "N/A",
        name = "Unknown Stock Name",
        quantity = 0, 
        price = 0.0, 
        description = "", 
        item_type = "infotainment", 
        brand = "N/A", 
        vat = 17.5,
        weight = 1.0,
        dimensions = (0.0,0.0,0.0),
        composition = {"undefined": 0},
        durability = "undefined",
        voltage = 0.0,
        amperage = 0.0,
        power_inout = 0.0,
        avg_lifespan = 0,
        temperature_rating = 50.0,
        display_type = ""
    ):
        self.part_stock = StockItem(
            id=id, 
            name=name, 
            quantity=quantity, 
            price=price, 
            description=description, 
            item_type=item_type, 
            brand=brand, 
            vat=vat
        )
        self.part_property = ElectricalSystem(
            weight=weight, 
            dimensions=dimensions, 
            composition=composition, 
            durability=durability, 
            voltage=voltage, 
            amperage=amperage, 
            power_inout=power_inout, 
            avg_lifespan=avg_lifespan, 
            temperature_rating=temperature_rating, 
            display_type=display_type
        )

    def __str__(self):
        return (
            f"""
            {self.part_stock}
            Voltage: {self.part_property.get_voltage()}
            Amperage: {self.part_property.get_amperage()}
            Power In/Out: {self.part_property.get_power_inout()}
            Average Lifespan: {self.part_property.get_avg_lifespan()}
            Temperature Rating: {self.part_property.get_temperature_rating()}
            Display Type: {self.part_property.get_display_type()}
            """
        )

    def get_complete_details(self):
        stock = self.part_stock.get_stock_details()
        quality = self.part_property.get_material_property()
        stock.update(quality)
        filtered_stock = {}
        for k, v in stock.items():
            if v is not None:
                filtered_stock[k] = v
        stock = filtered_stock
        return stock

#Class Testers
# Engine object
engine = Engine()

# Transmission object
transmission = Transmission()

# Tire object
tire = Tire()

# Brake object
brake = Brake()

# Suspension object
suspension = Suspension()

# Paint object
paint = Paint()

# SeatAndCover object
seat_and_cover = SeatAndCover()

# DecalAndTint object
decal_and_tint = DecalAndTint()

# Battery object
battery = Battery()

# WiringHarness object
wiring_harness = WiringHarness()

# Infotainment object
infotainment = Infotainment()