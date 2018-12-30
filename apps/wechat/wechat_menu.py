# -*- coding: utf-8 -*-
import requests
import json
import time


class Wechat(object):
    def __init__(self):
        self.token = 'hsreport0407'
        self.appID = 'wxe907c887563b14e0'
        self.appsecret = 'fefa69cc8b614fbcece20a60b4865b17'
        self.accessToken = None
        self.expiresTime = None
        self.create_menu_url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN'

    def getAccessToken(self):
        if self.accessToken is None or time.time()>self.expiresTime:
            url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (self.appID, self.appsecret)
            response = requests.get(url)
            result = json.loads(response.content)
            print(result)
            expires_in = result.get('expires_in')
            self.accessToken = result.get('access_token')
            self.expiresTime = time.time()+((expires_in-60)*1000)
        return self.accessToken

    def createMenu(self, menuJson):
        access_token = self.getAccessToken()
        url = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % access_token
        response = requests.post(url, data=menuJson)
        result = json.loads(response.content)
        print(result)


if __name__ == "__main__":
    menu = Wechat()
    menuJson = {
        "button": [
            {
                "type": "click",
                "name": "测试",
                "key": "V1001_TODAY_MUSIC"
            },
            {
                "name": "菜单",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "搜索",
                        "url": "http://www.soso.com/"
                    },
                    {
                        "type": "click",
                        "name": "赞一下我们",
                        "key": "V1001_GOOD"
                    }]
            }]
    }
    # data = json.dumps(menuJson, ensure_ascii=False)
    menu.createMenu(menuJson=menuJson)