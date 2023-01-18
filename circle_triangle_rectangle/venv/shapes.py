from flask import Flask
from flask import request
from flask import jsonify
import math

app = Flask(__name__)


@app.route("/rectangle")
def calculate_rectangle():
    height = int(request.args.get("height"))
    width = int(request.args.get("width"))
    area = height * width
    result = jsonify(height=height, width=width, area=area)
    return result


@app.route("/circle")
def calculate_circle():
    radius = int(request.args.get("radius"))
    area = math.pi * radius ** 2
    return jsonify(radius=radius, area=area)


@app.route("/triangle")
def calculate_triangle():
    base = int(request.args.get("base"))
    height = int(request.args.get("height"))
    area = (base * height) / 2
    return jsonify(base=base, height=height, area=area)
