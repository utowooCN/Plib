from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

import json
import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)


app = Flask(__name__)
bootstrap = Bootstrap(app)

# 设置用户属性, 包括secret_id, secret_key, region
# appid已在配置中移除,请在参数Bucket中带上appid。Bucket由bucketname-appid组成
secret_id = 'AKIDFKEvPgEcGhvxmOJAG9oHYcU9ew1vZ9Uc'     # 替换为用户的secret_id
secret_key = '4xe8PdhYLwNcffbLvISQ9dv99vSr30iD'     # 替换为用户的secret_key
region = 'ap-hongkong'    # 替换为用户的region
token = None               # 使用临时秘钥需要传入Token，默认为空,可不填
scheme = 'https'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)

booklist_names = []
marker = ""
while True:
    response = client.list_objects(
        Bucket='plib-1252875454',
        Marker=marker
    )
    print(response['Contents'][0])

    booklist_names.append(response['Contents'][0]['Key'])
    if response['IsTruncated'] == 'false':
        break
    marker = response['NextMarker']


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index.html')
def index_page():
    return render_template('index.html', booklist=booklist_names)


@app.route('/testbootstrap.html')
def base_page():
    return render_template('testbootstrap.html', name='bootstrap')


if __name__ == '__main__':
    app.run()
