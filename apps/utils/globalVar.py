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
        ('DemonHunter', '恶魔猎手'),
        ('Neutral', '中立')
    )
    ARENA_FACTION_TYPE = (
        ('ALL', '全部'),
        ('DRUID', '德鲁伊'),
        ('HUNTER', '猎人'),
        ('MAGE', '法师'),
        ('PALADIN', '圣骑士'),
        ('PRIEST', '牧师'),
        ('ROGUE', '潜行者'),
        ('SHAMAN', '萨满'),
        ('WARLOCK', '术士'),
        ('WARRIOR', '战士'),
        ('DEMONHUNTER', '恶魔猎手'),
    )
    RARITY_TYPE = (
        ('FREE', '免费'),
        ('COMMON', '普通'),
        ('RARE', '稀有'),
        ('EPIC', '史诗'),
        ('LEGENDARY', '传说'),
    )
    CLAZZ_TYPE = (
        ('MINION', '随从'),
        ('SPELL', '法术'),
        ('WEAPON', '武器'),
        ('HERO', '英雄牌'),
    )
    MODE_TYPE = (
        ('All', '全部模式'),
        ('Classic', '经典模式'),
        ('Standard', '标准模式'),
        ('Wild', '狂野模式'),
        ('Arena', '竞技场'),
        ('Duels', '对决模式')
    )

class globalFunc(object):
    def get_key(dict, value):
        return [k for k, v in dict.items() if v == value]

    def get_value(dict, key):
        return [v for k, v in dict.items() if k == key]