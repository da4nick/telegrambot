import telebot
from telebot import types
from selenium import webdriver
from time import sleep

bot = telebot.TeleBot("5246210066:AAEQ78jN4rUPaA0UkqYgxLIYvHokiyHitls", parse_mode=None)

a = ''
g = ''
k = 0
name = 'Пользователь'
driver = webdriver.Chrome()

@bot.message_handler(commands=['start'])
def commands(message):
    #Функция получает на вход сообщение /start, в ответ отправляет инструкцию по использованию
	bot.reply_to(message, "Привет! хочешь услышать анекдот или найти видео на youtube? Напиши /help, чтобы узнать как это сделать!")


@bot.message_handler(commands=['help'])
def commands(message):
    #Функция получает на вход сообщение /help, в ответ отправляет список команд и какую функцию они выполняют
	bot.reply_to(message, "Этот бот отправляет анекдоты на заданую тобой тему! Напиши команду /findan, чтобы найти анекдот на определённую тему или /findrandom, чтобы найти случчайный. Чтобы посмотреть какие есть темы, напиши /tags. \
    Чтобы найти видео на Youtube напиши /findvid.")

@bot.message_handler(commands=['tags'])
def commands(message):
    #Функция получает на вход сообщение /tags, в ответ отправляет темы анекдотов
	bot.reply_to(message, "Темы анекдотов: apple, telegram, windows, Абрамович, авиация, авто, автобус, аптека, армия, Баба-Яга, Березовский, бесплатное, \
    блондинки, богатыри, Брежнев, брюнетки, Буратино, Валуев, веган, Винни-Пух, Вконтакте, вовочка, водка, война, врачи, гаи, геи, грипп, дача, девушки, \
    демократия, деньги, дети, диета, Донцова, егэ, животные, жкх, звёзды, Иван-царевич, ии, инструкции, интернет, Каренина, Карлсон, кино, Колобок, \
    коронавирус, коррупция, космос, кошки, кредиты, кризис, Куклачев, лифт, любовь, Мазай, маршрутка, Медведев, метро, милиция, ммм, мобильный, Москва, \
    мужчины, мультфильмы, Муму, Навальный, налоги, нанотехнологии, наркотики, новогодний, Обама, объявления, Одесса, Онищенко, отдых, охота, парашют, пасха, \
    пенсионеры, Перельман, пиво, погода, поезд, пожарный, покемоны, политика, почта, пошлые, приметы, программист, Прохоров, Путин, Пушкин, Рабинович, работа, \
    реклама, Ржевский, рыбалка, санкции, сантехник, сбербанк, свадьба, секс, семья, сигареты, смс, собаки ,соседи, спорт, Сталин, студент, Сусанин, такси, таможня, \
    тараканы, тв, твиттер, тёща, трактор ,трамвай ,Трамп ,троллейбус ,Украина ,фильмы, фсб, футбол ,хоккей, Хоттабыч, цитаты, чапаев, Чебурашка, Челябинск, чукча, \
    школа, Штирлиц, юмор.")

@bot.message_handler(func=lambda m: True)
def find_anekdot(message):
    '''Функция получает на входе команду /findan, /findvid или /findrandom, после чего вым присылают сообщение, на которое вам надо ответить, ващ ответ перенаправится \
        в другие функции бота'''
    global k
    if message.text == '//start':
        bot.send_message(message.from_user.id, 'Как тебя можно называть?')
        bot.register_next_step_handler(message, username)
    elif message.text == '/findan':
        bot.send_message(message.from_user.id, name + ', напиши тему, на которую хочешь найти анекдот.')
        k = 0
        bot.register_next_step_handler(message, poiskan)
    elif message.text == '/findvid':
        bot.send_message(message.from_user.id, name + ', напиши название видео, которое ты хочешь найти.')
        k = 1
        bot.register_next_step_handler(message, poiskvid)
    elif message.text == '/findrandom':
        bot.send_message(message.from_user.id, 'Отправляю случайный анекдот!')
        ranekdot = 'http://anekdotme.ru/random'
        driver.get(ranekdot)
        sleep(1)
        joke = driver.find_element_by_class_name('anekdot_text')
        msg = joke.text
        bot.send_message(message.chat.id, msg)
    else:
        bot.reply_to(message, 'Я тебя не понимаю, напиши /help')

def username(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Приятно познакомиться, ' + name + '!')

def poiskan(message):
    #Данная функция спрашивает вас - уверенны ли вы в своём ответе, а так же сохраняет ваше сообщение из прошлой функции как переменную
    global a 
    a = message.text
    thema = "Ты хочешь найти анекдот на тему: " + a + "?"
    buttons = types.InlineKeyboardMarkup()
    yes_button = types.InlineKeyboardButton(text='Да', callback_data='yes')
    buttons.add(yes_button)
    no_button = types.InlineKeyboardButton(text='Нет', callback_data='no')
    buttons.add(no_button)
    bot.send_message(message.from_user.id, text = thema, reply_markup=buttons)

def poiskvid(message):
    #Данная функция спрашивает вас - уверенны ли вы в своём ответе, а так же сохраняет ваше сообщение из прошлой функции как переменную
    global g
    g = message.text
    thema = "Ты хочешь найти видео под названием: " + g 
    buttons = types.InlineKeyboardMarkup()
    yes_button = types.InlineKeyboardButton(text='Да', callback_data='yes')
    buttons.add(yes_button)
    no_button = types.InlineKeyboardButton(text='Нет', callback_data='no')
    buttons.add(no_button)
    bot.send_message(message.from_user.id, text = thema, reply_markup=buttons)


@bot.callback_query_handler(func=lambda call: True)
def otvet(call):
    '''Функция получает на входе ваш ответ (да или нет),если он отрицательный, вас возращает к предыдущей функции, если же он положительный, с помощью библиотеки selenium \
       происходит парсинг с сайтов(зависимые от вашего выбора), выводит информацию в телеграм '''
    if call.data == "yes":
        if k == 0:
            anekdot = 'https://www.anekdot.ru/tags/' + a
            bot.send_message(call.message.chat.id, 'Ищу анекдоты')
            driver.get(anekdot)
            sleep(3)
            joke = driver.find_elements_by_class_name('text')
            for i in range(len(joke)):
                msg = joke[i].text
                bot.send_message(call.message.chat.id, msg)
                if i == 2:
                    break
        else:
            video = 'https://www.youtube.com/results?search_query=' + g
            bot.send_message(call.message.chat.id, 'Ищу видео')
            driver.get(video)
            sleep(3)
            videos = driver.find_elements_by_id('video-title')
            for i in range(len(videos)):
                bot.send_message(call.message.chat.id, videos[i].get_attribute('href'))
                if i == 4:
                    break
    elif call.data == "no":
        if k == 0:
            bot.send_message(call.message.chat.id, "Выбери тему ещё раз")
            bot.register_next_step_handler(call.message, poiskan)
        else:
            bot.send_message(call.message.chat.id, "Выбери название видео ещё раз")
            bot.register_next_step_handler(call.message, poiskvid)

if __name__ == '__main__':
    bot.infinity_polling()