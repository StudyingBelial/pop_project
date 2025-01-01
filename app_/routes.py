from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

import sys
sys.path.append("./library/")
from navsys import NavSys
from visualizer import Visualiser

@app.route('/')
def home():
    return "Hello World!"