import base64
import io
import re
import sys
import json
import urllib
import requests
from lxml import etree
from bs4 import BeautifulSoup
import tkinter.messagebox


def entries(content):
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    url = 'https://baike.baidu.com/item/' + urllib.parse.quote(content)
    # 获得网页源代码
    response = urllib.request.Request(url=url, headers=headers, method='GET')
    response = urllib.request.urlopen(response)
    html = response.read().decode('utf-8')
    # 处理源代码
    html = etree.HTML(html)
    content_before = html.xpath('//div[contains(@class,"lemma-summary") or contains(@class,"lemmaWgt-lemmaSummary")]//text()')
    content = [item.strip('\n') for item in content_before]
    return ''.join(content)


def ocr(img_path: str):
    # 请求头
    headers = {
        'Host': 'cloud.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.99 Safari/537.36',
        'Accept': '*/*',
        'Origin': 'https://cloud.baidu.com',
        'Referer': 'https://cloud.baidu.com/product/ocr/general',
        'Accept-Language': 'zh-CN,en-US',
    }
    # 把图片用base64编码 
    with open(img_path, 'rb') as f:
        img = base64.b64encode(f.read())
    data = {
        'image': 'data:image/jpeg;base64,' + str(img)[2:-1],
        'image_url': '',
        'type': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
        'detect_direction': 'false'
    }
    # 调用百度云的api
    response = requests.post(
        'https://cloud.baidu.com/aidemo', headers=headers, data=data)

    # 空的列表，存储识别到的字符串
    ocr_text = []
    result = response.json()['data']
    if not result.get('words_result'):
        return []

    # 将识别的字符串添加到列表里面
    for r in result['words_result']:
        text = r['words'].strip()
        ocr_text.append(text)
    # 返回字符串列表
    return ocr_text


def translation(content):
    # 请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    # 获取网页源代码
    url = 'https://fanyi.baidu.com/sug'
    Form = {'kw': content}
    html = requests.post(url, data=Form, headers=header)
    content = json.loads(html.text)
    return content