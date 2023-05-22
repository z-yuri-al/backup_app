def download_photo_to_yandex(list_links, yandex_client):
    file_name_baza = '/фото с вк новые/'
    count = 1
    for links in list_links:
        file_name = file_name_baza + str(count)
        yandex_client.upload(file_name=file_name, url=links)
        print(count)
        count += 1
    print(f'Все файлы в количестве {len(list_links)} успешно загружены')