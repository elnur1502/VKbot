import vk_api
import random
from Consts import *
from vk_api.longpoll import VkLongPoll, VkEventType

vk = vk_api.VkApi(token=TOKEN)
long_poll = VkLongPoll(vk)

for event in long_poll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        user = vk.method("users.get", {"user_ids": event.user_id})[0]
        if event.text == "Привет":
            vk.method('messages.send', {'user_id': event.user_id,
                                        'message': "Добрый день, " + user['first_name'] + "!",
                                        'random_id': random.randint(1, 2 ** 64)})
        elif event.text == "Как дела?":
            vk.method('messages.send', {'user_id': event.user_id,
                                        'message': "Все хорошо, а у Вас?",
                                        'random_id': random.randint(1, 2 ** 64)})
        elif event.text == "Пока":
            vk.method('messages.send', {'user_id': event.user_id,
                                        'message': "До встречи, " + user['last_name'] + " " + user['first_name'] + "!",
                                        'random_id': random.randint(1, 2 ** 64)})
