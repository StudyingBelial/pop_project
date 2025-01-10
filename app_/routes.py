from flask import Flask, render_template, request, make_response, redirect, url_for, g, session

app = Flask(__name__)
app.secret_key = "SUPER_SECRET_BANKAI"

import sys
from os import getcwd
sys.path.append("..")
import ast
import csv
import pandas as pd
from library import StockItem, Engine, Transmission, Tire, Brake, Suspension, Paint, SeatAndCover, DecalAndTint, Battery, WiringHarness, Infotainment


def df_creator(file_path):
    try:
        data_frame = pd.read_csv(file_path, index_col="id")
        return data_frame
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"No data: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        print(f"{file_path} has been passed")

@app.before_request
def data_inatilizers():
    g.filepaths = {
        "engine": ".\\app_\\data\\engines.csv",
        "transmission": ".\\app_\\data\\transmissions.csv",
        "tire": ".\\app_\\data\\tires.csv",
        "brake": ".\\app_\\data\\brakes.csv",
        "suspension": ".\\app_\\data\\suspensions.csv",
        "paint": ".\\app_\\data\\paints.csv",
        "seat_and_cover": ".\\app_\\data\\seatandcovers.csv",
        "decal_and_tint": ".\\app_\\data\\decalandtints.csv",
        # "battery" = battery,
        # "wiringharness" = wiringharness,
        # "infotainment" = infotainment
    }
    engine = df_creator(g.filepaths["engine"])
    transmission = df_creator(g.filepaths["transmission"])
    tire = df_creator(g.filepaths["tire"])
    brake = df_creator(g.filepaths["brake"])
    suspension = df_creator(g.filepaths["suspension"])
    paint = df_creator(g.filepaths["paint"])
    seat_and_cover = df_creator(g.filepaths["seat_and_cover"])
    decal_and_tint = df_creator(g.filepaths["decal_and_tint"])
    #battery = df_creator("")
    #wiringharness = df_creator("")
    #infotainment = df_creator("")


    g.dataframes = {
        "engine": engine,
        "transmission": transmission,
        "tire": tire,
        "brake": brake,
        "suspension": suspension,
        "paint": paint,
        "seat_and_cover": seat_and_cover,
        "decal_and_tint": decal_and_tint,
        # "battery" = battery,
        # "wiringharness" = wiringharness,
        # "infotainment" = infotainment
    }
    print("Inatilized Dataframes")
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

def row_accesser(value, df_name):
    try:
        df = g.dataframes[df_name]
        row = df.loc[value]
    except AttributeError as e:
        print(f"Attribute Error: {e}")
    except KeyError as e:
        print(f"KeyError:{e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None
    else:
        # dictionary = {}
        # for col, nested_dict in row.to_dict().items():
        #     # Extract the value for the given row index
        #     dictionary[col] = nested_dict.get(value)

        # try:
        #     dictionary["dimensions"] = ast.literal_eval(dictionary["dimensions"])
        #     dictionary["composition"] = ast.literal_eval(dictionary["composition"])
        # except (ValueError, SyntaxError) as e:
        #     print(f"Error parsing dimensions or composition: {e}")
        #     return None
        dictionary = row.to_dict()
        print(dictionary)
        dictionary["dimensions"] = ast.literal_eval(dictionary["dimensions"])
        dictionary["composition"] = ast.literal_eval(dictionary["composition"])
        return dictionary

def create_component_object(component,dictionary):
    try:
        obj = g.classes[component]
    except KeyError:
        print(f"Component {component} not found in g.classes")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
    else:
        return obj(**dictionary)
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

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/cart_by_id', methods=["POST"])
def add_item_by_id():
    try:
        item_search = request.form.get("item_search")
        search_type = request.form.get("item_type")
        component = request.form.get("component")
        quantity = request.form.get("quantity")
    except RuntimeError as e:
        print(f"Unable to request details {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    try:
        quantity = int(quantity)
    except ValueError as e:
        print(f"Value Error: {e} quanitiy is invalid")
        quantity = 1
    except Exception as e:
        print(f"Unexpected Error: {e}")
    item_data = row_accesser(df_name = component, value=item_search)

    if item_data is None:
        print("Item not found")
        return "Item Not Found"
    else:
        print("Item FOUND")

    obj = create_component_object(component=component, dictionary=item_data)
    obj.part_stock.set_id(item_search)
    obj.part_stock.set_quantity(quantity)
    add_to_cart(obj.get_complete_details())
    return render_template("index.html", cart_items= show_cart())

@app.route('/add_new_stock_page')
def add_stock_page():
    return render_template("add_new_stock.html")

@app.route('/add_new_item', methods=["POST"])
def add_new_stock():
    try:
        dictionary = request.form.to_dict()
    except RuntimeError as e:
        print(f"Unable to request details {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
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
    except Exception as e:
        print(f"Unexpected Error: {e}")
        error = f"{e} is an invalid number"
        return error

    missing_dict = find_missing_keys(dictionary, dictionary["item_type"])
    return render_template("new_component_specific.html", dictionary=missing_dict)

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
    print(f"Keys in new_component but not in new_item: {missing_keys}")
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
        print(f"Unable to request details {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    component_values.update(session["new_stock"])
    return add_to_df(master_dictionary=component_values, message="Item Added Successfully")

def add_to_df(master_dictionary, message):
    obj = create_component_object(component = master_dictionary["item_type"], dictionary=master_dictionary)
    print(f"OBJECT CREATED SUCCESSFULLY {obj}")
    # ADDING THE NEW OBJECT DATA TO THE DATAFRAMES AND THEN INTO A FILE
    dictionary = obj.get_complete_details()
    dictionary_df = pd.DataFrame([dictionary]).set_index("id")
    object_df = g.dataframes[dictionary["item_type"]]
    object_df = pd.concat([object_df, dictionary_df])
    object_df.to_csv(g.filepaths[dictionary["item_type"]])
    return render_template("index.html", message = message)

@app.route('/change_stock_page')
def load_stock_page():
    return render_template("change_stock_form.html")

@app.route('/change_stock', methods=["POST"])
def change_stock():
    try:
        id = request.form.get("id")
        component = request.form.get("component")
    except RuntimeError as e:
        print(f"Unable to request details {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

    item_data = row_accesser(df_name = component, value=id)
    obj = create_component_object(component=component, dictionary=item_data)
    obj.part_stock.set_id(id)
    change_details = obj.get_complete_details()
    if not "change_stock" in session:
        session["change_stock"] = []
    session["change_stock"] = change_details
    return render_template("change_stock.html", details=change_details)

@app.route('/changer_grabber_and_verify', methods=["POST"])
def get_change_stock():
    try:
        dictionary = request.form.to_dict()
        print(dictionary)
    except RuntimeError as e:
        print(f"Unable to request details {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    try:
        dictionary["price"] = float(dictionary["price"])
        dictionary["vat"] = float(dictionary["vat"])
        dictionary["weight"] = float(dictionary["weight"])
        dictionary["quantity"] = int(dictionary["quantity"])
        dictionary["dimensions"] = ast.literal_eval(dictionary["dimensions"])
        dictionary["composition"] = ast.literal_eval(dictionary["composition"])  
    except ValueError as e:
        print(f"Invalid price {e}")
        error = f"{e}: is an invalid number"
        return error
    except Exception as e:
        print(f"Unexpected Error: {e}")
        error = f"{e} is an invalid number"
        return error

    missing_dict = find_missing_keys(dictionary, dictionary["item_type"])
    all_values = session["change_stock"]
    all_values.update(dictionary)
    key_value_dict = {}

    for key, value in missing_dict.items():
        corresponding_value = all_values.get(key, None)
        key_value_dict[key] = [value, corresponding_value]

    return render_template("change_component_specific.html", dictionary=key_value_dict)

def commit_df_to_storage(df, component):
    df.to_csv(g.filepaths[component])
    return True

def edit_existing_values(master_dictionary,message):
    print(f"Master Dictionary: {master_dictionary}")
    index = master_dictionary.pop("id")
    component = master_dictionary["item_type"]
    df = g.dataframes[component]
    df.loc[index, master_dictionary.keys()] = master_dictionary.values()
    print(f"ROW: {df.loc[index]}")
    if commit_df_to_storage(df, component):
        print("DF committed to storage")
    print(f"Dataframe {df}")
    return render_template("index.html", message = message)

@app.route('/change_component_specific', methods=["POST"])
def change_and_commit_stock():
    try:
        component_values = request.form.to_dict()
    except RuntimeError as e:
        print(f"Unable to request details {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    component_values.update(session["change_stock"])
    return edit_existing_values(master_dictionary=component_values, message="Item Changed Successfully")