import requests
import configuration

def getip(from_addr):
    if from_addr == 'json':
        getip_json()
    else:
        try:
            r = requests.get(from_addr)
            return r.text
        except:
            print('IP地址源异常，请检查网络连接或更换IP地址源')
            exit(404)


def getip_json():
    addr = configuration.json_addr()
    key = configuration.json_key()
    print('正在检查IP获取源是否可用...')
    try:
        r = requests.get(addr)
        ip = r.json()[key]
        print(f'IP获取源可用，当前IP为{ip}')
        return ip
    except:
        print('IP地址源异常，请检查网络连接或更换IP地址源')
        exit(404)