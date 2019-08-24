#Загрузка необходимых модулей
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id

# Перменная-костыль для избежания рекурсии
IsMyUpdate = False

def main():
	# Настройки
	vk_token="" # Токен пользователя
	app_id = "" # ID приложения
	vk_client_secret = "" # Ключ приложения 

	chat_id =  # id отслеживаемого чата (Обязательно число)
	mesAnswer = True # Подкрепляется ли восстановление втарки сообщением
	mesTxt = "Технологии на страже революции" # Текст сообщения
	dialog_id = 2000000000 + chat_id # СОздание peer_id

	# Авторизация
	vk_session = vk_api.VkApi(token=vk_token, app_id=app_id, client_secret=vk_client_secret)
	vk = vk_session.get_api()

	global IsMyUpdate # Объявления костыля как глобального

	# Подключение дополнительных библиотек
	longpoll = VkLongPoll(vk_session)
	upload = VkUpload(vk_session) 

	# Перебор данных
	for event in longpoll.listen():
		if event.type == VkEventType.CHAT_UPDATE:
			
			# Проверяем нужный ли чат
			if event.chat_id == chat_id:
				# Если не мы меняли аватар
				if not IsMyUpdate:
					try:
						# Загружаем новую
						r = upload.photo_chat(photo='gerb.png', chat_id=chat_id)
						print(r)
						print("Капитализм не пройдет!")
						# Отмечаем, что это мы, теперь это смена автара не обработается из за условия вше
						IsMyUpdate = True           
					except Exception as e:
						print(e) # выводим ошибки, если таковые имеются
					
					if mesAnswer:
						try:
							# Отправка сообщения
							vk.messages.send(
								peer_id=dialog_id,
								random_id=get_random_id(),
								message=mesTxt
							)
						except Exception as e:
							print(e) # выводим ошибки, если таковые имеются
				else:
					IsMyUpdate = False # Сбрасываем костыль
		elif event.type == VkEventType.MESSAGE_NEW:
			print(event.__dict__)
		else:
			print(event.type)

#Бесконечный цикл с обработкой ошибок
while True:
	try:
		main()
	except Exception as e:
		print(e.__class__)