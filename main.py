from YaUploader import YandexUploader
from VkGroup import VkApp
from download_file import download_photo_to_yandex

if __name__ == '__main__':
    with open('token_vk.txt') as token_file_vk, open('token_yandex.txt') as token_file_yandex:
        token_vk = token_file_vk.read()
        token_yandex = token_file_yandex.read()

    vk = VkApp(token_vk)
    ya =YandexUploader(token_yandex)

    list_links = vk.get_photos()
    download_photo_to_yandex(list_links, yandex_client=ya)