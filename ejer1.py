import json
import BaseHTTPServer
import BaseHTTPRequestHandler
import requests
import re
import collections
import struct
import base64
import googlemaps

def get_ruta(origen, destino):

    gmaps = googlemaps.Client(key='AIzaSyDxjE_B2p2t199wTZPwBErRiOmaqL1hkhM')

    resultadoDireccion = gmaps.directions(origen, destino, mode="driving")

    transform = json.dumps(resultadoDireccion)
    print type(transform)

    resultado = re.search('\"Fin_localizacion\"(.*)', transform)
    if resultado:
        encontro = result.group(1);

    final = found.split('\"Fin_localizacion\"')
    completo = []
    resultadoJson = []
    for i in range(0,len(final)):
        temp = final[i]
        completo.append(temp[2:43])

    for i in range(0, len(completo)):
        print completo[i]
        temp2 = completo[i]
        for j in range(0, len(temp2)):
            if temp2[j] == '}':
                if j+1 < len(temp2):
                    resultadoJson.append(temp2[:(j+1)])
                    print j
                    break

            elif j+1 >= len(temp2):
                resultadoJson.append((temp2+'}'))
                print j
                break

    cadenaJson = '{ \"ruta\":[ '
    for i in range(0, len(resultadoJson)):
        if i < (len(resultJ)-1):
            cadenaJson += resultadoJson[i]+ ', '
        else:
            cadenaJson += resultadoJson[i]

    cadenaJson += ']}'

    return cadenaJson
