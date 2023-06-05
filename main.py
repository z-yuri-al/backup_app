from YaUploader import YandexUploader
from VkGroup import VkApp
from download_file import download_photo_to_ya

if __name__ == '__main__':
    with open('token_vk.txt') as token_file_vk:
        token_vk = token_file_vk.read()
token_yandex = input('Введите токен с полигона Яндекс Диска')
id_vk = input('Введите id пользователя ВК')

vk = VkApp(token_vk)
ya = YandexUploader(token_yandex)

dict_links = vk.get_photos_info(id_vk=id_vk)
download_photo_to_ya(dict_links, ya)
