from mongoengine import *
from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, FloatField, IntField, ReferenceField, StringField
import datetime
import pymongo
import certifi

ca = certifi.where()

connect(host='mongodb+srv://dbSmartcy:Dsrush2021@cluster0.linaa.mongodb.net/Smartcy', tlsCAFile=ca)

class Lieu(Document):
    name = StringField()
    city = StringField()

class Affluence(Document):
    lat = FloatField(Required=True)
    lng = FloatField(Required=True)
    densite = IntField(required=True)
    remarque = StringField(max_length=100)
    date = DateTimeField(default=datetime.datetime.now().strftime("%H:%M:%S"))

# mairie_argenteuil = Lieu(name="Mairie", city="Argenteuil").save()
# affluence_1 = Affluence(lieu=mairie_argenteuil, densite='3', remarque="c'est nul").save()
# mairie_paris = Lieu(name="Mairie", city="Paris").save()
# affluence_1 = Affluence(lieu=mairie_paris, densite='5', remarque="Y'a trop de monde wola").save()
# mairie_jolie_foret = Lieu(name="Mairie", city="Jolie foret").save()
# affluence_1 = Affluence(lieu=mairie_jolie_foret, densite='1', remarque="wahoo la queue est courte, c'a me fait plaisir").save()
