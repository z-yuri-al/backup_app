from pprint import pprint
import json

def download_photo_to_ya(dict_links, ya_client):
    list_info = []
    for links,name in dict_links.items():
        file_name = name[0]
        for dict in list_info:
            x = dict['file_name']
            if str(name[0]) in x:
                file_name = name[1]
            else:
                file_name = name[0]
        ya_client.upload(file_name=file_name, url=links)
        dict_info = {
            'file_name' : f'{file_name}.jpg',
            'size' : f'{name[2]}'
        }
        list_info.append(dict_info)
    print(f'Все файлы в количестве {len(dict_links)} успешно загружены')
    with open('info.json', 'w') as file:
        json.dump(list_info, file, ensure_ascii=False, indent=2)

