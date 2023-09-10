import requests


def get_zone_id(provider, IAM_TOKEN):
    name = input('请输入域名：')
    if provider == 1:
        print('暂未开发')
        exit(404)
    elif provider == 2:
        url = 'https://dns.myhuaweicloud.com/v2/zones'
        headers = {
            'Content-Type': 'application/json;charset=utf8',
            'X-Auth-Token': IAM_TOKEN
        }
        r = requests.get(url, headers=headers)
        print(r.text)
        return r.text
