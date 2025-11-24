import sys
import os
import json
import requests
import django
from urllib import parse
from ast import literal_eval

from dbtools.iFanr import iFanr
from django.forms.models import model_to_dict

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HearthStoneStationBackend.settings")
django.setup()

from cards.models import HSCards

ifanr = iFanr()


def get_arena_cards(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 提取<pre>标签中的内容
        import re
        pre_content = re.search(r'<pre>(.*?)</pre>', content, re.DOTALL)
        if pre_content:
            return json.loads(pre_content.group(1)).get('data')
        return None


def format_card(item):
    filtered_card = HSCards.objects.filter(hsId=item['card_id']).first()
    if not filtered_card:
        return None

    # 定义字段及其默认值
    fields = [
        ('popularity', 0),
        ('drafted_popularity', 0),
        ('redrafted_popularity', 0),
        ('avg_copies_in_deck', 0),
        ('win_rate', 0),
        ('drawn_win_rate', 0),
        ('played_win_rate', 0),
        ('num_games', 0),
        ('offer_rate', 0),
        ('offer_bin', ''),
        ('pick_rate', 0),
        ('score', 0),
        ('wd_pct_played', 0),
        ('offer_rate_rd', 0),
        ('offer_bin_rd', ''),
        ('rm_pct_draft', 0)
    ]

    # 构建结果字典
    card = {
        'dbfId': filtered_card.dbfId,
        'card_id': item.get('card_id'),
        'name': filtered_card.name,
        'cardClass': filtered_card.cardClass,
        'cost': filtered_card.cost,
        'rarity': filtered_card.rarity
    }

    # 逐个添加字段，处理None值情况
    for field, default in fields:
        value = item.get(field)
        card[field] = default if value is None else value

    return card


if __name__ == '__main__':
    html_file = os.path.join(pwd, 'arena_file.html')
    json_data = get_arena_cards(html_file)
    # print(json_data)
    for faction in json_data:
        for item in json_data[faction]:
            card = format_card(item)
