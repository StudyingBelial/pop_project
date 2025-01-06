from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import sys
from os import getcwd
sys.path.append("..")
print("Current Directory:", getcwd())
from library import StockItem
from file_reader import df_creator



@app.route('/')
def home():
    return render_template("index.html")

def data_inatilizers():
    engine = df_creator(".\\data\\engines.csv")
    brake = df_creator(".\\data\\brakes.csv")
    suspension = df_creator(".\\data\\suspensions.csv")
    tire = df_creator(".\\data\\tires.csv")
    transmission = df_creator(".\\data\\transmissions.csv")
    # ADD MORE FILES

def engine_obj(engine_df,field, value):
    pass