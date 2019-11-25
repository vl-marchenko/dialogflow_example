import apiai, json

def textMessage(s):
    # Токен API к Dialogflow
    request = apiai.ApiAI('Ваш Dialogflow токен').text_request()
    # На каком языке будет послан запрос
    request.lang = 'ru'
    # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.session_id = '3301megabot'
    # Посылаем запрос к ИИ с сообщением от юзера
    request.query = s 
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    # Разбираем JSON и вытаскиваем ответ
    response=''
    response = responseJson['result']['fulfillment']['speech'] 
    # Если есть ответ от бота - выдаём его,
    # если нет - бот его не понял
    if response:
        return response
    else:
        return 'Я Вас не совсем понял!'

s=''
while(s!='Выход'):
    s=input('Введите ваше сообщение: ')
    print(textMessage(s))
