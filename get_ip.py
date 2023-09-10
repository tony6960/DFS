import requests

def getip(from_addr):
    if from_addr == '1':
        url = 'http://ip.42.pl/raw'
    elif from_addr == '2':
        url = 'http://icanhazip.com'
    elif from_addr == '3':
        url = 'http://ipinfo.io/ip'
    elif from_addr == '4':
        url = 'http://ip.3322.net'
    elif from_addr == '5':
        url = 'http://myip.ipip.net'
    elif from_addr == '6':
        url = 'http://www.trackip.net/ip'
    r = requests.get(url)
    return r.text


print(getip(input("choose a ip source:")))