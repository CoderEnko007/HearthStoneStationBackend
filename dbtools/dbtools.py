import sys
import os
import json


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HearthStoneStationBackend.settings")

import django
django.setup()

from cards.models import HSCards, Series

f = open('cards.collectible.json', encoding='utf-8')
data = json.load(f)
for item in data:
    card = HSCards()
    card.hsId = item.get('id')
    card.dbfId = item.get('dbfId')
    card.name = item.get('name')
    card.cost = item.get('cost')
    card.attack = item.get('attack')
    card.health = item.get('health')
    card.cardClass = item.get('cardClass').capitalize()
    card.rarity = item.get('rarity')
    card.type = item.get('type')
    card.race = item.get('race')
    card.mechanics = item.get('mechanics')
    card.flavor = item.get('flavor')
    card.text = item.get('text')
    card.artist = item.get('artist')
    card.collectible = item.get('collectible')

    set_ename = item.get('set')
    set = Series.objects.filter(ename=set_ename)
    if set:
        card.set = set[0]
    card.save()
    print('save:', item.get('name'))

f = open('cards_collectible_enUS.json', encoding='utf-8')
data = json.load(f)
for item in data:
    card = HSCards.objects.filter(hsId=item['id'])[0]
    card.ename = item['name']
    card.save()
    print('update:', item.get('name'))

