#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Author: whtrys
Email: whtrys@163.com
Description: 与百度 api 对接
"""

import json
import requests
import base64


def get_access_token():
    """
    获取百度 api 的 access token
    :return: token值
    """
    # 百度文档矫正api 官网：https://cloud.baidu.com/product/ocr/document_processing
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
        'API Key', 'Secret Key'
    )

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    key = json.loads(response.text)

    return key['access_token']


def save_back(path):
    """
    推送百度api
    :param path: 推送到 api 的图片文件的位置
    :return: 返回的校正后的图片的二进制数据
    """
    request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/doc_crop_enhance'

    with open(path, 'rb') as f:
        img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = get_access_token()
    request_url = request_url + '?access_token=' + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    # 返回图片的二进制数据
    img = base64.b64decode(response.json()['image_processed'])

    return img
