from requests.utils import dict_from_cookiejar
import requests
import json
import time
import os


def login(user, pwd):
    url = "http://crawlab.ztesa.site/api/login"
    data = {
        "username": user,
        "password": pwd
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, data=data, verify=False)
    return response.json()['data']


def totalSpiderInfos():
    
    url = "http://crawlab.ztesa.site/api/spiders"
    params = {
        "all": "true"
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    return response.json()['data']


def save(colId, path, fileName, spiderName):
    print(colId, path, fileName, spiderName)
    with open(os.path.join(os.path.dirname(__file__), f'{fileName}'), mode='r', encoding='utf-8') as f:
        code = f.read()
    url = f'http://crawlab.ztesa.site/api/spiders/{colId}/files/save'
    data = {
        "data" : code ,
        "path" : path
    }
    response = requests.post(url, headers=headers ,data=json.dumps(data))

    if 'success' in response.json()['message']:
        print(response.json()['message'] + ' --- ' + spiderName + '修改完成')
    else:
        print(response.json()['message'] + ' --- ' + spiderName + '修改失败')



if __name__ == '__main__':
    user = 'admin'
    pwd = 'admin'
    headers = {
        "Authorization" : login(user, pwd),
    }

    curDirFiles = os.listdir(os.path.join(os.path.dirname(__file__)))
    spiderInfos = totalSpiderInfos()

    for spiderInfo in spiderInfos:
        spiderCmd = spiderInfo['cmd'].split(' ')[-1]
        spiderName = spiderInfo['name']
        spiderId = spiderInfo['_id']
        for fileName in curDirFiles:
            if 'main' in fileName:
                continue
            path = f'/{spiderCmd}/{fileName}'
            save(spiderId, path, fileName, spiderName)
            time.sleep(1)