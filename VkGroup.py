import requests

class VkApp:

    def __init__(self, token, version = 5.131):
        self.params = {
            'access_token' : token,
            'v' : 5.131
        }

    def get_info_users(self,id):
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids' : id,
            'fields' : 'city,country,sex,site,about,bdate,counrets',
            **self.params
        }
        responce = requests.get(url, params=params)
        data = responce.json()
        return data

    def groups_search(self, text):
        url = 'https://api.vk.com/method/groups.search'
        params = {
            'q' : text,
            'sort' : 6,
            'count' : 5,
            **self.params
        }
        responce = requests.get(url, params=params)
        data = responce.json()
        return data

    def get_docs(self):
        url = 'https://api.vk.com/method/docs.get'
        params ={
            'count' : 10,
            **self.params
        }
        responce = requests.get(url, params=params)
        data = responce.json()
        return data

    def get_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id' : -33858187,
            'album_id' : 'wall',
            'count' : 1000,
            'rev' : 1,
            **self.params
        }
        response = requests.get(url,params=params)
        data = response.json()
        print(data['response']['count'])
        list_dict = data['response']['items']
        list_links = []
        for dict in list_dict:
            list_sizes_dict = dict['sizes']
            link_zero = list_sizes_dict[0]['url']
            height_zero = list_sizes_dict[0]['height']
            for sizes in list_sizes_dict:
                height = sizes['height']
                if height > height_zero:
                    height_zero = height
                    link_zero = sizes['url']
            list_links.append(link_zero)

        return list_links