# - *- coding: utf- 8 - *-
import telebot
from telebot import types


bot = telebot.TeleBot('1239457471:AAFgWZf4opZtAvtJBcr5py3DgiaXG60cgNI')


# вступ

@bot.message_handler(commands=['start'])
def welcome(message):
    # Клава
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Меню")
    markup.row(item1)

    bot.send_message(message.chat.id,
                     "Привіт, {0.first_name}!\nЯ - <b>{1.first_name}</b> у мене ти знайдеш найкращі ігри.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# Кнопка

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':

        if message.text == 'Меню':
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("Ігри", callback_data='games')
            item2 = types.InlineKeyboardButton("Покупка?", callback_data='buys')
            item3 = types.InlineKeyboardButton("Допомога?", callback_data='helpme')
            markup.row(item1)
            markup.row(item2)
            markup.row(item3)

            bot.send_message(message.chat.id, 'Головне меню', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю, що ти хочеш')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:

            # Меню
            if call.data == 'Menu':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Ігри", callback_data='games')
                item2 = types.InlineKeyboardButton("Покупка?", callback_data='buys')
                item3 = types.InlineKeyboardButton("Допомога?", callback_data='helpme')
                markup.row(item1)
                markup.row(item2)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Головне меню",
                                      reply_markup=markup)


            #########################################################################

            # Список розділів
            elif call.data == 'games':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Євро трак", callback_data='game1')
                item2 = types.InlineKeyboardButton("Топ ігор ", callback_data='game2')
                item3 = types.InlineKeyboardButton("Топ дешевих ігор", callback_data='game3')
                # item4 = types.InlineKeyboardButton("Всі ігри ", callback_data='game4')
                item5 = types.InlineKeyboardButton("Замовлення гри", callback_data='game5')

                item77 = types.InlineKeyboardButton("⬅️", callback_data='Menu')
                # item88 = types.InlineKeyboardButton("⏹", callback_data='Menu')

                markup.row(item1)
                markup.row(item2)
                markup.row(item3)
                #  markup.row(item4)
                markup.row(item5)
                markup.add(item77, )  # item88)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Каталог продукції",
                                      reply_markup=markup)







            ###########################################################################
            # Покупка
            elif call.data == 'buys':

                markup = types.InlineKeyboardMarkup(row_width=2)
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')

                markup.add(btn_my_site)
                item77 = types.InlineKeyboardButton("⬅️", callback_data='Menu')
                item88 = types.InlineKeyboardButton("⏹", callback_data='Menu')

                # item3 = types.InlineKeyboardButton("⬅", callback_data='Menu')
                markup.add(item77, item88)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="""Для покупки перейдіть по посиланю \nТа звяжіться з адміністрацією  вкажіть що ви хочете купити та кількість  після підтверженя  очікуйте обробку вашого замовлення та ваш ключ.""",
                                      reply_markup=markup)


            ###########################################################################
            # Допомога
            elif call.data == 'helpme':

                markup = types.InlineKeyboardMarkup(row_width=2)

                item1 = types.InlineKeyboardButton("Як активувати?", callback_data='key')
                item2 = types.InlineKeyboardButton("Як купити?", callback_data='buys')
                item3 = types.InlineKeyboardButton("⬅", callback_data='Menu')
                # item88 = types.InlineKeyboardButton("⏹", callback_data='Menu')
                markup.add(item1, item2)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть що вам потрібно",
                                      reply_markup=markup)


            elif call.data == 'key':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Стім", callback_data='steam1')
                item2 = types.InlineKeyboardButton("Рокстар", callback_data='gta51')
                item3 = types.InlineKeyboardButton("⬅", callback_data='helpme')
                item88 = types.InlineKeyboardButton("⏹", callback_data='Menu')

                markup.row(item1)
                markup.row(item2)
                markup.add(item3, item88)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть де ви хочете активувати ключ",
                                      reply_markup=markup)



            elif call.data == 'steam1':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("⬅", callback_data='key')
                item88 = types.InlineKeyboardButton("⏹", callback_data='Menu')
                markup.row(item3, item88)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=""""Як активувати ключ в стім?

Після отримання ключа його необхідно активувати, щоб придбання виявилося в ігровій бібліотеці Steam. Якщо у користувача немає Стіма, то для початку потрібно буде пройти на офіційний сайт компанії і завантажити його, після чого будуть завантажені всі оновлення, і тоді можна реєструватися.
Після цього клікніть по кнопці « Додати гру»В лівому нижньому кутку вікна і виберіть в списку пункт« Активувати в Steam ... ».
Відкриється наступне вікно, в якому стверджується, що покупку можна додати в свою бібліотеку, ввівши цифровий код. натискаємо « далі».

У наступному вікні запропонують ознайомитися з ліцензійною угодою Стим, роз'яснюють торговельну політику компанії і права користувача. Щоб продовжити натисніть « погоджуюся».

З'явиться саме вікно введення. Скопіюйте набір символів в єдине поле або введіть його вручну, якщо він записаний на фізичному носії. Після чого натисніть «Далі».

Після завершення активації з'явиться вікно, яке повідомить про успішне завершення процесу і грі яку отримав користувач.""",
                                      reply_markup=markup)

            elif call.data == 'gta51':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item3 = types.InlineKeyboardButton("⬅", callback_data='key')
                markup.row(item3)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Як активувати ключ в стім?GTA 5 ключ на пк
Активація GTA 5.
1)Скачайте Rockstar Games Launcher на офіційному сайті і встановіть.
Увага! Не пробуйте активувати ключ на сайті!
2)Запустіть програму і увійдіть у свій акаунт, або створіть новий, якщо у вас його нема .
3)У верхньому правому куті програми натисніть на значок облікового запису, клікніть на кнопку «Погашення коду», введіть куплений ключ і натисніть «Перевірити».""",
                                      reply_markup=markup)


            #######################################################################################################################

            # ETS 2

            elif call.data == 'game1':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Євро трак 2 ключ", callback_data='etsgame')
                item2 = types.InlineKeyboardButton("Євро трак 2 длс", callback_data='etsdlc')
                item3 = types.InlineKeyboardButton("<-", callback_data='games')

                markup.row(item1)
                markup.row(item2)
                markup.row(item3)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть що ви хочете.",
                                      reply_markup=markup)

            # ETS 2 key

            elif call.data == 'etsgame':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Євро трак 2", callback_data='etsgame1')
                item2 = types.InlineKeyboardButton("Євро трак 2 Game of the Year Edition", callback_data='etsgame2')
                item3 = types.InlineKeyboardButton("<-", callback_data='game1')

                markup.row(item1)
                markup.row(item2)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть видавництво гри.",
                                      reply_markup=markup)

            # ETS 2 key buy

            elif call.data == 'etsgame1':

                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='etsgame')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Ets 2 - ціна 90 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            # ETS 2 Game year key buy

            elif call.data == 'etsgame2':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='etsgame')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Ets 2 Game of the Year Edition  - ціна 120 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # ETS dls

            elif call.data == 'etsdlc':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Карти", callback_data='maps')
                item2 = types.InlineKeyboardButton("Грузи", callback_data='gryz')
                item3 = types.InlineKeyboardButton("Тюнінг", callback_data='tune1')
                item4 = types.InlineKeyboardButton("<-", callback_data='game1')
                markup.row(item1)
                markup.row(item2)
                markup.row(item3)
                markup.row(item4)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажану категорію длс.",
                                      reply_markup=markup)

            # Длс карта
            elif call.data == 'maps':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Euro Truck Simulator 2 - Beyond the Baltic Sea",
                                                   callback_data='Baltick')
                item2 = types.InlineKeyboardButton("DLC Euro Truck Simulator 2 - Italia", callback_data='Italia')
                item3 = types.InlineKeyboardButton("DLC Euro Truck Simulator 2 - Vive la France!",
                                                   callback_data='France')
                item4 = types.InlineKeyboardButton("DLC Euro Truck Simulator 2 – Scandinavia",
                                                   callback_data='Scandinavia')
                item5 = types.InlineKeyboardButton("DLC Euro Truck Simulator 2 - Going East", callback_data='East')
                item6 = types.InlineKeyboardButton("<-", callback_data='etsdlc')
                markup.row(item1)
                markup.row(item2)
                markup.row(item3)
                markup.row(item4)
                markup.row(item5)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане длс.",
                                      reply_markup=markup)

            # Покупка длс карта
            elif call.data == 'Baltick':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='maps')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Euro Truck Simulator 2 - Beyond the Baltic Sea  - ціна 180 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            elif call.data == 'Italia':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='maps')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="DLC Euro Truck Simulator 2 - Italia - 130 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            elif call.data == 'France':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='maps')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="DLC Euro Truck Simulator 2 - Vive la France! - 75 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            elif call.data == 'Scandinavia':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='maps')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="DLC Euro Truck Simulator 2 – Scandinavia - 75 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            elif call.data == 'East':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='maps')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="DLC Euro Truck Simulator 2 - Going East! -45 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Длс грузи
            elif call.data == 'gryz':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("DLC Special Transport ", callback_data='gryz11')
                item2 = types.InlineKeyboardButton("DLC Heavy Cargo Pack", callback_data='gryz12')
                item3 = types.InlineKeyboardButton("DLC High Power Cargo Pack", callback_data='gryz13')
                item6 = types.InlineKeyboardButton("<-", callback_data='etsdlc')
                markup.row(item1)
                markup.row(item2)
                markup.row(item3)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане длс.",
                                      reply_markup=markup)
            # Покупка длс грузи
            elif call.data == 'gryz11':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='gryz')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="DLC Special Transport - 47 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            elif call.data == 'gryz12':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='gryz')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="DLC Heavy Cargo Pack - 35 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            elif call.data == 'gryz13':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='gryz')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="DLC High Power Cargo Pack - 25 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Длс тюн
            elif call.data == 'tune1':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("DLC Cabin Accessories", callback_data='cabin')
                item6 = types.InlineKeyboardButton("<-", callback_data='etsdlc')
                markup.row(item1)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане длс.",
                                      reply_markup=markup)
            # Покупка длс грузи
            elif call.data == 'cabin':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='tune1')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="DLC Cabin Accessories -33 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            ##################################################################################

            # Топ ігор список
            elif call.data == 'game2':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Gta 5", callback_data='gta5game')
                item2 = types.InlineKeyboardButton("Euro truck 2", callback_data='game1')
                item3 = types.InlineKeyboardButton("Dark Souls 3", callback_data='dark3')
                item4 = types.InlineKeyboardButton("Mount & Blade 2:Bannerlord", callback_data='mb2')
                item12 = types.InlineKeyboardButton("Rainbow Six: Siege", callback_data='six')
                item5 = types.InlineKeyboardButton("Dying Light", callback_data='dl')
                item6 = types.InlineKeyboardButton("Far cry 5", callback_data='farcry5')
                item7 = types.InlineKeyboardButton("Fallout 4", callback_data='fallout4')
                item8 = types.InlineKeyboardButton("The Elder Scrolls V", callback_data='skyrim')
                item9 = types.InlineKeyboardButton("Civilization V", callback_data='civa5')
                item13 = types.InlineKeyboardButton("Civilization VI", callback_data='civa6')
                item10 = types.InlineKeyboardButton("Mafia 2", callback_data='mafia2')

                item11 = types.InlineKeyboardButton("<-", callback_data='games')

                markup.row(item1)
                markup.row(item2)
                markup.row(item3)
                markup.row(item4)
                markup.row(item12)
                markup.row(item5)
                markup.row(item6)
                markup.row(item7)
                markup.row(item8)
                markup.row(item9)
                markup.row(item13)
                markup.row(item10)
                markup.row(item11)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберайте і насолоджуйтесь.",
                                      reply_markup=markup)

            # гта 5
            elif call.data == 'gta5game':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Gta 5", callback_data='gta5game1')
                item2 = types.InlineKeyboardButton("GTA 5 Premium Edition", callback_data='gta5game2')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item2)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво\nGTA 5.",
                                      reply_markup=markup)

            # Покупка GTA 5 stock
            elif call.data == 'gta5game1':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='gta5game')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="GTA 5 - 280 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка GTA 5 premiyn
            elif call.data == 'gta5game2':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='gta5game')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="GTA 5 premium edition - 300 грн\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Dark soul
            elif call.data == 'dark3':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Dark Souls 3", callback_data='dark31')
                item2 = types.InlineKeyboardButton("Dark Souls 3 - Deluxe Edition", callback_data='dark32')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item2)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка dark stock
            elif call.data == 'dark31':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='dark3')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Dark Souls 3- 175 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка dark  premiyn
            elif call.data == 'dark32':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='dark3')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Dark Souls 3 - Deluxe Edition - 210 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # MB
            elif call.data == 'mb2':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Mount & Blade II: Bannerlord", callback_data='mb1')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка mb
            elif call.data == 'mb1':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='mb2')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Mount & Blade II: Bannerlord - 510 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            # six
            elif call.data == 'six':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Rainbow Six", callback_data='six11')
                item2 = types.InlineKeyboardButton("Rainbow Six: Siege deluxe edition", callback_data='six12')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item2)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка six stock
            elif call.data == 'six11':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='six')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Rainbow Six edition - 180 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка six  premiyn
            elif call.data == 'six12':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='six')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Rainbow Six: Siege deluxe edition - 240 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Dying Light
            elif call.data == 'dl':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Dying Light", callback_data='dl1')
                item2 = types.InlineKeyboardButton("Dying Light Enhanced Edition", callback_data='dl2')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item2)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка Dying Light
            elif call.data == 'dl1':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='dl')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Dying Light - 150 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка Dying Light Enhanced Edition
            elif call.data == 'dl2':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='dl')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Dying Light Enhanced Edition - 170 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # fc5
            elif call.data == 'farcry5':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Far cry 5", callback_data='fc51')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка fc5
            elif call.data == 'fc51':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='farcry5')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Far Cry 5 - 250 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

            # fallout 4
            elif call.data == 'fallout4':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Fallout 4", callback_data='f41')
                item2 = types.InlineKeyboardButton("Fallout 4 game of the year edition", callback_data='f42')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item2)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка fallout 4
            elif call.data == 'f41':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='fallout4')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Fallout 4 - 115 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка fallout 4
            elif call.data == 'f42':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='fallout4')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Fallout 4 game of the year edition - 320 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # skyrim
            elif call.data == 'skyrim':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("The Elder Scrolls V: Skyrim", callback_data='sk11')
                item2 = types.InlineKeyboardButton("The Elder Scrolls V: Skyrim Legendary Edition",
                                                   callback_data='sk12')
                item3 = types.InlineKeyboardButton("The Elder Scrolls V: Skyrim Special Edition", callback_data='sk13')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item2)
                markup.row(item3)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка The Elder Scrolls V
            elif call.data == 'sk11':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='skyrim')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="The Elder Scrolls V: Skyrim - 75 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка Scrolls V: Skyrim Legendary Edition
            elif call.data == 'sk12':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='skyrim')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="The Elder Scrolls V: Skyrim Legendary Edition - 210 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка The Elder Scrolls V: Skyrim Special Edition  - 265 грн
            elif call.data == 'sk13':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='skyrim')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="The Elder Scrolls V: Skyrim Special Edition - 265 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # CV5
            elif call.data == 'civa5':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Civilization V", callback_data='civa511')
                item2 = types.InlineKeyboardButton("Civilization V complete edition", callback_data='civa512')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item2)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка cv5
            elif call.data == 'civa511':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='civa5')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Civilization V - 99 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка Civilization V complete edition - 240 грн
            elif call.data == 'civa512':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='civa5')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Civilization V complete edition - 240 грн - 210 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # CV6
            elif call.data == 'civa6':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Civilization VI", callback_data='civa611')
                item2 = types.InlineKeyboardButton("Civilization VI Deluxe Edition ", callback_data='civa612')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)
                markup.row(item2)
                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка cv6
            elif call.data == 'civa611':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='civa6')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Civilization VI - 210 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # Покупка Civilization 6 deluxe edition
            elif call.data == 'civa612':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='civa6')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Civilization VI Deluxe Edition - 240 грн - 210 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            # mafia
            elif call.data == 'mafia2':

                markup = types.InlineKeyboardMarkup(row_width=2)
                item1 = types.InlineKeyboardButton("Mafia 2", callback_data='mafia221')
                item6 = types.InlineKeyboardButton("<-", callback_data='game2')
                markup.row(item1)

                markup.row(item6)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберіть бажане видавництво.",
                                      reply_markup=markup)

            # Покупка mafia 2
            elif call.data == 'mafia221':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Оформлення покупки',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='mafia2')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Mafia 2 - 99 грн.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)
            ##################################################################################################

            # Топ дешевих ігор список
            elif call.data == 'game3':
                markup = types.InlineKeyboardMarkup(row_width=2)
                item2 = types.InlineKeyboardButton("Euro truck 2", callback_data='game1')
                item7 = types.InlineKeyboardButton("Fallout 4", callback_data='fallout4')
                item8 = types.InlineKeyboardButton("The Elder Scrolls V", callback_data='skyrim')
                item9 = types.InlineKeyboardButton("Civilization V", callback_data='civa5')
                item10 = types.InlineKeyboardButton("Mafia 2", callback_data='mafia2')

                item11 = types.InlineKeyboardButton("<-", callback_data='games')

                markup.row(item2)
                markup.row(item7)
                markup.row(item8)
                markup.row(item9)
                markup.row(item10)
                markup.row(item11)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Виберайте і насолоджуйтесь.",
                                      reply_markup=markup)
            ######################################################################################################
            #
            ##всі ігри
            #          elif call.data == 'game3':
            #             markup = types.InlineKeyboardMarkup(row_width=2)
            #            item2 = types.InlineKeyboardButton("Euro truck 2", callback_data='game1')
            #           item7 = types.InlineKeyboardButton("Fallout 4", callback_data='fallout4')
            #          item8 = types.InlineKeyboardButton("The Elder Scrolls V", callback_data='skyrim')
            #         item9 = types.InlineKeyboardButton("Civilization V", callback_data='civa5')
            #        item10 = types.InlineKeyboardButton("Mafia 2", callback_data='mafia2')
            #
            #               item11 = types.InlineKeyboardButton("<-", callback_data='games')
            #
            #
            #
            #             markup.row(item2)
            #            markup.row(item7)
            #           markup.row(item8)
            #          markup.row(item9)
            #         markup.row(item10)
            #        markup.row(item11)
            #
            #
            #               bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Виберайте і насолоджуйтесь.",
            #             reply_markup=markup)
            #
            #######################################################################################################
            elif call.data == 'game5':
                markup = types.InlineKeyboardMarkup()
                btn_my_site = types.InlineKeyboardButton(text='Замовлення гри',
                                                         url='https://t.me/joinchat/IrOLNllNNpdQVLwbEC6ODA')
                item3 = types.InlineKeyboardButton("<-", callback_data='games')
                markup.add(btn_my_site)
                markup.row(item3)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Не знайшли гру не бійтеся є вихід просто замовте її у нас.\nДля покупки перейдіть за посиланням.",
                                      reply_markup=markup)

                # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                # text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)

