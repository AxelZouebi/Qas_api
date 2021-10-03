from Affluence import Affluence
from flask import Flask, request
from flask_cors import CORS, cross_origin
from bson.json_util import dumps
import pymongo
import certifi
import urllib.parse
import requests

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def display():
    return 'root'

@app.route("/affluence", methods = ['POST', 'GET'])
@cross_origin()
def display_affluence():
    ca = certifi.where()
    client=pymongo.MongoClient('mongodb+srv://dbSmartcy:Dsrush2021@cluster0.linaa.mongodb.net/Smartcy', tlsCAFile=ca)
    db = client['Smartcy']
    if request.method == 'POST':
        print('post method la ici')
        data = request.get_json()
        address = data['address']
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
        response = requests.get(url).json()
        lat = response[0]["lat"]
        lon = response[0]["lon"]
        new_affluence = Affluence(lat=lat, lon=lon, densite=data['densite'], remarque=data['remarque']).save()
    else: 
        affluence = db.affluence
        json_lieu = list(affluence.find())
        All_lieu = []
        for key in json_lieu:
            All_lieu.append(key)
        json_data = dumps(All_lieu)
        return json_data

@app.route("/lieu")
@cross_origin()
def display_lieu():
    return 'lieu'

if __name__ == "__main__":
    app.run()