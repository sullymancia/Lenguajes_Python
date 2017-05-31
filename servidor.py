from flask import route, run, post, request, HTTPResponse
from PIL import Image
import sys
import googlemaps
import json
import base64

from ejer1 import get_ruta
@post('ejer1')

#Ejercicio 1
def ejer1():
    print "ejer1"

    body = request.body.read()
    print type(body)

    direccion = json.loads(body)
    origen = direccion['origen']
    destino = direccion['destino']

    print origen
    print destino
    JsonValue = json.loads(routes)
    routes = get_route(origen, destino)

    ValorRetorno = json.dumps(JsonValue, sort_keys=True, indent=4)
    return HTTPResponse(status=200, body = ValorRetorno)

#Ejercicio 2
from ejer2 import get_restaurantes
@post('ejer2')
def ejer2():
    print "ejer2"

    body = request.body.read()
    print type(body)

    direccion = json.loads(body)
    origen = direccion['origen']

    print origen

    gmaps = googlemaps.Client(key='AIzaSyDxjE_B2p2t199wTZPwBErRiOmaqL1hkhM')
    resultadoDireccion = gmaps.direccion(origen, origen, mode="driving")

    lat = resultadoDireccion[0]['bounds']['northeast']['lat']
    lng = resultadoDireccion[0]['bounds']['northeast']['lng']

    restaurantes = get_restaurantes(lat, lng)
    JsonValue = json.loads(restaurantes)

    ValorRetorno = json.dumps(JsonValue, sort_keys=True, indent=4)
    return HTTPResponse(status=200, body=ValorRetorno)

#Ejercicio 3
from ejer3 import blanco_negro
@post('ejer3')
def ejer3():
    print "ejer3"

    body = request.body.read()
    print type(body)

    direccion = json.loads(body)
    print 'Ok!'

    nombre = direccion['nombre']
    data = direccion['data']
    print nombre
    print data

    blancoNegro = blanco_negro(nombre, data)
    JsonValue = json.loads(blancoNegro)

    ValorRetorno = json.dumps(JsonValue,sort_keys=True, indent=4)
    return HTTPResponse(status=200, body=ValorRetorno)

#Ejercicio 4
from ejer4 import Resize
@post('ejer4')
def ejer4():
    print "ejer4"

    body = request.body.read()
    print type(body)

    direccion = json.loads(body)
    print 'Ok!'

    nombre = direccion['nombre']
    data = direccion['data']
    lat = direccion['Tam']['alto']
    lng = direccion['Tam']['ancho']
    print nombre
    print data
    print lat
    print lng

    deco = data.decode('base64', 'strict')
    with open(nombre, 'wb') as f:
        f.write(deco)

    img = Image.open(nombre)
    lat_lng = img.size

    if lat < int(lat_lng[0]) and lng < int(lat_lng[1]):
        Resize(img, (lat, lng), True, nombre)
        with open(nombre, "rb") as f:
            imgOpen = f.read()
        enco = imgOpen.encode('base64', 'strict')
        enco = base64.b64encode(bytes(enco),"utf-8")

        resultJson = '{\"nombre\":\"'+nombre+'\",\"data\":\"'+enco+'\"}'
        JsonValue = json.loads(resultJson)
        ValorRetorno = json.dumps(JsonValue,sort_keys=True, indent=4)
        return HTTPResponse(status=200, body=ValorRetorno)
    msg = '{\"error\":\"El tam es mayor al de la imagen\"}'
    return HTTPResponse(status=400, body=msg)

run(host='0.0.0.0', port=7777, debug=True)
