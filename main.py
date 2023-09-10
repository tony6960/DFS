import get_ip
import zone_set
import configuration
import iam_set
import record
import datetime
import time

if __name__ == '__main__':
    # 定义IP获取地址源
    from_url = configuration.get_ip_from()
    ip = ""
    if from_url == 'json':
        get_ip.getip_json()
    else:
        print('正在检查IP获取源是否可用...')
        ip = get_ip.getip(from_url)
        print(f'IP获取源可用，当前IP为{ip}')
    # 定义刷新间隔
    sleep_time = configuration.get_sleep_time()
    # 定义云服务商
    cloud_service_provider = configuration.get_cloud_service_provider()
    key = input('是否有现成的IAM密钥？(y/n)')
    if key == 'y':
        IAM_TOKEN = input('请输入IAM密钥：')
    else:
        # 通过IAM获取token
        IAM_TOKEN = iam_set.get_token(cloud_service_provider)
        # 展示所有zone并获取zone_id
    zone_set.get_zone_id(cloud_service_provider, IAM_TOKEN)
    zone_id = input('请输入对应域名的ID：')
    dns = input('你是否有现成的记录集？(y/n)')
    record_id = ""
    domain = ""
    if dns == 'y':
        # 展示所有record并获取record_id
        record.get_record_id(zone_id, IAM_TOKEN)
        record_id = input('请输入对应记录的ID：')
    else:
        # 创建记录集
        domain = input('请输入域名：')
        record.creat_dns(zone_id, IAM_TOKEN, ip, domain)
    # 进入循环，修改记录集
    # 校验所有参数
    print('请确认所有参数：')
    print(f'IP获取源：{from_url}')
    print(f'刷新间隔：{sleep_time}')
    print(f'云服务商：{cloud_service_provider}')
    print(f'域名ID：{zone_id}')
    print(f'记录ID：{record_id}')
    print(f'IAM密钥：{IAM_TOKEN}')
    print(f'域名：{domain}')
    print(f'IP：{ip}')
    print('请确认以上参数，确认无误后按回车键继续')
    input()
    while True:
        ip = get_ip.getip(from_url)
        record.change_dns(zone_id, record_id, IAM_TOKEN, ip)
        time_now = str(datetime.datetime.now())
        print(f'[{time}]修改DNS为{ip}')
        # 休眠
        time.sleep(sleep_time)
