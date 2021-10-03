from Affluence import Affluence
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from bson.json_util import dumps
import pymongo
import certifi
import urllib.parse
import requests
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

ca = certifi.where()
client=pymongo.MongoClient('mongodb+srv://dbSmartcy:Dsrush2021@cluster0.linaa.mongodb.net/Smartcy', tlsCAFile=ca)
db = client['Smartcy']
affluence = db.affluence

@app.route("/")
@cross_origin()
def display():
    return 'root'

@app.route("/affluence", methods = ['GET'])
@cross_origin()
def display_affluence():
    json_lieu = list(affluence.find())
    All_lieu = []
    for key in json_lieu:
        All_lieu.append(key)
    json_data = dumps(All_lieu)
    return json_data



@app.route('/post_affluence', methods = ['POST'])
@cross_origin()
def post_affluence():
    if request.is_json:
        content = request.get_json()
        affluence.insert_one(content)
        return {"sucsess":"True"}
    else:
        return {"success": "But not json"}

if __name__ == "__main__":
    app.run()