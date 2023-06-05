import requests

class VkApp:
    def __init__(self, token):
        self.params = {
            'access_token': token,
            'v': 5.131
        }

    def get_photos_info(self, id_vk, count=5, album_id='profile'):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': id_vk,
            'album_id': album_id,
            'count': count,
            'rev': 1,
            'extended': 1,
            **self.params
        }
        response = requests.get(url, params=params)
        data = response.json()
        list_dict = data['response']['items']
        dict_links = {}
        for dict in list_dict:
            list_sizes_dict = dict['sizes']
            link_zero = list_sizes_dict[0]['url']
            height_zero = list_sizes_dict[0]['height']
            width_zero = list_sizes_dict[0]['width']
            for sizes in list_sizes_dict:
                height = sizes['height']
                if height > height_zero:
                    height_zero = height
                    width_zero = sizes['width']
                    link_zero = sizes['url']
            dict_links[link_zero] = (dict['likes']['count'], dict['date'], f'{height_zero}*{width_zero}')
        return dict_links