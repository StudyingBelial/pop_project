import ast
import csv
import pandas as pd
from library import Engine

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
    
def file_updater(file_path, data_frame):
    pass

def data_frame_manager():
    engine = df_loader(".\\app_\\data\\engines.csv")
    # brake = df_loader(".\\app_\\data\\brakes.csv")
    # suspension = df_loader(".\\app_\\data\\suspensions.csv")
    # tire = df_loader(".\\app_\\data\\tires.csv")
    # transmission = df_loader(".\\app_\\data\\transmissions.csv")
    row = engine.loc["EN0001"]
    dictionary = row.to_dict()
    dimensions = ast.literal_eval(dictionary["dimensions"])
    composition = ast.literal_eval(dictionary["composition"])
    dictionary["dimensions"] = dimensions
    dictionary["composition"] = composition
    obj = Engine(**dictionary)
    dictor = obj.get_complete_engine_details()
    for key, value in dictor.items():
        print(f"{key}: {value}")

