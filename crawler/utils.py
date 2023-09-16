import socket
import requests
import os

def getIpByDomainName(dn):
    return socket.gethostbyname(dn)


def getGeoData(ip):
    r = requests.get('https://geolocation-db.com/json/{}/{}'.format(os.getenv('GEOAPI_KEY'), ip))
    return r.json()
