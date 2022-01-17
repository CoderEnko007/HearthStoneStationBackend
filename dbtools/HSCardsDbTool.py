import sys
import os
import json
import requests
import copy
from datetime import datetime
from dbtools.iFanr import iFanr
from django.db.models import Q

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HearthStoneStationBackend.settings")

import django
django.setup()
from django.forms.models import model_to_dict

ifanr = iFanr()

from cards.models import HSCards, Series

filter_id = ['BAR_539', 'SW_315', 'BAR_320', 'AV_255', 'SW_090', 'SW_003', 'CS3_008', 'AV_137', 'BT_733', 'AV_113',
             'DED_515', 'AV_200', 'BAR_546']

def add_zh_info(data):
    for item in data:
        # if not ((item.get('cardClass', '') == 'DEMONHUNTER')):
        #     continue
        # if item.get('collectible', False) == False:
        #     continue
        # if not item.get('set', '') == 'HERO_SKINS':
        #     continue
        # if not item.get('set', '') == 'ALTERAC_VALLEY':
        #     continue
        if item.get('id') not in filter_id:
            continue
        # if not (item.get('cardClass') == 'DEMONHUNTER' or item.get('set') == 'BLACK_TEMPLE' or item.get('set') == 'DEMON_HUNTER_INITIATE'):
        #     continue
        # if not item.get('id') == 'YOP_015':
        #     continue
        filter_card = HSCards.objects.filter(hsId=item['id'])
        if filter_card:
            card = filter_card[0]
        else:
            card = HSCards()
        card.dbfId = item.get('dbfId')
        if not card.dbfId:
            continue
        card.hsId = item.get('id')
        card.name = item.get('name')
        card.cost = item.get('cost')
        card.attack = item.get('attack')
        card.health = item.get('health')
        card.cardClass = item.get('cardClass', '').capitalize()
        if card.cardClass == 'Demonhunter':
            card.cardClass = 'DemonHunter'
        multiClassGroup = []
        if item.get('classes'):
            for clazz in item.get('classes'):
                formatClazz = clazz.capitalize() if clazz.lower() != 'demonhunter' else 'DemonHunter'
                multiClassGroup.append(formatClazz)
        card.classes = multiClassGroup
        card.rarity = item.get('rarity', '')
        card.type = item.get('type')
        card.race = item.get('race')
        card.mechanics = item.get('mechanics')
        card.flavor = item.get('flavor')
        card.text = item.get('text')
        card.artist = item.get('artist')
        card.collectible = item.get('collectible', False)
        card.entourage = item.get('entourage')
        card.howToEarn = item.get('howToEarn')
        card.howToEarnGolden = item.get('howToEarnGolden')
        card.update_time = datetime.now()

        set_ename = item.get('set')
        set = Series.objects.filter(ename=set_ename)
        if set:
            card.set = set[0]
        card.save()
        print('save:', item.get('name'))

def add_en_info(data):
    # 补充英文信息
    for item in data:
        # if item.get('id') not in filter_id:
        #     continue
        # if not ((item.get('cardClass', '') == 'PRIEST') and (item.get('set', '') == 'CORE' or item.get('set', '') == 'EXPERT1')):
        #     continue
        # if item.get('collectible', False) == False:
        #     continue
        # if not item.get('set', '') == 'HERO_SKINS':
        #     continue
        if not item.get('set', '') == 'ALTERAC_VALLEY':
            continue
        # if not (item.get('cardClass') == 'DEMONHUNTER' or item.get('set') == 'BLACK_TEMPLE' or item.get('set') == 'DEMON_HUNTER_INITIATE'):
        #     continue
        # if not item.get('id') == 'BAR_080':
        #     continue
        filterCard = HSCards.objects.filter(hsId=item['id'])
        print('hsId:', item['id'])
        if len(filterCard)>0:
            card = filterCard[0]
            card.ename = item['name']
            card.eflavor = item.get('flavor')
            card.save()
            print('update:', item.get('name'))

def valid_fbi_card():
    cardList = []
    # with open('valid_card_id.txt', 'r') as f:
    #     line = f.readline().strip()
    #     while line:
    #         hsId = line.split(",")
    #         for item in hsId:
    #             if item not in cardList:
    #                 cardList.append(item)
    #         line = f.readline().strip()
    #
    # with open('format_card_id.txt', 'w') as f:
    #     f.write('\n'.join(cardList))

    with open('format_card_id.txt', 'r') as f:
        line = f.readline().strip()
        while line:
            cardList.append(line)
            line = f.readline().strip()

    for item in HSCards.objects.all():
        if item.hsId not in cardList:
            item.invalid = True
            item.save()
            print('{},{} invalid'.format(item.name,item.hsId))
        else:
            item.invalid = False
            item.save()
            print('{} valid'.format(item.name))

def fill_entourage(data):
    for item in data:
        filterCard = HSCards.objects.filter(Q(hsId__contains=item.hsId), Q(invalid=False), ~Q(hsId=item.hsId), ~Q(type='ENCHANTMENT'))
        list = []
        for card in filterCard:
            list.append(card.hsId)
        if len(list)>0:
            print(item.name, list)
            item.entourage = json.dumps(list)
            item.save()
        else:
            item.entourage = None
            item.save()
        # else:
        #     item.entourage = None
        #     item.save()
    pass

def fill_entourage_audio(data):
    for item in data:
        print(item)
        entourage = json.loads(item.entourage.replace('\'', '"'))
        audio_play_en = json.loads(item.audio_play_en) if item.audio_play_en != '' and item.audio_play_en else None
        audio_attack_en = json.loads(item.audio_attack_en) if item.audio_attack_en != '' and item.audio_attack_en else None
        audio_death_en = json.loads(item.audio_death_en) if item.audio_death_en != '' and item.audio_death_en else None
        audio_trigger_en = json.loads(item.audio_trigger_en) if item.audio_trigger_en != '' and item.audio_trigger_en else None
        audio_play_zh = json.loads(item.audio_play_zh) if item.audio_play_zh != '' and item.audio_play_zh else None
        audio_attack_zh = json.loads(item.audio_attack_zh) if item.audio_attack_zh != '' and item.audio_attack_zh else None
        audio_death_zh = json.loads(item.audio_death_zh) if item.audio_death_zh != '' and item.audio_death_zh else None
        audio_trigger_zh = json.loads(item.audio_trigger_zh) if item.audio_trigger_zh != '' and item.audio_trigger_zh else None
        audio_dict = {
            'audio_play_en': audio_play_en,
            'audio_attack_en': audio_attack_en,
            'audio_trigger_en': audio_trigger_en,
            'audio_death_en': audio_death_en,
            'audio_play_zh': audio_play_zh,
            'audio_attack_zh': audio_attack_zh,
            'audio_trigger_zh': audio_trigger_zh,
            'audio_death_zh': audio_death_zh
        }
        for hsId in entourage:
            for (k, v) in audio_dict.items():
                if v is None:
                    continue
                list = []
                for audio in v[:]:
                    if hsId+'_' in audio:
                        list.append(audio)
                        v.remove(audio)
                card = HSCards.objects.filter(hsId=hsId)[0]
                if len(list)>0 and hasattr(card, k):
                    setattr(card, k, json.dumps(list))
                    card.save()
                    setattr(item, k, json.dumps(v) if v is not None and len(v)>0 else '')
                    item.save()
    pass

def update_local_cards():
    # 录入卡牌信息
    # f = open('cards.json', encoding='utf-8')
    # data = json.load(f)
    # add_zh_info(data)

    # 补充英文信息
    # f = open('cards_enUS.json', encoding='utf-8')
    # data = json.load(f)
    # add_en_info(data)
    #
    # # 从fbigame中读取有效卡牌
    # # valid_fbi_card()
    #
    # 补全衍生卡
    data = HSCards.objects.filter(Q(collectible=True) & Q(invalid=False) & Q(set__ename='ALTERAC_VALLEY'))
    # data = HSCards.objects.filter(Q(collectible=True) & Q(invalid=False) & Q(hsId='SCH_199'))
    # data = HSCards.objects.filter(Q(collectible=True) & Q(invalid=False) & Q(hsId__in=filter_id))
    fill_entourage(data)

    data = HSCards.objects.filter(Q(collectible=True) & Q(entourage__isnull=False)
                                  & Q(set__ename='ALTERAC_VALLEY'))
    fill_entourage_audio(data)

    # 衍生卡中的双引号改成单引号
    data = HSCards.objects.filter(Q(entourage__isnull=False) & Q(set__ename='ALTERAC_VALLEY'))
    for item in data:
        item.entourage = item.entourage.replace('\"', '\'')
        item.save()

def update_ifanr_cards():
    # local_cards = HSCards.objects.filter(artist__isnull=False)
    # local_cards = HSCards.objects.filter(Q(name='攻城恶魔') | Q(name='野性赐福') | Q(name='正义') | Q(name='光明之翼') | Q(name='大检查官怀特迈恩')
    #                                      | Q(name='贫瘠之地饲养员') | Q(name='军情七处渗透者') | Q(name='奥术吞噬者') | Q(name='圣光闪耀'))
    # local_cards = HSCards.objects.filter(Q(name='大铡蟹') | Q(name='泽尔，暗影斗篷'))
    # local_cards = HSCards.objects.filter(set__ename='HERO_SKINS')
    local_cards = HSCards.objects.filter(set__ename='ALTERAC_VALLEY')
    # local_cards = HSCards.objects.filter(name='发掘潜力')
    # local_cards = HSCards.objects.filter(Q(hsId='YOP_015'))
    # local_cards = HSCards.objects.filter(hsId__in=filter_id)
    # local_cards = HSCards.objects.filter(Q(cardClass='PRIEST') & (Q(set__ename='CORE') | Q(set__ename='EXPERT1')))
    # local_cards = HSCards.objects.filter(cardClass='DEMONHUNTER')
    print(len(local_cards))

    for card in local_cards:
        card_dict = model_to_dict(card)
        if card_dict.get('entourage', ''):
            card_dict['entourage'] = eval(card_dict['entourage'])
        if card_dict.get('classes', ''):
            card_dict['multiClass'] = eval(card_dict['classes'])
        card_dict['set_id'] = card_dict['set']
        card_dict['name'] = card_dict['name']
        del card_dict['create_time']
        del card_dict['update_time']
        query = {
            'where': json.dumps({
                'dbfId': {'$eq': card_dict['dbfId']}
            })
        }
        res = ifanr.get_table_data(tableID=ifanr.tablesID['hsCard'], query=query)
        if res['meta']['total_count'] > 0:
            ifanr_card = res.get('objects')[0]
            res = ifanr.put_table_data(tableID=ifanr.tablesID['hsCard'], id=ifanr_card['id'], data=card_dict)
        else:
            res = ifanr.add_table_data(tableID=ifanr.tablesID['hsCard'], data=card_dict)
        print('update_ifanr_cards {0}: {1}'.format(card_dict['name'], res))

def test():
    query = {
        'where': json.dumps({
            'cardClass': {'$eq': 'Demonhunter'}
        })
    }
    res = ifanr.get_table_data(tableID=76131, query=query)
    if res['meta']['total_count'] > 0:
        for item in res['meta']['objects']:
            item['cardClass'] = 'DemonHunter'
            res = ifanr.put_table_data(tableID=76131, id=item['id'], data=item)

    print(res)

if __name__ == '__main__':
    update_local_cards()
    # 记住去掉“回归”下的代码
    update_ifanr_cards()
    # test()
