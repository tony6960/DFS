import requests


def get_record_id(zone_id, IAM_TOKEN):
    headers = {
        'X-Auth-Token': IAM_TOKEN
    }
    record_id = requests.get('https://dns.myhuaweicloud.com/v2/zones/' + zone_id + '/recordsets', headers=headers)
    # 提取所有record的id和name并输出
    for record in record_id.json()['recordsets']:
        print(record['id'], record['name'])


def change_dns(zone_id, record_id, IAM_TOKEN, ip):
    url = 'https://dns.myhuaweicloud.com/v2/zones/' + zone_id + '/recordsets/' + record_id
    headers = {
        'Content-Type': 'application/json;charset=utf8',
        'X-Auth-Token': IAM_TOKEN
    }
    data = {
        "name": "www.example.com.",
        "description": "This is an example record set.",
        "type": "A",
        "ttl": 3600,
        "records": ip
    }
    r = requests.put(url, headers=headers, json=data)


def creat_dns(zone_id, IAM_TOKEN, ip):
    url = 'https://dns.myhuaweicloud.com/v2/zones/' + zone_id + '/recordsets'
    headers = {
        'X-Auth-Token': IAM_TOKEN
    }
    data = {
        "name": "dns.example.com.",
        "description": "made by DFS",
        "type": "A",
        "ttl": 3600,
        "records": ip
    }
    r = requests.post(url, headers=headers, json=data)