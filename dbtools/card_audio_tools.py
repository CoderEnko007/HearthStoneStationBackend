import sys
import os
import glob
import re
from HearthStoneStationBackend.settings import BASE_DIR

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HearthStoneStationBackend.settings")

import django
django.setup()

from cards.models import HSCards

audioPath = os.path.join(BASE_DIR, 'media')
audioFileEn = glob.glob(audioPath+'/sound/sounds*/*.wav')
audioFileZh = glob.glob(audioPath+'/sound/zhcn*/*.wav')
# print(type(audioFileEn), len(audioFileEn))
# f = open('./audio_name.txt', 'w')
# f.write(str(len(audioFileEn))+'\n')
# for audio in audioFileEn:
#     name = audio[audio.rfind('/')+1:]
#     print(name)
#     f.write(name+'\n')
# f.close()

queryset = HSCards.objects.all().order_by('cost')
for card in queryset:
    # print(card.hsId)
    for audio in audioFileEn:
        audio_name = audio[audio.rfind('/') + 1:]
        if ('HERO' not in card.hsId.upper()) and (card.hsId.upper() in audio_name.upper()):
            file_name = audio[audio[:audio.rfind('/')].rfind('/'):audio.rfind('/')]
            if re.search('.*_play[_.]+.*', audio_name, re.IGNORECASE) or re.search('.*_EnterPlay[_.].*', audio_name, re.IGNORECASE):
                card.audio_play_en = "http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name)
            if re.search('.*_attack[_.]+.*', audio_name, re.IGNORECASE):
                card.audio_attack_en = "http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name)
            if re.search('.*_death[_.]+.*', audio_name, re.IGNORECASE):
                card.audio_death_en = "http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name)
            if re.search('.*_trigger[_.]+.*', audio_name, re.IGNORECASE):
                card.audio_trigger_en = "http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name)
    for audio in audioFileZh:
        audio_name = audio[audio.rfind('/') + 1:]
        if ('HERO' not in card.hsId.upper()) and (card.hsId.upper() in audio_name.upper()):
            file_name = audio[audio[:audio.rfind('/')].rfind('/'):audio.rfind('/')]
            if re.search('.*_play[_.]+.*', audio_name, re.IGNORECASE) or re.search('.*_EnterPlay[_.].*', audio_name, re.IGNORECASE):
                card.audio_play_zh = "http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name)
            if re.search('.*_attack[_.]+.*', audio_name, re.IGNORECASE):
                card.audio_attack_zh = "http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name)
            if re.search('.*_death[_.]+.*', audio_name, re.IGNORECASE):
                card.audio_death_zh = "http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name)
            if re.search('.*_trigger[_.]+.*', audio_name, re.IGNORECASE):
                card.audio_trigger_zh = "http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name)
    card.save()
    print(card.hsId, card.name)
