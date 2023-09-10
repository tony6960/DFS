import get_ip
import zone_set
import configuration
import iam_set
import record


if __name__ == '__main__':
    # 定义IP获取地址源
    from_url = configuration.get_ip_from()
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
    ip = get_ip.getip(from_url)
    dns = input('你是否有现成的记录集？(y/n)')
    if dns == 'y':
        record.get_record_id(zone_id, IAM_TOKEN)
        record_id = input('请输入对应记录的ID：')
    else:
        record.creat_dns()
    record.change_dns(zone_id, record_id, IAM_TOKEN, ip)