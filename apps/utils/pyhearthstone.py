from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType

class HearthStoneDeck():
    def __init__(self, hero, cards, sideboards, format=FormatType.FT_STANDARD):
        self.deck = Deck()
        self.heroes = hero
        self.format = format
        self.cards = cards
        self.sideboards = sideboards

    def getHeroesId(self, hero_str):
        heroes = {'Druid': 274, 'Hunter': 31, 'Mage': 637, 'Paladin': 671, 'Priest': 813, 'Rogue': 930,
                  'Shaman': 1066, 'Warlock': 893, 'Warrior': 7, 'Demonhunter': 56550, 'Deathknight': 78065}
        return heroes.get(hero_str.capitalize())

    def genDeckString(self):
        self.deck.heroes = [self.getHeroesId(self.heroes)]
        self.deck.format = self.format
        self.deck.cards = self.cards
        self.deck.sideboards = self.sideboards
        deckstring = self.deck.as_deckstring
        print(deckstring)
        return deckstring


