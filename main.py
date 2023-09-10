import get_ip
import zone_set
import configuration
import iam_set


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
        # 校验IAM密钥是否有效
        iam_set.check_token(IAM_TOKEN)
    else:
        # 通过IAM获取token
        IAM_TOKEN = iam_set.get_token(cloud_service_provider)
        # 展示所有zone并获取zone_id
    zone_set.get_zone_id(cloud_service_provider, IAM_TOKEN)
    input('请输入对应域名的ID：')
    ip = get_ip.getip(from_url)
    print(ip)