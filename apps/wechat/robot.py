# -*- coding: utf-8 -*-
import sys
import os

from utils import wechatConfig
from werobot import WeRoBot

from HearthStoneStationBackend.settings import BASE_DIR

robot = WeRoBot(enable_session=False,
                token=wechatConfig.token,
                APP_ID=wechatConfig.appID,
                APP_SECRET=wechatConfig.appsecret,
                ENCODING_AES_KEY=wechatConfig.encodingAESkey)
client = robot.client
client.create_menu({
    # "button":[{
    #      "type":"miniprogram",
    #      "name":"test",
    #      "url":"https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzUxMjgxNjcwNg==#wechat_redirect",
    #      "appid":"wx68185c439fa57f83",
    #      "pagepath":"pages/index/main"
    # }]
    "button":[{
         "type":"click",
         "name":"测试",
         "key":"miniprogram"
    }]
})

@robot.key_click("test_key")
def test_menu_key(message):
    return '什么都没有，测试一下而已[Facepalm]'

@robot.subscribe
def subscribe(event):
    if (event.type == 'subscribe_event'):
        return "公众号还在开发中[Facepalm]，敬请期待！有什么问题可以直接在这里留言[Smirk]"

@robot.text
def echo(message):
    print(message.content)
    return '已收到'

@robot.image
def image(message):
    print(message.img)
    return '图片已收到'