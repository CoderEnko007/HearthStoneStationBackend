class globalVariable(object):
    FACTION_TYPE = (
        ('Druid', '德鲁伊'),
        ('Hunter', '猎人'),
        ('Mage', '法师'),
        ('Paladin', '圣骑士'),
        ('Priest', '牧师'),
        ('Rogue', '潜行者'),
        ('Shaman', '萨满'),
        ('Warlock', '术士'),
        ('Warrior', '战士'),
        ('Neutral', '中立')
    )
    RARITY_TYPE = (
        ('1', '基本'),
        ('2', '普通'),
        ('3', '稀有'),
        ('4', '史诗'),
        ('5', '传说'),
    )
    CLAZZ_TYPE = (
        ('1', '随从'),
        ('2', '法术'),
        ('3', '装备'),
        ('4', '英雄牌'),
    )
    MODE_TYPE = (
        ('Standard', '标准模式'),
        ('Wild', '狂野模式'),
        ('Arena', '竞技场')
    )

class globalFunc(object):
    def get_key(dict, value):
        return [k for k, v in dict.items() if v == value]

    def get_value(dict, key):
        return [v for k, v in dict.items() if k == key]