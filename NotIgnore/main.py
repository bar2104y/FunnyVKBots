import vk_api,re
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from vk_api.utils import get_random_id

def main():

	users = []
	countMes = 10
	
	vk_token=""
	app_id = ""
	vk_client_secret = ""

	myid = 

	
	vk_session = vk_api.VkApi(token=vk_token, app_id=app_id, client_secret=vk_client_secret)
	vk = vk_session.get_api()

	longpoll = VkLongPoll(vk_session)

	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
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

			else:
				if event.raw[3] in users and event.from_user and event.to_me:
					mes = vk.messages.getHistory(user_id=event.raw[3], count=countMes)
					txt = mes['items'][0]['text'].lower()
					f = True
					for i in mes['items']:
						if (i['out'] == 1): f = False
					print(f)
					if(f):
						if re.search(r'(\?|кто|по какому|что|како|который|где|когда|почему|зачем|куда|откуда|сколько|чей|как|можно ли|стоит ли|ли)',txt) != None:
							try:
								vk.messages.send(
									user_id=event.raw[3],
									random_id=get_random_id(),
									message="ИГОРЬГЕЙ"
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