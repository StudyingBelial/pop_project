import ast
import csv
import pandas as pd
from library import Engine

    
def data_frame_manager():
    engine = df_creator(".\\app_\\data\\engines.csv")
    # brake = df_loader(".\\app_\\data\\brakes.csv")
    # suspension = df_loader(".\\app_\\data\\suspensions.csv")
    # tire = df_loader(".\\app_\\data\\tires.csv")
    # transmission = df_loader(".\\app_\\data\\transmissions.csv")
    row = engine.loc["EN0001"]
    specific_row = engine.loc[engine['column_name'] == 'desired_value']
    dictionary = row.to_dict()
    dimensions = ast.literal_eval(dictionary["dimensions"])
    composition = ast.literal_eval(dictionary["composition"])
    dictionary["dimensions"] = dimensions
    dictionary["composition"] = composition
    obj = Engine(**dictionary)
    dictor = obj.get_complete_engine_details()
    for key, value in dictor.items():
        print(f"{key}: {value}")

data_frame_manager()
