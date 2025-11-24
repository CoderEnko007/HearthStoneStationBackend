import sys
import os
import json
import requests
import copy
from datetime import datetime
from dbtools.iFanr import iFanr
from django.db.models import Q

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HearthStoneStationBackend.settings")

import django

django.setup()
from django.forms.models import model_to_dict

ifanr = iFanr()

from cards.models import HSCards, Series

filter_id = ['FIR_959', 'EDR_979', 'GDB_100', 'TLC_446', 'TLC_426', 'TOY_800', 'VAC_427', 'EDR_817', 'TOY_521', 'TLC_818', 'TOY_606',
             'TOY_602', 'SC_019', 'VAC_330', 'TOY_354', 'BT_351', 'EX1_365', 'KAR_089']
set_ename = ['EMERALD_DREAM', 'SPACE', 'THE_LOST_CITY', 'WHIZBANGS_WORKSHOP', 'ISLAND_VACATION', 'ISLAND_VACATION', 'CORE', 'THE_SUNKEN_CITY']
# set_ename = ['TIME_TRAVEL']
set_name = 'standard'


def add_zh_info(data, cn_cards):
    for item in data:
        # if not ((item.get('cardClass', '') == 'DEATHKNIGHT')):
        #     continue
        # if item.get('set', '') not in set_ename:
        #     continue
        # if item.get('set', '') != 'PLACEHOLDER_202204':
        #     continue
        if item.get('id') not in filter_id:
            continue
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
        if card.cardClass == 'Deathknight':
            card.cardClass = 'DeathKnight'
        multiClassGroup = []
        if item.get('classes'):
            for clazz in item.get('classes'):
                if clazz.lower() == 'demonhunter':
                    formatClazz = 'DemonHunter'
                elif clazz.lower() == 'deathknight':
                    formatClazz = 'DeathKnight'
                else:
                    formatClazz = clazz.capitalize()
                # formatClazz = clazz.capitalize() if clazz.lower() != 'demonhunter' else 'DemonHunter'
                # formatClazz = clazz.capitalize() if clazz.lower() != 'deathknight' else 'DeathKnight'
                multiClassGroup.append(formatClazz)
        card.classes = multiClassGroup
        card.rarity = item.get('rarity', 'COMMON')
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
        cn_card = next((obj for obj in cn_cards if obj.get('id') == card.dbfId), None)
        card.img_card_link = cn_card['image'] if cn_card is not None else ''
        card.img_tile_link = cn_card['crop_image'] if cn_card is not None else ''
        card.update_time = datetime.now()

        if item.get('set', '') == 1810 or item.get('set', '') == 'PLACEHOLDER_202204':
            set_ename_temp = 'CORE'
        else:
            set_ename_temp = item.get('set')
        set_obj = Series.objects.filter(ename=set_ename_temp)
        if set_obj:
            card.set = set_obj[0]
        print('start save:', item.get('name'))
        card.save()
        print('end save:', item.get('name'))


def add_en_info(data):
    # 补充英文信息
    for item in data:
        # if not ((item.get('cardClass', '') == 'DEATHKNIGHT')):
        #     continue
        if item.get('id') not in filter_id:
            continue
        # if item.get('set', '') not in set_ename:
        #     continue
        filterCard = HSCards.objects.filter(hsId=item['id'])
        print('hsId:', item['id'])
        if len(filterCard) > 0:
            card = filterCard[0]
            card.ename = item['name']
            card.eflavor = item.get('flavor')
            card.save()
            print('update:', item.get('name'))


def fill_entourage(data):
    for item in data:
        if not hasattr(item, 'hsId'):
            continue
        filterCard = HSCards.objects.filter(Q(hsId__contains=item.hsId), Q(invalid=False), ~Q(hsId=item.hsId),
                                            ~Q(type='ENCHANTMENT'))
        card_list = []
        card_dbfid_list = []
        for card in filterCard:
            card_list.append(card.hsId)
            card_dbfid_list.append(card.dbfId)
        if len(card_list) > 0:
            print(item.name, card_list)
            item.entourage = json.dumps(card_list)
            res = fetch_entourage_cards({"ids": card_dbfid_list})
            entourage_cards = res['data']['list']
            for e_cn_card in entourage_cards:
                f_card = HSCards.objects.filter(dbfId=e_cn_card['id'])[0]
                f_card.img_card_link = e_cn_card['image'] if e_cn_card.get('image') else None
                f_card.save()
            item.save()
        else:
            item.entourage = None
            item.save()


def fill_entourage_audio(data):
    for item in data:
        print(item)
        entourage = json.loads(item.entourage.replace('\'', '"'))
        audio_play_en = json.loads(item.audio_play_en) if item.audio_play_en != '' and item.audio_play_en else None
        audio_attack_en = json.loads(
            item.audio_attack_en) if item.audio_attack_en != '' and item.audio_attack_en else None
        audio_death_en = json.loads(item.audio_death_en) if item.audio_death_en != '' and item.audio_death_en else None
        audio_trigger_en = json.loads(
            item.audio_trigger_en) if item.audio_trigger_en != '' and item.audio_trigger_en else None
        audio_play_zh = json.loads(item.audio_play_zh) if item.audio_play_zh != '' and item.audio_play_zh else None
        audio_attack_zh = json.loads(
            item.audio_attack_zh) if item.audio_attack_zh != '' and item.audio_attack_zh else None
        audio_death_zh = json.loads(item.audio_death_zh) if item.audio_death_zh != '' and item.audio_death_zh else None
        audio_trigger_zh = json.loads(
            item.audio_trigger_zh) if item.audio_trigger_zh != '' and item.audio_trigger_zh else None
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
                    if hsId + '_' in audio:
                        list.append(audio)
                        v.remove(audio)
                card = HSCards.objects.filter(hsId=hsId)[0]
                if len(list) > 0 and hasattr(card, k):
                    setattr(card, k, json.dumps(list))
                    card.save()
                    setattr(item, k, json.dumps(v) if v is not None and len(v) > 0 else '')
                    item.save()
    pass


def update_local_cards(cn_cards):
    # 录入卡牌信息
    f = open('cards.json', encoding='utf-8')
    cards_data = json.load(f)
    add_zh_info(cards_data, cn_cards)

    # 补充英文信息
    f = open('cards_enUS.json', encoding='utf-8')
    cards_data = json.load(f)
    add_en_info(cards_data)

    # 补全衍生卡
    # cards_data = HSCards.objects.filter(Q(collectible=True) & Q(invalid=False) & Q(set__ename__in=set_ename))
    # cards_data = HSCards.objects.filter(Q(collectible=True) & Q(invalid=False) & Q(set__ename='CORE'))
    # data = HSCards.objects.filter(Q(collectible=True) & Q(invalid=False) & Q(hsId='SCH_199'))
    cards_data = HSCards.objects.filter(Q(collectible=True) & Q(invalid=False) & Q(hsId__in=filter_id))
    # data = HSCards.objects.filter(Q(collectible=True) & Q(invalid=False) & Q(cardClass='DEATHKNIGHT'))
    fill_entourage(cards_data)

    # data = HSCards.objects.filter(Q(collectible=True) & Q(entourage__isnull=False)
    #                               & Q(set__ename='THE_SUNKEN_CITY'))
    # fill_entourage_audio(data)

    # 衍生卡中的双引号改成单引号
    # cards_data = HSCards.objects.filter(Q(entourage__isnull=False) & Q(set__ename__in=set_ename))
    # cards_data = HSCards.objects.filter(Q(entourage__isnull=False) & Q(set__ename='CORE'))
    # data = HSCards.objects.filter(Q(entourage__isnull=False) & Q(cardClass='DEATHKNIGHT'))
    for item in cards_data:
        if item.entourage is None:
            continue
        item.entourage = item.entourage.replace('\"', '\'')
        item.save()


def update_ifanr_cards():
    # local_cards = HSCards.objects.filter(set__ename__in=set_ename)
    # local_cards = HSCards.objects.filter(set__ename='CORE')
    local_cards = HSCards.objects.filter(hsId__in=filter_id)
    # local_cards = HSCards.objects.filter(Q(cardClass='PRIEST') & (Q(set__ename='CORE') | Q(set__ename='EXPERT1')))
    # local_cards = HSCards.objects.filter(cardClass='DEATHKNIGHT')
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


def fetch_hs_cards(card_set='standard'):
    url = 'https://webapi.blizzard.cn/hs-cards-api-server/api/web/cards/constructed'

    all_cards = []
    page = 1
    page_size = 200
    total = 0

    while True:
        payload = {
            "attack": -1,
            "class": "all",
            "faction": "",
            "health": -1,
            "keyword": "",
            "mana_cost": [],
            "minion_type": "",
            "page": page,
            "page_size": page_size,
            "rarity": "",
            "set": card_set,
            "sort": "manaCost:asc",
            "spell_school": "",
            "text_filter": "",
            "type": ""
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()

            # 获取总量
            if total == 0:
                total = data['data']['total']
                print('total series cards:', total)

            # 添加当前页的数据到列表中
            all_cards.extend(data['data']['list'])

            # 检查是否获取到所有数据
            if len(all_cards) >= total:
                break

            # 增加页码
            page += 1

        except requests.exceptions.RequestException as e:
            print(f"请求发生错误: {e}")
            break

    # 将所有数据保存到文件
    # with open('cn_cards.json', 'w', encoding='utf-8') as f:
    #     json.dump(all_cards, f, ensure_ascii=False, indent=2)

    return all_cards


def fetch_entourage_cards(payload):
    url = 'https://webapi.blizzard.cn/hs-cards-api-server/api//web/cards/constructed'

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {e}")
        return None


if __name__ == '__main__':
    result = fetch_hs_cards(set_name)
    # result = []
    update_local_cards(result)
    update_ifanr_cards()
    pass
