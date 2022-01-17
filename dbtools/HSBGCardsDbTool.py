import sys
import os
import json
import requests
import copy
from dbtools.iFanr import iFanr
from django.db.models import Q
from urllib import parse
from ast import literal_eval

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HearthStoneStationBackend.settings")

import django

django.setup()
from django.forms.models import model_to_dict

ifanr = iFanr()

from cards.models import HSBattleGroundCards, HSCards

updatedCard = []


def get_cards_list(url):
    res = requests.get(url, verify=False)
    return res.json()


def gen_cards_list(card_list, recursion=True):
    for item in card_list:
        # if not item.get('minionTypeId', '') == 24:
        #     continue
        filter_card = HSBattleGroundCards.objects.filter(hsId=item['id'])
        if filter_card:
            card = filter_card[0]
        else:
            card = HSBattleGroundCards()
        print('save start:', item.get('name'), item.get('id'))
        card.hsId = item.get('id')
        card.name = item.get('name')
        temp_card = HSCards.objects.filter(dbfId=item['id'])
        if temp_card:
            card.ename = temp_card[0].ename
        else:
            temp_card = HSCards.objects.filter(name=item['name'])
            if temp_card:
                card.ename = temp_card[0].ename
            else:
                card.ename = ''
        card.entourageID = item.get('childIds')
        card.cost = item.get('manaCost')
        card.attack = item.get('attack')
        card.health = item.get('health')
        card.outTier = item.get('tier')
        card.minionType = item.get('minionTypeId')
        card.rarityID = item.get('rarityID')
        card.setID = item.get('cardSetId')
        card.typeID = item.get('cardTypeId')
        card.parentID = item.get('parentId')
        card.keywords = item.get('keywordIds')
        card.flavor = item.get('flavorText')
        card.text = item.get('text')
        card.artist = item.get('artistName')
        card.collectible = item.get('collectible')
        battlegrounds = item.get('battlegrounds')
        if battlegrounds is None:
            print('{}:battlegrounds is None'.format(item['name']))
            continue
        card.tier = battlegrounds.get('tier') if battlegrounds else ''
        card.hero = battlegrounds.get('hero') if battlegrounds else 0
        card.image = battlegrounds.get('image') if battlegrounds else ''
        card.gold_image = battlegrounds.get('imageGold') if battlegrounds else ''
        card.upgradeID = battlegrounds.get('upgradeId') if battlegrounds else ''
        if not card.image:
            card.image = item.get('image')
        if not card.gold_image:
            card.gold_image = item.get('imageGold')

        # 衍生卡和英雄技能卡
        if len(card.entourageID) and card.parentID is None and recursion:
            params = parse.urlencode({
                'ids': ','.join([str(i) for i in card.entourageID]),
                'tier': 'all',
                'pageSize': 300,
                'locale': 'zh_cn'
            })
            url = 'http://hs.blizzard.cn/action/hs/cards/battlegrounds?{}'.format(params)
            print('url:', url)
            res = requests.get(url, verify=False)
            format_data = res.json()
            if format_data['cardCount']:
                gen_cards_list(format_data['cards'], False)

        # 三连升级卡牌
        if card.upgradeID is not None:
            params = parse.urlencode({
                'ids': card.upgradeID,
                'tier': 'all',
                'pageSize': 300,
                'locale': 'zh_cn'
            })
            url = 'https://hs.blizzard.cn/action/hs/cards/battlegrounds?{}'.format(params)
            res = requests.get(url, verify=False)
            format_data = res.json()
            if format_data['cardCount']:
                gen_cards_list(format_data['cards'])

        card.save()
        updatedCard.append(card.hsId)
        print('save end:', item.get('name'), updatedCard)


def update_ifanr_cards():
    local_cards = HSBattleGroundCards.objects.filter(hsId__in=updatedCard)
    print(updatedCard, len(local_cards))
    for card in local_cards:
        card_dict = model_to_dict(card)
        del card_dict['id']
        card_dict['hsId'] = int(card_dict['hsId'])
        card_dict['minionType'] = int(card_dict['minionType']) if card_dict['minionType'] else None
        card_dict['entourageID'] = literal_eval(card_dict['entourageID']) if card_dict['entourageID'] else None
        card_dict['keywords'] = literal_eval(card_dict['keywords']) if card_dict['keywords'] else None
        del card_dict['create_time']
        query = {
            'where': json.dumps({
                'hsId': {'$eq': int(card_dict['hsId'])}
            })
        }
        res = ifanr.get_table_data(tableID=ifanr.tablesID['bgsCard'], query=query)
        if res['meta']['total_count'] > 0:
            ifanr_card = res.get('objects')[0]
            res = ifanr.put_table_data(tableID=ifanr.tablesID['bgsCard'], id=ifanr_card['id'], data=card_dict)
        else:
            res = ifanr.add_table_data(tableID=ifanr.tablesID['bgsCard'], data=card_dict)
        print('update_ifanr_cards {0}: {1}'.format(card_dict['name'], res))
    pass


if __name__ == '__main__':
    # bgCardsUrl = 'http://hs.blizzard.cn/action/hs/cards/battleround?tier=all&type=minion%2Chero&collectible=0%2C1&pageSize=200&locale=zh_cn'
    # bgCardsUrl = 'http://hs.blizzard.cn/action/hs/cards/battleround?sort=tier&order=asc&type=minion&tier=all&viewMode=grid&collectible=0%2C1&pageSize=200&locale=zh_cn'
    # bgCardsUrl = 'https://hs.blizzard.cn/action/hs/cards/battleround?tier=all&type=minion%2Chero&collectible=0%2C1&pageSize=300&locale=zh_cn'
    bgCardsUrl = 'https://hs.blizzard.cn/action/hs/cards/battlegrounds?type=hero%2Cminion&tier=all&collectible=0%2C1&pageSize=300&locale=zh_cn'
    data = get_cards_list(bgCardsUrl)
    list_id = [76562]
    filteredData = list(filter(lambda x: x.get('id', '') in list_id, data['cards']))
    gen_cards_list(filteredData)
    # gen_cards_list(data['cards'])
    # updatedCard = list_id
    update_ifanr_cards()
    pass
