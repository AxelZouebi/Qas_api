from flask import Flask
from bson.json_util import dumps
import pymongo
import certifi

app = Flask(__name__)

@app.route("/")
def display():
    return 'root'

@app.route("/affluence")
def display_affluence():
    ca = certifi.where()
    client=pymongo.MongoClient('mongodb+srv://dbSmartcy:Dsrush2021@cluster0.linaa.mongodb.net/Smartcy', tlsCAFile=ca)
    db = client['Smartcy']
    affluence = db.affluence
    json_lieu = list(affluence.find())
    All_lieu = []
    for key in json_lieu:
        All_lieu.append(key)
    json_data = dumps(All_lieu)
    return json_data

@app.route("/lieu")
def display_lieu():
    return 'lieu'

if __name__ == "__main__":
    app.run()