#Подключение модулей
import vk_api,re
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id


def main():
	users = [] # Пользователи, которых мы "не игнорим"
	countMes = 10 # Кол-во сообщений 
	
	vk_token="" # Токен пользователя
	app_id = "" # Id приложения
	vk_client_secret = "" # Ключ приложения

	myid = # Ваш id

	# Подключаемся к серверу
	vk_session = vk_api.VkApi(token=vk_token, app_id=app_id, client_secret=vk_client_secret)
	vk = vk_session.get_api()
	longpoll = VkLongPoll(vk_session)

	# Перебираем события
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			# Если пишем сами себе и это не сообщение бота, то бота можно настраивать
			if event.raw[3] == myid and event.message[0] != "`":
				#Тут будет управление ботом				
				# try:
				# 	vk.messages.send(
				# 		user_id=myid,
				# 		random_id=get_random_id(),
				# 		message="`Повилитель, я тут, но я бесполезен"
				# 	)
				# except Exception as e:
				# 	print(e)

			else: # Если сообщение не в своем же чате 
				# Если сообщение нам пришло от нужного человека НЕ в чате
				if event.raw[3] in users and event.from_user and event.to_me:
					mes = vk.messages.getHistory(user_id=event.raw[3], count=countMes) # 
					txt = mes['items'][0]['text'].lower()# 
					f = True # Костыль
					# проверяем последние 10 сообщений
					for i in mes['items']:
						if (i['out'] == 1): f = False
					print(f) #
					# Если он написал >=countMes сообщений 
					if(f):
						# Если вопрос
						if re.search(r'(\?|кто|по какому|что|како|который|где|когда|почему|зачем|куда|откуда|сколько|чей|как|можно ли|стоит ли|ли)',txt) != None:
							#ПРобуем отправить сообщение
							try:
								vk.messages.send(
									user_id=event.raw[3],
									random_id=get_random_id(),
									message="Я не ингорю"
								)
							except Exception as e:
								print(e)
		else:
			print(event.type)


#Бесконечный цикл с обработкой исключений
while True:
	try:
		main()
	except Exception as e:
		print(e.__class__)