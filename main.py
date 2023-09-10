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
    # 通过IAM获取token
    IAM_TOKEN = iam_set.get_token(cloud_service_provider)
    print(IAM_TOKEN)