# -*- coding: utf-8 -*-
import time
import hashlib
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# 微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法
import xml.etree.ElementTree as ET

TOKEN = 'hsreport0407'

class WeChat(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(WeChat, self).dispatch(*args, **kwargs)

    # URL接入校验
    def get(self, request):
        # 接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        # 服务器配置中的token
        token = TOKEN
        # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist]).encode('utf-8')
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
            print('授权成功')
            return HttpResponse(echostr)
        else:
            print('授权失败')
            return HttpResponse("failed")

    def post(self, request):
        xmlData = ET.fromstring(request.body)
        inMsg = InMsgEntity(xmlData)

        if inMsg.MsgType == 'event':
            # 关注事件
            if inMsg.Event == 'subscribe':
                content = "公众号还在开发中[Facepalm]，敬请期待！有什么问题可以直接在这里留言[Smirk]"
                replyMsg = OutMsgEntity(inMsg, content)
                return replyMsg.send()
        elif inMsg.MsgType == 'text':
            print(inMsg.Content)
            content = "收到"
            replyMsg = OutMsgEntity(inMsg, content)
            return replyMsg.send()
        elif inMsg.MsgType == 'image':
            content = "图片已收到,谢谢"
            replyMsg = OutMsgEntity(inMsg, content)
            return replyMsg.send()
        elif inMsg.MsgType == 'voice':
            content = "语音已收到,谢谢"
            replyMsg = OutMsgEntity(inMsg, content)
            return replyMsg.send()
        elif inMsg.MsgType == 'video':
            content = "视频已收到,谢谢"
            replyMsg = OutMsgEntity(inMsg, content)
            return replyMsg.send()
        elif inMsg.MsgType == 'shortvideo':
            content = "小视频已收到,谢谢"
            replyMsg = OutMsgEntity(inMsg, content)
            return replyMsg.send()
        elif inMsg.MsgType == 'location':
            content = "位置已收到,谢谢"
            replyMsg = OutMsgEntity(inMsg, content)
            return replyMsg.send()
        else:
            inMsg.MsgType == 'link'
            content = "链接已收到,谢谢"
            replyMsg = OutMsgEntity(inMsg, content)
            return replyMsg.send()


class InMsgEntity(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text if xmlData.find('ToUserName') is not None else None
        self.FromUserName = xmlData.find('FromUserName').text if xmlData.find('FromUserName') is not None else None
        self.CreateTime = xmlData.find('CreateTime').text if xmlData.find('CreateTime') is not None else None
        # text/image/voice/video/shortvideo/link/event
        self.MsgType = xmlData.find('MsgType').text if xmlData.find('MsgType') is not None else None
        self.MsgId = xmlData.find('MsgId').text if xmlData.find('MsgId') is not None else None

        #subscribe订阅，unsubscribe取消订阅，CLICK点击菜单
        self.Event = xmlData.find('Event').text if xmlData.find('Event') is not None else None
        #菜单的key值
        self.EventKey = xmlData.find('EventKey').text if xmlData.find('EventKey') is not None else None
        #接收到的文本信息内容
        self.Content = xmlData.find('Content').text if xmlData.find('Content') is not None else None
        self.PicUrl = xmlData.find('PicUrl').text if xmlData.find('PicUrl') is not None else None
        self.MediaId = xmlData.find('MediaId').text if xmlData.find('MediaId') is not None else None


class OutMsgEntity(InMsgEntity):
    def __init__(self, inMsg, content, msgType='text'):
        self.__dict = dict()
        self.__dict['ToUserName'] = inMsg.FromUserName
        self.__dict['FromUserName'] = inMsg.ToUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
        self.__dict['MsgType'] = msgType

    def send(self):
        if self.__dict['MsgType'] == 'text':
            XmlForm = """
            <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
            response = XmlForm.format(**self.__dict)
            return HttpResponse(response)
        else:
            return HttpResponse('')