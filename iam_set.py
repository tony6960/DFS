import requests


def get_token(provider):
    iam_user = input('请输入IAM用户名：')
    iam_password = input('请输入IAM密码：')
    from_user = input('请输入IAM用户隶属于哪个用户：')
    if provider == 1:
        print('暂未开发')
        exit(404)
    elif provider == 2:
        url = 'https://iam.myhuaweicloud.com/v3/auth/tokens'
        headers = {
            'Content-Type': 'application/json;charset=utf8'
        }
        data = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "domain": {
                                "name": from_user
                            },
                            "name": iam_user,
                            "password": iam_password
                        }
                    }
                },
                "scope": {
                    "project": {
                        "name": "cn-north-4"
                    }
                }
            }
        }

        r = requests.post(url, headers=headers, json=data)
        IAM_TOKEN = r.headers['X-Subject-Token']
        return IAM_TOKEN