import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from spam_text import spam
from time import sleep
import random
import json
token =
groupnumberid = 
vk_session = vk_api.VkApi(token=token)
longpoll  = VkBotLongPoll(vk_session, groupnumberid)
i=0

def get_but(text, color):
	return {
				"action": {
					"type": "text",
					"payload": "{\"button\": \"" + "1" + "\"}",
					"label": f"{text}"
				},
				"color": f"{color}"
			}

keyboard = {
	"one_time" : True,
	"buttons" : [
		[get_but('Я никогда', 'primary'), get_but('не стану', 'primary'), get_but('феминисткой', 'primary'), get_but('За то, что у', 'primary')],
		[get_but('Меня есть сиськи', 'primary'), get_but('Я получаю что', 'primary'), get_but('Ни захочу', 'primary'), get_but('Завтра вот в', 'primary')],
		[get_but('Мальдивы полечу', 'primary'), get_but('Ты захотела я уже', 'primary'), get_but('решила У своего', 'primary'), get_but('Мужчины попросила', 'primary')],
		[get_but('К моим ногам', 'primary'), get_but('Летят шелка', 'primary'), get_but('К твоим лишь', 'primary'), get_but('Окончание Ка', 'primary')],
		[get_but('Чем больше он', 'primary'), get_but('Ебашит, тем я краше', 'primary'), get_but('сижу и дома жду', 'primary'), get_but('его с борщем', 'primary')],
		[get_but('Засуньте в жопу', 'primary'), get_but('Феменизмы ваши', 'primary'), get_but('Я бэха, а не русский', 'primary'), get_but('автопром! ты работаешь', 'primary')],
		[get_but('как ломовая лошадь', 'primary'), get_but('Чтобы купить себе', 'primary'), get_but('какую то жилплощадь', 'primary'), get_but('И будешь на работе', 'primary')]
	]
}
keyboard2 = {
	"one_time" : True,
	"buttons" : [
		[get_but('Я за будду', 'negative'), get_but('Путин топ', 'negative'), get_but('лгбт', 'negative'), get_but('гы', 'negative')],
		[get_but('Я за будду', 'negative'), get_but('Путин топ', 'negative'), get_but('лгбт', 'negative'), get_but('гы', 'negative')],
		[get_but('Я за будду', 'negative'), get_but('Путин топ', 'negative'), get_but('лгбт', 'negative'), get_but('гы', 'negative')],
		[get_but('Я за будду', 'negative'), get_but('Путин топ', 'negative'), get_but('лгбт', 'negative'), get_but('гы', 'negative')],
		[get_but('Я за будду', 'negative'), get_but('Путин топ', 'negative'), get_but('лгбт', 'negative'), get_but('гы', 'negative')],
		[get_but('Я за будду', 'negative'), get_but('Путин топ', 'negative'), get_but('лгбт', 'negative'), get_but('гы', 'negative')],
		[get_but('как ломовая лошадь', 'negative'), get_but('Чтобы купить себе', 'negative'), get_but('какую то жилплощадь', 'negative'), get_but('И будешь на работе', 'negative')]
	]
}
keyboard3 = {
	"one_time" : True,
	"buttons" : [
		[get_but('В этом', 'positive'), get_but('мире', 'positive'), get_but('только натуралы,', 'positive'), get_but('если вы', 'positive')],
		[get_but('за лгбт', 'positive'), get_but('то мы', 'positive'), get_but('разорвем', 'positive'), get_but('ваше анальное', 'positive')],
		[get_but('отверствие, а', 'positive'), get_but('потом поставим', 'positive'), get_but('раком и трахнет', 'positive'), get_but('вас краб!', 'positive')],
		[get_but('В этом', 'positive'), get_but('мире', 'positive'), get_but('только натуралы,', 'positive'), get_but('если вы', 'positive')],
		[get_but('за лгбт', 'positive'), get_but('то мы', 'positive'), get_but('разорвем', 'positive'), get_but('ваше анальное', 'positive')],
		[get_but('отверствие, а', 'positive'), get_but('потом поставим', 'positive'), get_but('раком и трахнет', 'positive'), get_but('вас краб!', 'positive')],
		[get_but('В этом', 'positive'), get_but('мире', 'positive'), get_but('только натуралы,', 'positive'), get_but('если вы', 'positive')]	
	]
}

keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
keyboard2 = json.dumps(keyboard2, ensure_ascii = False).encode('utf-8')
keyboard2 = str(keyboard2.decode('utf-8'))
keyboard3 = json.dumps(keyboard3, ensure_ascii = False).encode('utf-8')
keyboard3 = str(keyboard3.decode('utf-8'))

def sender(id, text):
	global i
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard})
	i+=1
	print(f'сообщений отправлено - {i}')
	sleep(2)
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard2})
	i+=1
	print(f'сообщений отправлено - {i}')
	sleep(2)
	vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard3})
	i+=1
	print(f'сообщений отправлено - {i}')
	sleep(2)

for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW:
		if event.from_chat:

			id = event.chat_id
			msg = event.object.message['text'].lower()
			msg2 = event.object.message['text']
			print(msg2)

			if msg == '/help':
				while True:
					sender(id, "LL#4865 " + spam + " LL#4865")

