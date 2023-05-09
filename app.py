from flask import Flask, render_template
from flask_googlemaps import GoogleMaps, Map
from ping3 import ping, verbose_ping
import googlemaps

app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = "AIzaSyB4Mm3IJnMfHU3D4yacjnzBtvqIVhaJ6mA"
GoogleMaps(app)
gmaps = googlemaps.Client(key='AIzaSyB4Mm3IJnMfHU3D4yacjnzBtvqIVhaJ6mA')
