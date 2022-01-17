import json
import requests
import urllib

api_key = {
    'client_id':'ec59002ba0fc4c74bf50',
    'client_secret':'bd7264a9542173aa188b650c1b76580e7d612355'
}

tablesID = {
    'decks_trending': 55498,
    'decks_decks': 53174,
    'standard_decks': 53174,
    'wild_decks': 55625,
    'classic_decks': 117489,
    'arena_cards': 70488,
    'trending': 53120,
    'hsCard': 76131,
    'bgsCard': 87402,
    'winrate': 96629,
    'new_cards': 88786,
    'activation_code': 90990
}

class iFanr(object):

    def __init__(self):
        self.client_id = api_key.get('client_id')
        self.client_secret = api_key.get('client_secret')
        self.code_url = "https://cloud.minapp.com/api/oauth2/hydrogen/openapi/authorize/"
        self.token_url = "https://cloud.minapp.com/api/oauth2/access_token/"
        self.tablesID = tablesID
        self.get_token()

    def get_code(self):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(self.code_url, data=json.dumps(params))
        re_dict = json.loads(response.text)
        return re_dict.get('code')

    def get_token(self):
        code = self.get_code()
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code
        }
        response = requests.post(self.token_url, data=params)
        re_dict = json.loads(response.text)
        self.token = re_dict.get('access_token')

    def get_table_data(self, tableID, query, next=None):
        if next:
            BASE_API = r'https://cloud.minapp.com{}'.format(next)
        else:
            BASE_API = r'https://cloud.minapp.com/oserve/v1/table/%s/record/' % tableID
        HEADERS = {
            'Authorization': 'Bearer %s' % self.token
        }
        if query:
            """ query写法
            where_ = {
              'price': {'$gt': 100},
            }
             query_ = urllib.urlencode({
                'where': json.dumps(where_),
                'order_by': '-created_at',
                'limit': 10,
                'offset': 0,
            })
            """
            query_ = urllib.parse.urlencode(query)
            API = '?'.join((BASE_API, query_))
        else:
            API = BASE_API
        response = requests.get(API, headers=HEADERS)
        try:
            re_dict = json.loads(response.text)
        except Exception as e:
            re_dict = ''
            print(e)
            print('API:', API)
            print('response:', response)
        return re_dict

    def add_table_data(self, tableID, data):
        print('add_table_data', tableID)
        url = r'https://cloud.minapp.com/oserve/v1/table/%s/record/' % tableID
        headers = {
            'Authorization': 'Bearer %s' % self.token,
            'Content-Type': 'application/json'
        }
        data = json.dumps(data)
        response = requests.post(url, headers=headers, data=data)
        re_dict = json.loads(response.text)
        print('add', re_dict)
        return re_dict

    def put_table_data(self, tableID, id, data):
        print('put_table_data', tableID, id)
        if id is None:
            print('ifanr id is None')
            return
        url = r'https://cloud.minapp.com/oserve/v1/table/%s/record/%s/' % (tableID, id)
        headers = {
            'Authorization': 'Bearer %s' % self.token,
            'Content-Type': 'application/json'
        }
        data = json.dumps(data)
        response = requests.put(url, headers=headers, data=data)
        re_dict = json.loads(response.text)
        print('update', re_dict)


    def upload_file(self, filename, category_id, filepath):
        # Step 1：获取授权凭证和上传地址
        url = 'https://cloud.minapp.com/oserve/v1/upload/'
        headers = {
            'Authorization': 'Bearer %s' % self.token,
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = json.dumps({
            'filename': filename,
            'category_id': category_id
        })
        response = requests.post(url, headers=headers, data=data)
        # Step 2: 使用Step 1中的授权凭证上传文件
        if response.status_code == 200:
            re_dict = json.loads(response.text)
            print('update', re_dict)

            upload_url = re_dict['upload_url']

            headers = {
                'Authorization': 'Bearer %s' % self.token,
            }
            with open(filepath, 'rb') as f:
                data = {
                    'authorization': re_dict['authorization'],
                    'policy': re_dict['policy'],
                }
                res = requests.post(upload_url, headers=headers, data=data, files={'file': f})
                return re_dict['file_link']
        else:
            print('获取授权失败')



if __name__ == "__main__":
    ifanr = iFanr()
    filePath = '/home/enko/projects/HearthStoneStationBackend/media/images/tiles/HERO_01.png'
    link = ifanr.upload_file('test.jpg', '5c7b53390f978c6e00e864fe', filePath)
    print('file link:', link)

