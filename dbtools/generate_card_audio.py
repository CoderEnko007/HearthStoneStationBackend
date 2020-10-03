import os
import re
import json

class AssetManager():
    def __init__(self):
        self.cn_file = os.path.join(os.path.abspath('./mono_file'), 'asset_catalog_locale_zhcn.txt')
        self.us_file = os.path.join(os.path.abspath('./mono_file'), 'base_assets_catalog.txt')
        self.cards_list = []

    def generation_json_file(self):
        for locale in ['enUS', 'zhCN']:
            self.load_file(locale)
        print('共包含{}张卡牌'.format(len(self.cards_list)))
        self.write_json()

    def load_file(self, locale='enUS'):
        path = self.cn_file if locale == 'zhCN' else self.us_file
        with open(path, 'r') as f:
            file_lines = f.readlines()
            for line in file_lines:
                # 过滤所有.wav文件
                if re.search('.*(\.wav)', line, re.I|re.M):
                    format_str = re.search('.*\"(.*)\"', line).group(1).split('/')
                    # 去除非卡牌音频
                    if len(format_str) < 6 or (not re.search(r'\d', format_str[-2]) and not re.search(r'\d', format_str[-3])):
                        continue
                    hsId = format_str[-2] if re.search(r'\d', format_str[-2]) else format_str[-3]
                    card_dict = {}
                    filtered_items = list(filter(lambda x: x['hsId']==hsId, self.cards_list))
                    if len(filtered_items):
                        card_dict = filtered_items[0]
                    else:
                        card_dict['hsId'] = hsId
                    audio_file_name = format_str[-1]
                    if locale == 'enUS':
                        if re.search('.*_play[0-9_.]+.*', audio_file_name, re.I) or re.search('.*_EnterPlay[0-9_.]+.*', audio_file_name, re.I):
                            if 'audio_play_en' in card_dict:
                                card_dict['audio_play_en'].append(audio_file_name)
                            else:
                                card_dict['audio_play_en'] = [audio_file_name]
                        elif re.search('.*_attack[0-9_.]+.*', audio_file_name, re.I):
                            if 'audio_attack_en' in card_dict:
                                card_dict['audio_attack_en'].append(audio_file_name)
                            else:
                                card_dict['audio_attack_en'] = [audio_file_name]
                        elif re.search('.*_death[0-9_.]+.*', audio_file_name, re.I):
                            if 'audio_death_en' in card_dict:
                                card_dict['audio_death_en'].append(audio_file_name)
                            else:
                                card_dict['audio_death_en'] = [audio_file_name]
                        elif re.search('.*_trigger[0-9_.]+.*', audio_file_name, re.I):
                            if 'audio_trigger_en' in card_dict:
                                card_dict['audio_trigger_en'].append(audio_file_name)
                            else:
                                card_dict['audio_trigger_en'] = [audio_file_name]
                        else:
                            if 'none_type_audio_en' in card_dict:
                                card_dict['none_type_audio_en'].append(audio_file_name)
                            else:
                                card_dict['none_type_audio_en'] = [audio_file_name]
                    if locale == 'zhCN':
                        if re.search('.*_play[0-9_.]+.*', audio_file_name, re.I) or re.search('.*_EnterPlay[0-9_.]+.*', audio_file_name, re.I):
                            if 'audio_play_zh' in card_dict:
                                card_dict['audio_play_zh'].append(audio_file_name)
                            else:
                                card_dict['audio_play_zh'] = [audio_file_name]
                        elif re.search('.*_attack[0-9_.]+.*', audio_file_name, re.I):
                            if 'audio_attack_zh' in card_dict:
                                card_dict['audio_attack_zh'].append(audio_file_name)
                            else:
                                card_dict['audio_attack_zh'] = [audio_file_name]
                        elif re.search('.*_death[0-9_.]+.*', audio_file_name, re.I):
                            if 'audio_death_zh' in card_dict:
                                card_dict['audio_death_zh'].append(audio_file_name)
                            else:
                                card_dict['audio_death_zh'] = [audio_file_name]
                        elif re.search('.*_trigger[0-9_.]+.*', audio_file_name, re.I):
                            if 'audio_trigger_zh' in card_dict:
                                card_dict['audio_trigger_zh'].append(audio_file_name)
                            else:
                                card_dict['audio_trigger_zh'] = [audio_file_name]
                        else:
                            if 'none_type_audio_zh' in card_dict:
                                card_dict['none_type_audio_zh'].append(audio_file_name)
                            else:
                                card_dict['none_type_audio_zh'] = [audio_file_name]
                    if len(filtered_items)<=0:
                        self.cards_list.append(card_dict)
                        print('新增：', card_dict['hsId'])
                    else:
                        print('更新：',card_dict['hsId'])

    def write_json(self):
        jsonCookies = json.dumps(self.cards_list)
        filename = os.path.join(os.path.abspath('.'), 'audio_json_file.json')
        with open(filename, 'w') as f:
            try:
                f.write(jsonCookies)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    obj = AssetManager()
    obj.generation_json_file()
