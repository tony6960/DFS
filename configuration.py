def get_ip_from():
    print('请配置API源：')
    print('1. http://ip.42.pl/raw')
    print('2. http://icanhazip.com')
    print('3. http://ipinfo.io/ip')
    print('4. http://ip.3322.net')
    print('5. http://myip.ipip.net')
    print('6. http://www.trackip.net/ip')
    print('7. 自定义源(有几率出现错误)')
    from_addr = input('请输入API源编号：')
    if from_addr == '1':
        return 'http://ip.42.pl/raw'
    elif from_addr == '2':
        return 'http://icanhazip.com'
    elif from_addr == '3':
        return 'http://ipinfo.io/ip'
    elif from_addr == '4':
        return 'http://ip.3322.net'
    elif from_addr == '5':
        return 'http://myip.ipip.net'
    elif from_addr == '6':
        return 'http://www.trackip.net/ip'
    elif from_addr == '7':
        return input('请输入自定义源：')
    else:
        print('输入错误，请重新输入')
        return get_ip_from()


def get_sleep_time():
    print('请输入刷新间隔（秒）：')
    sleep_time = input()
    try:
        sleep_time = int(sleep_time)
        return sleep_time
    except:
        print('输入错误，请重新输入')
        return get_sleep_time()


def get_cloud_service_provider():
    print('请选择云服务商：')
    print('1. 阿里云')
    print('2. 华为云')
    privider = input('请输入云服务商编号：')
    if privider == '1':
        return 1
    elif privider == '2':
        return 2