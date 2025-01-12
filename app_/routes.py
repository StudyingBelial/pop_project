from flask import Flask, render_template, request, make_response, redirect, url_for, g, session

app = Flask(__name__)
app.secret_key = "SUPER_SECRET_BANKAI"

import sys
from os import getcwd
sys.path.append("..")
import ast
import csv
import pandas as pd
from datetime import datetime
from library import StockItem, Engine, Transmission, Tire, Brake, Suspension, Paint, SeatAndCover, DecalAndTint, Battery, WiringHarness, Infotainment, Visualizers

# method to create dataframe objects and return them
def df_creator(file_path):
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

@app.before_request
def data_inatilizers():

    # g object to store all the filepath of the csv files for the dataframes to update and access
    g.filepaths = {
        "engine": ".\\app_\\data\\engines.csv",
        "transmission": ".\\app_\\data\\transmissions.csv",
        "tire": ".\\app_\\data\\tires.csv",
        "brake": ".\\app_\\data\\brakes.csv",
        "suspension": ".\\app_\\data\\suspensions.csv",
        "paint": ".\\app_\\data\\paints.csv",
        "seat_and_cover": ".\\app_\\data\\seatandcovers.csv",
        "decal_and_tint": ".\\app_\\data\\decalandtints.csv",
        "battery" : ".\\app_\\data\\battery.csv",
        "wiringharness" : ".\\app_\\data\\wiringharness.csv",
        "infotainment" : ".\\app_\\data\\infotainment.csv"
    }

    # calling the method to create dataframes
    engine = df_creator(g.filepaths["engine"])
    transmission = df_creator(g.filepaths["transmission"])
    tire = df_creator(g.filepaths["tire"])
    brake = df_creator(g.filepaths["brake"])
    suspension = df_creator(g.filepaths["suspension"])
    paint = df_creator(g.filepaths["paint"])
    seat_and_cover = df_creator(g.filepaths["seat_and_cover"])
    decal_and_tint = df_creator(g.filepaths["decal_and_tint"])
    battery = df_creator(g.filepaths["battery"])
    wiringharness = df_creator(g.filepaths["wiringharness"])
    infotainment = df_creator(g.filepaths["infotainment"])

    # g object to store all the dataframes in a dict to dynamically access and change data
    g.dataframes = {
        "engine": engine,
        "transmission": transmission,
        "tire": tire,
        "brake": brake,
        "suspension": suspension,
        "paint": paint,
        "seat_and_cover": seat_and_cover,
        "decal_and_tint": decal_and_tint,
        "battery" : battery,
        "wiringharness" : wiringharness,
        "infotainment" : infotainment
    }
    print("Inatilized Dataframes")

    # g object to store all the classes in a dict to dynamically create objects
    g.classes = {
        "engine": Engine,
        "transmission": Transmission,
        "tire": Tire,
        "brake": Brake,
        "suspension": Suspension,
        "paint": Paint,
        "seat_and_cover": SeatAndCover,
        "decal_and_tint": DecalAndTint,
        "battery": Battery,
        "wiringharness": WiringHarness,
        "infotainment": Infotainment
    }
    print("Inatilized Classes")

# home page
@app.route('/')
def home():
    return render_template("index.html", cart_items=show_cart())

# access a row of a dataframe using the name of the df and the appropriate index
def row_accesser(value, df_name):
    try:
        # extracting a row from a df
        try:
            df = g.dataframes[df_name]
            row = df.loc[value]
        except AttributeError as e:
            error = f"Attribute Error: {e}"
            return error
        except KeyError as e:
            error = f"KeyError:{e}. Entered type does not exist!"
            return error
        if row.empty:
            return "Incorrect ID, Please Try Again"

        dictionary = row.to_dict()

        # normalizing all the data coming from the df before any calculation
        try:
            dictionary["dimensions"] = ast.literal_eval(dictionary["dimensions"])
            dictionary["composition"] = ast.literal_eval(dictionary["composition"])
            dictionary["quantity"] = int(dictionary["quantity"])
        except ValueError as e:
            error = f"ValueError: {e}"
            return error
        except TypeError as e:
            error = f"TypeError: {e}"
            return error
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return error

    return dictionary

# creates an object from the g.classes dict and inserts a set of values into it to trigger its constructor and handle it's data properly
def create_component_object(component,dictionary):
    try:
        # trying to create class from the appropriate component in g.classes
        try:
            obj = g.classes[component]
        except KeyError:
            error = f"Component {component} not found in g.classes"
            return error
        else:
            print(f"DICTIONARY BEFORE UNPACKING: {dictionary}")
            # Off case Error Handelling for an unknown behaviour caused by creation of a tuple
            if isinstance(dictionary, tuple):
                dictionary = dictionary[0]
            else:
                dictionary = dictionary

            # checking if loading the object with necessary input causes any errors    
            try:
                instance = obj(**dictionary)
            except ValueError as e:
                error = f"ValueError: {e}. Loading Value Caused Errors"
                return error
            except TypeError as e:
                error = f"ValueError: {e}. Loading Value Caused Errors"
                return error
            else:
                return instance # returning obj properly if no errors are caused
    except Exception as e:
        print(f"Unexpected Error: {e}")
    else:
        return None

def add_to_cart(dictionary):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(dictionary)
    session.modified = True

def show_cart():
    return session.get("cart", []) 

@app.route('/clear_cart')
def clear_cart():
    session.pop("cart", None)
    session.modified = True
    return redirect(url_for('home'))

@app.route('/show_cart')
def render_cart():
    return render_template("cart.html", cart_items= show_cart())

@app.route('/cart_by_id', methods=["POST"])
def add_item_by_id():
    try:
        item_search = request.form.get("item_search")
        search_type = request.form.get("item_type")
        component = request.form.get("component")
        quantity = request.form.get("quantity")
    except RuntimeError as e:
        error = f"Unable to request details {e} from the previous form"
        return render_template("error.html", message=error)  
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message=error)  

    item_data = row_accesser(df_name = component, value=item_search)

    # checking if the returned value is a vlaid dictionary
    if isinstance(item_data, str) or (not isinstance(item_data, dict)):
        return render_template("error.html", message = item_data)
    else:
        # Checks if the item requested by the user exists in the database
        if item_data is None:
            print("Item not found")
            return render_template("error.html", message = "Item not found")
        else:
            print("Item FOUND")

    # Normalizes the quantity into an int
    try:
        true_quantity = int(item_data["quantity"])
        quantity = int(quantity)
        true_quantity = int(true_quantity)
        print(f"TRUE QUANTITY: {true_quantity}")
        if (quantity < 1):
            print("Normalized Negative quantity to 1")
            quantity = 1
    except ValueError as e:
        print(f"Value Error: {e} quanitiy is invalid")
        quantity = 1
    except Exception as e:
        print(f"Unexpected Error: {e}")
        quantity = 1

    # Checks if quantity asked by the user is valid
    if (quantity > true_quantity):
        print(f"Error! Requested Quantity Exceeds current stock")
        print(f"Normalized quanity to max quantity in db")
        quantity = true_quantity

    # creating an  appropraite object of the data and checking if all the values align, as well as to set different values like id and quantity
    obj = create_component_object(component=component, dictionary=item_data)

    # Checking if 'obj' has a valid value and was handeled correctly in create_component_object
    if (isinstance(obj, str)):
        return render_template("error.html", message = obj)
    else:
        if (obj == None):
            return render_template("error.html", message = "Created object is empty")

    # executing the methods associated with the object
    try:
        obj.part_stock.set_id(item_search)
        obj.part_stock.set_quantity(quantity)
        print(f"OBJECT DETAILS: {type(obj.get_complete_details())}")
        add_to_cart(obj.get_complete_details())
    except ValueError as e:
        error = f"ValueError:  {e}. Error in setting the ID or the Quantity of the requested Item"
        return render_template("error.html", message=error)
    except AttributeError as e:
        error = f"AttributeError: {e}. Requested methods are unavailaible"
        return render_template("error.html", message=error)
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message=error)  


    return render_template("index.html", cart_items= show_cart())

@app.route('/add_new_item', methods=["POST" ,"GET"])
def add_new_stock():
    if (request.method == "GET"):
        return render_template("add_new_stock.html")

    try:
        dictionary = request.form.to_dict()
    except RuntimeError as e:
        error = f"Unable to request details {e} from the previous form"
        return render_template("error.html", message=error)  
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message=error)  

    # Normalizing all the data into valid types to appropriately add into the db    
    try:
        dictionary["price"] = float(dictionary["price"])
        dictionary["vat"] = float(dictionary["vat"])
        dictionary["weight"] = float(dictionary["weight"])
        dictionary["quantity"] = int(dictionary["quantity"])
        dictionary["dimensions"] = ast.literal_eval(dictionary["dimensions"])
        dictionary["composition"] = ast.literal_eval(dictionary["composition"])  
    except ValueError as e:
        print(f"Invalid price {e}")
        error = f"{e} is an invalid number"
        return error
    except TypeError as e:
        print(f"Invalid price {e}")
        error = f"{e} is an invalid number"
        return error
    except Exception as e:
        print(f"Unexpected Error: {e}")
        error = f"{e} is an invalid number"
        return error

    # Normalizing the data into valid ranges
    if (dictionary["price"] < 0):
        dictionary["price"] = 1
    if (dictionary["vat"] < 0):
        dictionary["vat"] = 0
    if (dictionary["weight"] < 1):
        dictionary["weight"] = 1
    if (dictionary["quantity"] < 1):
        dictionary["quantity"] = 1

    missing_dict = find_missing_keys(dictionary, dictionary["item_type"])
    return render_template("new_component_specific.html", dictionary=missing_dict)

# a method that find the component specific attributes and returns them as a dict
def find_missing_keys(new_item, component):  
    # create a session if not created
    if "new_stock" not in session:
        session["new_stock"] = []
    session["new_stock"] =  new_item
    session.modified = True

    # create an object of the component to find all the keys
    try:
        obj = g.classes[component]
    except KeyError:
        print(f"Component {component} not found in g.classes")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
    new_component = obj().get_complete_details()

    # identify keys that are present in new_component but missing in new_item
    missing_keys = []
    for key in new_component.keys():
        if key not in new_item.keys():
            missing_keys.append(key)
            
    missing_keys_dict = {}
    for keys in missing_keys:
        formatted_keys = keys.replace("_", " ").title()
        missing_keys_dict[keys] = formatted_keys
    return missing_keys_dict

@app.route('/new_component_specific', methods=["POST"])
def add_new_component():
    try:
        component_values = request.form.to_dict()
    except RuntimeError as e:
        error = f"Unable to request details {e} from the previous form"
        return render_template("error.html", message=error)  
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message=error) 

    #updating the dict with information from the previous form
    component_values.update(session["new_stock"])

    return add_to_df(master_dictionary=component_values, message="Item Added Successfully")

def add_to_df(master_dictionary, message):
    obj = create_component_object(component = master_dictionary["item_type"], dictionary=master_dictionary)

    # Checking if 'obj' has a valid value and was handeled correctly in create_component_object
    if (isinstance(obj, str)):
        return render_template("error.html", message = obj)
    else:
        if (obj == None):
            return render_template("error.html", message = "Created object is empty")
        else:
            print(f"OBJECT CREATED SUCCESSFULLY {obj}")

    # ADDING THE NEW OBJECT DATA TO THE DATAFRAMES AND THEN INTO A FILE
    dictionary = obj.get_complete_details()

    #creating a new df with all the necessary fields
    dictionary_df = pd.DataFrame([dictionary]).set_index("id")
    object_df = g.dataframes[dictionary["item_type"]]
    # concatenating the new df with the old df which has all the data
    object_df = pd.concat([object_df, dictionary_df])

    # Comitting df to the appropriate file
    df.to_csv(g.filepaths[dictionary["item_type"]])
    print("DF committed to storage")

    return render_template("index.html", message = message)

@app.route('/change_stock', methods=["POST", "GET"])
def change_stock():
    if (request.method == "GET"):
        return render_template("change_stock_form.html")
    try:
        # requesting the necessary files
        try:
            id = request.form.get("id")
            component = request.form.get("component")
        except RuntimeError as e:
            error = f"Unable to request details {e}"
            return render_template("error.html", message = error)

        # requesting an object from the id and components and checking if it is valid
        try:
            item_data = row_accesser(df_name = component, value=id)
            obj = create_component_object(component=component, dictionary=item_data)
            obj.part_stock.set_id(id)
            change_details = obj.get_complete_details()
        except AttributeError as e:
            error = f"Requested Operations are invalid {e}"
            return render_template("error.html", message = error)

    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message = error)

    # checking if the cookie exists
    if not "change_stock" in session:
        session["change_stock"] = []

    # overwriting the cookie, just in case there is anything on it
    session["change_stock"] = change_details
    return render_template("change_stock.html", details=change_details)

@app.route('/changer_grabber_and_verify', methods=["POST"])
def get_change_stock():
    try:
        # requesting all the data from the page in a dictionary
        try:
            dictionary = request.form.to_dict()
        except RuntimeError as e:
            error = f"Unable to request details {e}"
            return render_template("error.html", message = error)

        # normalizing the all the data properly for insersion
        try:
            dictionary["price"] = float(dictionary["price"])
            dictionary["vat"] = float(dictionary["vat"])
            dictionary["weight"] = float(dictionary["weight"])
            dictionary["quantity"] = int(dictionary["quantity"])
            dictionary["dimensions"] = ast.literal_eval(dictionary["dimensions"])
            dictionary["composition"] = ast.literal_eval(dictionary["composition"])  
        except ValueError as e:
            error = f"{e}: is an invalid number"
            return render_template("error.html", message = error)
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message = error)

    missing_dict = find_missing_keys(dictionary, dictionary["item_type"])
    all_values = session["change_stock"]
    all_values.update(dictionary)
    key_value_dict = {}

    for key, value in missing_dict.items():
        corresponding_value = all_values.get(key, None)
        key_value_dict[key] = [value, corresponding_value]

    return render_template("change_component_specific.html", dictionary=key_value_dict)

def edit_existing_values(master_dictionary,message=""):
    # extracting the index to add it to the df properly
    index = master_dictionary.pop("id")
    # extracting component name to call the appropriate df
    component = master_dictionary["item_type"]

    #calling and changing the proper df
    df = g.dataframes[component]
    df.loc[index, master_dictionary.keys()] = master_dictionary.values()

    #committing changes to the file
    df.to_csv(g.filepaths[component])
    return render_template("index.html", message = message)

@app.route('/change_component_specific', methods=["POST"])
def change_and_commit_stock():
    # error handelling to see if request from the previous page works
    try:
        component_values = request.form.to_dict()
    except RuntimeError as e:
        error = f"Unable to request details {e}"
        return render_template("error.html", message = error)
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message = error)

    component_values.update(session["change_stock"])
    return edit_existing_values(master_dictionary=component_values, message="Item Changed Successfully")

@app.route('/check_out_verify')
def check_out_verify():
    try:
        # checking the cart before any code is run with session["cart"]
        try:
            if not session.get("cart"):
                return "Cart is empty"
        except KeyError as e:
            error = "Cart is empty"
            return render_template("error.html", message = error)
        except Exception as e:
            error = f"Unexpected Error: {e}"
            return render_template("error.html", message = error)

        # iterating through the cart to access each item 
        for dicts in session["cart"]:
            # type checking incase data was not handeled properly during insersion
            try:
                # calculating the total with vat for the check out process
                item_total = float(dicts["quantity"]) * float(dicts["price"])
                item_total = item_total + item_total * float(dicts["vat"])
                dicts["item_total"] = item_total
            except TypeError as e:
                error = "Cart has invalid Data"
                return render_template("error.html", message = error)
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message = error)
    session.modified = True
    return render_template("check_out.html", cart_items=session["cart"])

@app.route('/remove_item_from_cart', methods=["GET"])
def remove_item_from_cart():
    # requesting id of the item to be removed
    item_id = request.args.get("item_id")
    if not item_id:
        return "Unable to remove item from cart"

    # checking if session["cart"] exists or not     
    try:
        if not session.get("cart"):
            return "Unable to remove item from cart! Cart is empty"
    except KeyError as e:
        return "Unable to remove item from cart! Cart is empty"
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return error

    item_found = False
    new_cart = []

    # looping through to cart to find the id of the requested removal
    for item in session["cart"]:
        try:
            if str(item.get("id")) == str(item_id):
                item_found = True
            else:
                new_cart.append(item)
        except KeyError as e:
            return "Requested Item does not exist in cart"
        except Exception as e:
            error = f"Unexpected Error: {e}"
            return error

    # updating the new cart       
    session["cart"] = new_cart
    session.modified = True

    # rendering the home page with the appropriate message according to how the code was executed
    if item_found:
        return render_template("index.html", cart_items=show_cart(), message="Item removed from cart")
    else:
        return render_template("index.html", cart_items=show_cart(), message="Unable to removed item from cart")

def df_committer_post_purchase():
    # checking if session["cart"] exists or not   
    try:
        if not session.get("cart"):
            return "Unable to remove item from cart! Cart is empty"
    except KeyError as e:
        return "Unable to remove item from cart! Cart is empty"
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return 

    for items in session["cart"]:
        print(f"ITEMS FROM CART: {items}")
        df = g.dataframes[items["item_type"]]
        row = df.loc[items["id"]]
        print(f"ITEM ID: {items["id"]} TYPE: {type(items["id"])}")

        # Normalizing all the values in the row to appropriate types
        try:
            row["price"] = float(row["price"])
            row["vat"] = float(row["vat"])
            row["weight"] = float(row["weight"])
            row["quantity"] = int(row["quantity"])
            row["dimensions"] = ast.literal_eval(row["dimensions"])
            row["composition"] = ast.literal_eval(row["composition"]) 
        except ValueError as e:
            error = f"ValueError: {e}. is an invalid number"
            return error
        except TypeError as e:
            error = f"TypeError: {e}. is an invalid number"
            return error
        except Exception as e:
            error = f"UnexpectedError:{e}, is an invalid number"
            return error

        # changing the stock using the object
        try:
            obj = g.classes[items["item_type"]](**row) # creating the object and calling the constructor as well 
            obj.part_stock.decrease_stock(int(items["quantity"]))
            obj.part_stock.set_id(items["id"])
            master_dict = obj.get_complete_details()
        except TypeError as e:
            error = f"TypeError: {e}. session['cart'] contains invalid 'quantity' type"
            return error
        except ValueError as e:
            error = f"ValueError: {e}. Unable to call StockItem.decrease_stock() to change stock as quantity value is invalid"
            return error
        except AttributeError as e:
            error = f"AttributeError: {e}. Requested Method cannot be accessed"
            return error

        edit_existing_values(master_dict)
        # comitting the df to the file
        df.to_csv(g.filepaths[items["item_type"]])
    return None

@app.route('/buy_page', methods=["POST"])
def buy_page():
    return render_template("buy.html")

@app.route('/buy' , methods=["POST"])
def buy():
    # file path for the main file with the purchase history
    BUY_HISTORY_PATH = ".\\app_\\data\\purchase_history.csv"
    try:
        user_details = request.form.to_dict()
    except RuntimeError as e:
        err = f"Unable to request details {e}"
        return render_template("error.html", message= err)
    except Exception as e:
        err = f"Unexpected Error: {e}"
        return render_template("error.html", message= err)

    # checking if session["cart"] exists or not   
    try:
        if not session.get("cart"):
            return render_template("error.html", message="Unable to remove item from cart! Cart is empty")
    except KeyError as e:
        return render_template("error.html", message="Unable to remove item from cart! Cart is empty")
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return 

    # used to create a dictionary with all the necessary fields to be added to the purchase_history csv    
    master_dictionary = {}
    master_dictionary.update(user_details)
    csv_keys = ["customer_name", "phonenumber", "id", "name", "quantity", "vat", "item_type", "item_total"]
    writer_list = []
    for items in session["cart"]:
        master_dictionary.update(items)
        csv_dictionary = {}
        for key in csv_keys:
            value = master_dictionary.get(key)
            csv_dictionary[key] = value
        csv_dictionary["time_stamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer_list.append(csv_dictionary)

    # writes the necessay details in purchase_history csv
    with open (BUY_HISTORY_PATH, mode="a", newline="") as file:
        for rows in writer_list:
            writer = csv.DictWriter(file, fieldnames=csv_keys + ["time_stamp"])
            writer.writerow(rows)

    # calls the fucntion that commits all the changes in the cart to storage
    err = df_committer_post_purchase()
    msg = ""
    if (err == None):
        msg = "Purchase Changes Comitted successfully"
    else:
        if isinstance(err, str):
            return render_template("error.html", message=err)

    # clears the current cart which also renders the home page
    clear_cart()
    return render_template("index.html", message="Item Bough Successfully")

@app.route('/remove_item', methods=["POST", "GET"])
def remove_item():
    if (request.method == "GET"):
        return render_template("remove_item.html")

    # requesting all the necessary files
    try:
        id = request.form.get("id")
        component = request.form.get("component")
    except RuntimeError as e:
        error = f"Unable to request details: {e}"
        return render_template("error.html", message = error)
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message = error)

    # trying to remove the row with the entered ID
    try:
        df = g.dataframes[component]
        df = df.drop(id, axis = 0)
    except KeyError as e:
        error = f"Given Item ID does not exixt: {e} \n Did you specify the Component Properly?"
        return render_template("error.html", message = error)
    except Exception as e:
        error = f"Unexpected Error:  {e}"
        return render_template("error.html", message = error)

    # commits the df to storage
    df.to_csv(g.filepaths[component])
    return render_template("index.html", message="Item Removed Successfully")

@app.route('/increase_stock', methods=["POST", "GET"])
def increase_stock():
    if (request.method == "GET"):
        return render_template("increase_stock.html")
    
    # requesting all the necessary files
    try:
        id = request.form.get("id")
        component = request.form.get("component")
        quantity = request.form.get("quantity")
    except RuntimeError as e:
        error = f"Unable to request details: {e}"
        return render_template("error.html", message = error)
    except Exception as e:
        error = f"Unexpected Error: {e}"
        return render_template("error.html", message = error)

    item_data = row_accesser(df_name = component, value=id)

    # checking if the returned value is a vlaid dictionary
    if isinstance(item_data, str) or (not isinstance(item_data, dict)):
        return render_template("error.html", message = item_data)
    else:
        # Checks if the item requested by the user exists in the database
        if item_data is None:
            print("Item not found")
            return render_template("error.html", message = "Item not found")
        else:
            print("Item FOUND")

    # Normalizes the quantity into an int
    try:
        quantity = int(quantity)
        if (quantity < 1):
            print("Normalized Negative quantity to 1")
            quantity = 1
    except ValueError as e:
        print(f"Value Error: {e} quanitiy is invalid")
        quantity = 1
    except Exception as e:
        print(f"Unexpected Error: {e}")
        quantity = 1

    # creating an  appropraite object of the data and checking if all the values align, as well as to set different values like id and quantity
    obj = create_component_object(component=component, dictionary=item_data)
    # changing the stock using the object
    try: 
        obj.part_stock.increase_stock(quantity)
        obj.part_stock.set_id(id)
        master_dict = obj.get_complete_details()
    except TypeError as e:
        error = f"TypeError: {e}. session['cart'] contains invalid 'quantity' type"
        return error
    except ValueError as e:
        error = f"ValueError: {e}. Unable to call StockItem.decrease_stock() to change stock as quantity value is invalid"
        return error
    except AttributeError as e:
        error = f"AttributeError: {e}. Requested Method cannot be accessed"
        return error
    edit_existing_values(master_dict)
    # comitting the df to the file
    df = g.dataframes[component]
    df.to_csv(g.filepaths[component])
    return render_template("index.html", message="Stock Successfully Increases", cart_items=show_cart())

@app.route('/visualizers', methods=["GET"])
def visualizers():
    visualizers = Visualizers(".\\app_\\data\\purchase_history.csv")
    visualizers.sales_over_time()
    visualizers.sale_per_transaction()
    visualizers.quantity_sold_overtime()
    visualizers.revenue_by_type()
    return render_template("visualizers.html")