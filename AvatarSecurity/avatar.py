import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload

IsMyUpdate = False

def main():
    vk_token=""
    app_id = ""
    vk_client_secret = ""
    vk_session = vk_api.VkApi(token=vk_token, app_id=app_id, client_secret=vk_client_secret)
    vk = vk_session.get_api()

    global IsMyUpdate
    longpoll = VkLongPoll(vk_session)
    upload = VkUpload(vk_session) 

    for event in longpoll.listen():
        if event.type == VkEventType.CHAT_UPDATE:
            print(event.__dict__)
            print(event.update_type)
            print(event.update_type.__dict__)
            
            if not IsMyUpdate:
                try:
                    r = upload.photo_chat(photo='gerb.png', chat_id='111')
                    print(r)
                    IsMyUpdate = True               
                except Exception as e:
                    print(e)
            else:
                IsMyUpdate = False
        # else:
        #     print(event.type)

while True:
    try:
        main()
    except Exception as e:
        print(e.__class__)