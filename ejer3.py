from PIL import Image
import json
import BaseHTTPServer
import BaseHTTPRequestHandler
import requests
import re
import collections
import struct
import base64
import googlemaps

from PIL import Image

def blanco_negro(nombre, data):
    deco = data.decode('base64', 'strict')
    with open(nombre, 'wb') as f:
        f.write(deco)

    img = Image.open(nombre)
    pixels = img.load()
    width, heigth = img.size

    print "Antes: "
    print pixels[0, 0]
    for x in range(width):
        for y in range(heigth):
            color_r = pixels[x, y][0]
            color_g = pixels[x, y][1]
            color_b = pixels[x, y][2]
            average =((color_r+color_g+color_b)/3)
            tmp = (average, average, average)
            img.putpixel((x, y), temp)
    print "Despues: "
    print pixels[0, 0]
    img.save(nombre)
    with open(nombre, "rb") as f:
        img_open = f.read()
        enco = img_open.encode('base64', 'strict')
    enco = base64.b64encode(bytes(enco),"utf-8")
    JsonResultado = '{ \"nombre\":\"'+nombre+'\", \"data\":\"'+enco+'\"}'

    print JsonResultado
    return JsonResultado
