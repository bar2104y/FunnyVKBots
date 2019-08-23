#Загрузка необходимых модулей
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload

# Перменная-костыль для избежания рекурсии
IsMyUpdate = False

def main():
    vk_token="" # Токен пользователя
    app_id = "" # ID приложения
    vk_client_secret = "" # Ключ приложения 
    # Авторизация
    vk_session = vk_api.VkApi(token=vk_token, app_id=app_id, client_secret=vk_client_secret)
    vk = vk_session.get_api()

    global IsMyUpdate # Объявления костыля как глобального
    chat_id = "" # id отслеживаемого чата

    # Подключение дополнительных библиотек
    longpoll = VkLongPoll(vk_session)
    upload = VkUpload(vk_session) 

    # Перебор данных
    for event in longpoll.listen():
        if event.type == VkEventType.CHAT_UPDATE:
            # print(event.__dict__)
            # print(event.update_type)
            # print(event.update_type.__dict__)
            
            # Если не мы меняли аватар
            if not IsMyUpdate:
                try:
                    # Загружаем новую
                    r = upload.photo_chat(photo='gerb.png', chat_id=chat_id)
                    #print(r)
                    # Отмечаем, что это мы, теперь это смена автара не обработается из за условия вше
                    IsMyUpdate = True           
                except Exception as e:
                    print(e) # выводим ошибки, если таковые имеются
            else:
                IsMyUpdate = False # Сбрасываем костыль
        # else:
        #     print(event.type)

#Бесконечный цикл с обработкой ошибок
while True:
    try:
        main()
    except Exception as e:
        print(e.__class__)