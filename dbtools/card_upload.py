'''
此文件用于下载hearthstoneJSON上的卡牌图片并上传到知晓云OSS中
'''
import sys
import os
import glob

import urllib.request
from urllib.request import urlretrieve
from HearthStoneStationBackend.settings import BASE_DIR
from dbtools.iFanr import iFanr

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HearthStoneStationBackend.settings")

import django
django.setup()

from cards.models import HSCards

# category_id: 上传文件的所属分类，格式为文件分类的 ID 数组
tile_category_id = '5ca6d9ab2855795d62b2728c' # '5c7b53390f978c6e00e864fe'
card_category_id = '5ca6d9a32855795d54b26d4e'

cardsBaseURL512 = 'https://art.hearthstonejson.com/v1/render/latest/zhCN/256x/'
cardsTileURL = 'https://art.hearthstonejson.com/v1/tiles/'
cardsOrigURL = 'https://art.hearthstonejson.com/v1/256x/'

ifanr = iFanr()
imagePath = os.path.join(BASE_DIR, 'media/images')
queryset = HSCards.objects.all().order_by('cost')
# queryset = HSCards.objects.filter(set__ename='DALARAN')
# queryset = HSCards.objects.filter(hsId='BOT_700')
for card in queryset:
    hsId = card.hsId
    # 原始图片URL
    cardURL = cardsBaseURL512+card.hsId+'.png'
    origURL = cardsOrigURL+card.hsId+'.jpg'
    tileURL = cardsTileURL+card.hsId+'.png'
    # 图片存放路径
    cardPath = '{}/cards-temp/{}.png'.format(imagePath, card.hsId)
    origPath = '{}/origs/{}.jpg'.format(imagePath, card.hsId)
    tilePath = '{}/cards-thumb0606/{}.jpg'.format(imagePath, card.hsId)
    # 生成目标地址
    cardDict = {'url': cardURL, 'path': cardPath}
    origDict = {'url': origURL, 'path': origPath}
    tileDict = {'url': tileURL, 'path': tilePath}
    # 生成知晓云OSS目标字典
    cardIfanrDict = {'category_id': card_category_id, 'path': cardPath, 'name': card.hsId + '.png',
                     'filed': 'img_card_link'}
    tileIfanrDict = {'category_id': tile_category_id, 'path': tilePath, 'name': card.hsId + '.png',
                     'filed': 'img_tile_link'}


    # 下载图片
    opener = urllib.request.build_opener()
    opener.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36')]
    urllib.request.install_opener(opener)
    # 这里需要跟前后一致，tileURL对应tilePath，cardURL对应cardPath
    for item in [cardDict, ]:
        if os.path.exists(item['path']) == False:
            try:
                urlretrieve(item['url'], item['path'])
                print('finish download:', card.name, item['path'])
            except urllib.error.URLError as e:
                print('error: ', card.name)
                print(e)
        else:
            print('{} img exists, path:{}'.format(card.name, item['path']))

    # 压缩图片


    # 上传到知晓云
    # 这里需要跟前后一致，tilePath对应img_tile_link，cardPath对应img_card_link
    # for item in [tileIfanrDict,]:
    #     # 过滤掉filed相应字段中已有值的卡牌，即已经关联图片路径的卡牌
    #     if getattr(card, item['filed']) is None or len(getattr(card, item['filed']))<=0:
    #         link = ifanr.upload_file(item['name'], item['category_id'], item['path'])
    #         setattr(card, item['filed'], link)
    #         # card.img_tile_link = link
    #         card.save()
    #         print('save img', card.name, link)
    #     else:
    #         print('{} filed exist:{}'.format(item['filed'], getattr(card, item['filed'])))