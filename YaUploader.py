import requests

class YandexUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'{self.token}'
        }

    def upload(self, file_name, url):
        url_ya = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'path': f'photo_vk/{file_name}',
            'url': url,
        }
        responce = requests.post(url_ya, headers=headers, params=params)
        if responce.status_code == 202:
            print('Файл успешно загружен!')
        else:
            print(responce.json())