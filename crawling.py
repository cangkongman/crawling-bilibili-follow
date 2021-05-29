import json
import os
import requests


headers = {
  # 用浏览器打开访问网址https://api.bilibili.com/x/relation/tags?jsonp=jsonp
  # 把request_headers复制下来，注意字典的格式
  # 如果有重新登录，cookie要换
}


# 爬取关注数量
def crawling_first():
    url = 'https://api.bilibili.com/x/relation/tags?jsonp=jsonp'

    response = requests.get(url=url, headers=headers)
    assign = response.json()

    with open('关注者数量.json', 'w', encoding='utf-8')as f:
        json.dump(assign, f, ensure_ascii=False)
        print('关注者数量.json保存成功！！！')


# 爬取关注的人
def crawling_second(path):
    if not os.path.exists(path):
        os.makedirs(path)
    url = 'https://api.bilibili.com/x/relation/followings'
    params = {
        'vmid': 289920431,
        'pn': 1,
        'ps': 20,
        'order': 'desc',
        'order_type': '',
        'jsonp': 'jsonp',
    }

    with open('关注者数量.json', 'r', encoding='utf-8')as f:
        file = json.load(f)
    count = file['data'][1]['count']
    while params['pn'] <= (count/20+1):
        headers['path'] = '/x/relation/followings?vmid=289920431&pn='+str(params['pn']) + \
                          '&ps=20&order=desc&order_type=&jsonp=jsonp'
        response = requests.get(url=url, params=params, headers=headers)
        assign = response.json()
        with open(path+str(params['pn'])+'.json', 'w', encoding='utf-8')as fp:
            json.dump(assign, fp, ensure_ascii=False)
            print(str(params['pn'])+'.json爬取成功！！！')
        params['pn'] += 1
