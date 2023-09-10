import requests

def getip(from_addr):
    r = requests.get(from_addr)
    return r.text