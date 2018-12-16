import sys
import os
import glob
import re
import json
from HearthStoneStationBackend.settings import BASE_DIR

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HearthStoneStationBackend.settings")

import django
django.setup()

from cards.models import HSCards

audioPath = os.path.join(BASE_DIR, 'media')
audioFileEn = glob.glob(audioPath+'/sound/sounds/*.wav')
audioFileZh = glob.glob(audioPath+'/sound/soundszhcn/*.wav')
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
    # if card.type == 'SPELL' or card.type == 'WEAPON': continue
    audio_play_en = []
    audio_attack_en = []
    audio_death_en = []
    audio_trigger_en = []
    audio_play_zh = []
    audio_attack_zh = []
    audio_death_zh = []
    audio_trigger_zh = []
    for audio in audioFileEn:
        audio_name = audio[audio.rfind('/') + 1:]
        if ('HERO' not in card.hsId.upper()) and (card.hsId.upper() in audio_name.upper()):
            # file_name = audio[audio[:audio.rfind('/')].rfind('/'):audio.rfind('/')]
            file_name = '/sounds'
            if re.search('.*_play[0-9_.]+.*', audio_name, re.IGNORECASE) or re.search('.*_EnterPlay[0-9_.]+.*', audio_name, re.IGNORECASE):
                audio_play_en.append("http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name))
            if re.search('.*_attack[0-9_.]+.*', audio_name, re.IGNORECASE):
                audio_attack_en.append("http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name))
            if re.search('.*_death[0-9_.]+.*', audio_name, re.IGNORECASE):
                audio_death_en.append("http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name))
            if re.search('.*_trigger[0-9_.]+.*', audio_name, re.IGNORECASE):
                audio_trigger_en.append("http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name))
    for audio in audioFileZh:
        audio_name = audio[audio.rfind('/') + 1:]
        if ('HERO' not in card.hsId.upper()) and (card.hsId.upper() in audio_name.upper()):
            # file_name = audio[audio[:audio.rfind('/')].rfind('/'):audio.rfind('/')]
            file_name = '/soundszhcn'
            if re.search('.*_play[0-9_.]+.*', audio_name, re.IGNORECASE) or re.search('.*_EnterPlay[0-9_.]+.*', audio_name, re.IGNORECASE):
                audio_play_zh.append("http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name))
            if re.search('.*_attack[0-9_.]+.*', audio_name, re.IGNORECASE):
                audio_attack_zh.append("http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name))
            if re.search('.*_death[0-9_.]+.*', audio_name, re.IGNORECASE):
                audio_death_zh.append("http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name))
            if re.search('.*_trigger[0-9_.]+.*', audio_name, re.IGNORECASE):
                audio_trigger_zh.append("http://47.98.187.217/media/sound{0}/{1}".format(file_name, audio_name))
    card.audio_play_en = json.dumps(sorted(audio_play_en), ensure_ascii=False) if len(audio_play_en)>0 else None
    card.audio_attack_en = json.dumps(sorted(audio_attack_en), ensure_ascii=False) if len(audio_attack_en)>0 else None
    card.audio_death_en = json.dumps(sorted(audio_death_en), ensure_ascii=False) if len(audio_death_en)>0 else None
    card.audio_trigger_en = json.dumps(sorted(audio_trigger_en), ensure_ascii=False) if len(audio_trigger_en)>0 else None
    card.audio_play_zh = json.dumps(sorted(audio_play_zh), ensure_ascii=False) if len(audio_play_zh)>0 else None
    card.audio_attack_zh = json.dumps(sorted(audio_attack_zh), ensure_ascii=False) if len(audio_attack_zh)>0 else None
    card.audio_death_zh = json.dumps(sorted(audio_death_zh), ensure_ascii=False) if len(audio_death_zh)>0 else None
    card.audio_trigger_zh = json.dumps(sorted(audio_trigger_zh), ensure_ascii=False) if len(audio_trigger_zh)>0 else None
    card.save()
    print(card.hsId, card.name)
