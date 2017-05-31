import json
import BaseHTTPServer
import BaseHTTPRequestHandler
import requests
import re
import collections
import struct
import base64
import googlemaps

from googlemaps.convert import latlng

def get_restaurantes (lat, lng):
    gmaps = googlemaps.Client(key='AIzaSyDxjE_B2p2t199wTZPwBErRiOmaqL1hkhM')

    locacion = latlng((lat,lng))
    lugares = gmaps.places_nearby(locacion, 300, type='Restautantes')
    restaurantes = '{\"restaurantes\":['
    for i in range(len(lugares['resultado'])):
        restaurantes +='{\"nombre\":\"'
        restaurantes += lugares['resultado'][i]['nombre']
        restaurantes +='\", '
        restaurantes +='\"lat\":'
        restaurantes += str(lugares['resultado'][i]['geometry']['locacion']['lat'])
        restaurantes +=', '
        restaurantes +='\"lng\":'
        restaurantes += str(lugares['resultado'][i]['geometry']['locacion']['lng'])
        restaurantes +='}'

        if i < (len(lugares['resultado'])-1):
            restaurantes += ', '
    restaurantes += ']}'
    return restaurantes
