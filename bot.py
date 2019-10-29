import telebot
import urllib.request
logo = urllib.request.urlopen("http://ccte.nau.edu.ua/images/Zameni.jpg").read()
bot = telebot.TeleBot("939402799:AAEfPDo4CZ7by1f_RpZnMW84FEyuQuRWDSA")

P_11 = P_12 = P_13 = R_11 = R_12 = K_11 = K_12 = K_13 = E_11 = F_11 = D_11 = A_11 = O_11 = 'Если хочешь что-бы тут было твое расписание - отправь его @kravavchenko :)'
P_21 = P_22 = P_23 = R_21 = R_22 = K_21 = K_22 = E_21 = F_21 = D_21 = A_21 = O_21 = 'Если хочешь что-бы тут было твое расписание - отправь его @kravavchenko :)'
P_31 = P_32 = P_33 = P_34 = R_31 = R_32 = R_33 = K_31 = K_32 = K_33 = E_31 = F_31 = D_31 = A_31 = A_32 = O_31 = 'Если хочешь что-бы тут было твое расписание - отправь его @kravavchenko :)'
P_41 = P_42 = P_43 = R_41 = R_42 = K_41 = K_42 = K_43 = K_44 = D_41 = A_41 = O_41 = 'Если хочешь что-бы тут было твое расписание - отправь его @kravavchenko :)'
from rasp import * # Файл с заполненными переменными

@bot.message_handler(commands=['start'])
def handle_start(message):
	user_markup = telebot.types.ReplyKeyboardMarkup(True)
	user_markup.row('Замены','Расписание')
	bot.send_message(message.from_user.id, 'Привет, я заменный бот. Работаю как в чате, так и в лс', reply_markup=user_markup)
	global id_user
	id_user.append(message.from_user.id)

@bot.message_handler(commands=['ccte_bot_replacements'])
def ccte_replacements(message):
	bot.send_photo(message.chat.id, logo)


@bot.message_handler(content_types=['text'])
def ccte_replacements(message):
	user_markup0 = telebot.types.ReplyKeyboardMarkup(True)
	user_markup0.row('На главную')
	if message.text == 'На главную':
		user_markup = telebot.types.ReplyKeyboardMarkup(True)
		user_markup.row('Замены', 'Расписание')
		bot.send_message(message.from_user.id, 'Главное меню', reply_markup=user_markup)

	if message.text == 'Замены':
		bot.send_photo(message.from_user.id, logo, )
	if message.text == 'Расписание':
		user_markup_kurs = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs.row('1 курс', '2 курс', '3 курс', '4 курс')
		bot.send_message(message.from_user.id, 'Выбери курс', reply_markup=user_markup_kurs)

	if message.text == '1 курс':
		user_markup_kurs1 = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs1.row('П-1', 'Р-1', 'К-1', 'Е-1')
		user_markup_kurs1.row('Ф-1', 'Д-1', 'А-1', 'О-1')
		bot.send_message(message.from_user.id, 'Выбери специальнось', reply_markup=user_markup_kurs1)

	if message.text == 'П-1':
		user_markup_kurs1p = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs1p.row('П-11', 'П-12', 'П-13')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs1p)
	if message.text == 'П-11':
		bot.send_message(message.from_user.id, P_11, reply_markup=user_markup0)
	if message.text == 'П-12':
		bot.send_message(message.from_user.id, P_12, reply_markup=user_markup0)
	if message.text == 'П-13':
		bot.send_message(message.from_user.id, P_13, reply_markup=user_markup0)

	if message.text == 'Р-1':
		user_markup_kurs1r = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs1r.row('Р-11', 'Р-12')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs1r)
	if message.text == 'Р-11':
		bot.send_message(message.from_user.id, R_11, reply_markup=user_markup0)
	if message.text == 'Р-12':
		bot.send_message(message.from_user.id, R_12, reply_markup=user_markup0)

	if message.text == 'К-1':
		user_markup_kurs1k = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs1k.row('К-11', 'К-12', 'К-13')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs1k)
	if message.text == 'К-11':
		bot.send_message(message.from_user.id, K_11, reply_markup=user_markup0)
	if message.text == 'К-12':
		bot.send_message(message.from_user.id, K_12, reply_markup=user_markup0)
	if message.text == 'К-13':
		bot.send_message(message.from_user.id, K_13, reply_markup=user_markup0)

	if message.text == 'Е-1':
		bot.send_message(message.from_user.id, E_11, reply_markup=user_markup0)

	if message.text == 'Ф-1':
		bot.send_message(message.from_user.id, F_11, reply_markup=user_markup0)

	if message.text == 'Д-1':
		bot.send_message(message.from_user.id, D_11, reply_markup=user_markup0)

	if message.text == 'А-1':
		bot.send_message(message.from_user.id, A_11, reply_markup=user_markup0)

	if message.text == 'О-1':
		bot.send_message(message.from_user.id, O_11, reply_markup=user_markup0)


	if message.text == '2 курс':
		user_markup_kurs2 = telebot.types.ReplyKeyboardMarkup(True)																	#1курс!!!!!!!!!
		user_markup_kurs2.row('П-2', 'Р-2', 'К-2', 'Е-2')
		user_markup_kurs2.row('Ф-2', 'Д-2', 'А-2', 'О-2')
		bot.send_message(message.from_user.id, 'Выбери специальнось', reply_markup=user_markup_kurs2)

	if message.text == 'П-2':
		user_markup_kurs2p = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs2p.row('П-21', 'П-22', 'П-23')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs2p)
	if message.text == 'П-21':
		bot.send_message(message.from_user.id, P_21, reply_markup=user_markup0)
	if message.text == 'П-22':
		bot.send_message(message.from_user.id, P_22, reply_markup=user_markup0)
	if message.text == 'П-23':
		bot.send_message(message.from_user.id, P_23, reply_markup=user_markup0)

	if message.text == 'Р-2':
		user_markup_kurs2r = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs2r.row('Р-21', 'Р-22')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs2r)
	if message.text == 'Р-21':
		bot.send_message(message.from_user.id, R_21, reply_markup=user_markup0)
	if message.text == 'Р-22':
		bot.send_message(message.from_user.id, R_22, reply_markup=user_markup0)

	if message.text == 'К-2':
		user_markup_kurs2k = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs2k.row('К-21', 'К-22')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs2k)
	if message.text == 'К-21':
		bot.send_message(message.from_user.id, K_21, reply_markup=user_markup0)
	if message.text == 'К-22':
		bot.send_message(message.from_user.id, K_22, reply_markup=user_markup0)

	if message.text == 'Е-2':
		bot.send_message(message.from_user.id, E_21, reply_markup=user_markup0)

	if message.text == 'Ф-2':
		bot.send_message(message.from_user.id, F_21, reply_markup=user_markup0)

	if message.text == 'Д-2':
		bot.send_message(message.from_user.id, D_21, reply_markup=user_markup0)

	if message.text == 'А-2':
		bot.send_message(message.from_user.id, A_21, reply_markup=user_markup0)

	if message.text == 'О-2':
		bot.send_message(message.from_user.id, O_21, reply_markup=user_markup0)

	if message.text == '3 курс':
		user_markup_kurs3 = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs3.row('П-3', 'Р-3', 'К-3', 'Е-3')
		user_markup_kurs3.row('Ф-3', 'Д-3', 'А-3', 'О-3')
		bot.send_message(message.from_user.id, 'Выбери специальнось', reply_markup=user_markup_kurs3)

	if message.text == 'П-3':
		user_markup_kurs3p = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs3p.row('П-31', 'П-32', 'П-33', 'П-34')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs3p)
	if message.text == 'П-31':
		bot.send_message(message.from_user.id, P_31, reply_markup=user_markup0)
	if message.text == 'П-32':
		bot.send_message(message.from_user.id, P_32, reply_markup=user_markup0)
	if message.text == 'П-33':
		bot.send_message(message.from_user.id, P_33, reply_markup=user_markup0)
	if message.text == 'П-34':
		bot.send_message(message.from_user.id, P_34, reply_markup=user_markup0)

	if message.text == 'Р-3':
		user_markup_kurs3r = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs3r.row('Р-31', 'Р-32', 'Р-33')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs3r)
	if message.text == 'Р-31':
		bot.send_message(message.from_user.id, R_31, reply_markup=user_markup0)
	if message.text == 'Р-32':
		bot.send_message(message.from_user.id, R_32, reply_markup=user_markup0)
	if message.text == 'Р-33':
		bot.send_message(message.from_user.id, R_33, reply_markup=user_markup0)

	if message.text == 'К-3':
		user_markup_kurs3k = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs3k.row('К-31', 'К-32', 'К-33')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs3k)
	if message.text == 'К-31':
		bot.send_message(message.from_user.id, K_31, reply_markup=user_markup0)
	if message.text == 'К-32':
		bot.send_message(message.from_user.id, K_32, reply_markup=user_markup0)
	if message.text == 'К-33':
		bot.send_message(message.from_user.id, K_33, reply_markup=user_markup0)

	if message.text == 'Е-3':
		bot.send_message(message.from_user.id, E_31, reply_markup=user_markup0)

	if message.text == 'Ф-3':
		bot.send_message(message.from_user.id, F_31, reply_markup=user_markup0)

	if message.text == 'Д-3':
		bot.send_message(message.from_user.id, D_31, reply_markup=user_markup0)

	if message.text == 'А-3':
		user_markup_kurs3a = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs3a.row('А-31', 'А-32')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs3a)
	if message.text == 'А-31':
		bot.send_message(message.from_user.id, A_31, reply_markup=user_markup0)
	if message.text == 'А-32':
		bot.send_message(message.from_user.id, A_32, reply_markup=user_markup0)

	if message.text == 'О-3':
		bot.send_message(message.from_user.id, O_31, reply_markup=user_markup0)

	if message.text == '4 курс':
		user_markup_kurs4 = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs4.row('П-4', 'Р-4', 'К-4')
		user_markup_kurs4.row('Д-4', 'А-4', 'О-4')
		bot.send_message(message.from_user.id, 'Выбери специальнось', reply_markup=user_markup_kurs4)

	if message.text == 'П-4':
		user_markup_kurs4p = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs4p.row('П-41', 'П-42', 'П-43')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs4p)
	if message.text == 'П-41':
		bot.send_message(message.from_user.id, P_41, reply_markup=user_markup0)
	if message.text == 'П-42':
		bot.send_message(message.from_user.id, P_42, reply_markup=user_markup0)
	if message.text == 'П-43':
		bot.send_message(message.from_user.id, P_43, reply_markup=user_markup0)

	if message.text == 'Р-4':
		user_markup_kurs4r = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs4r.row('Р-41', 'Р-42')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs4r)
	if message.text == 'Р-41':
		bot.send_message(message.from_user.id, R_41, reply_markup=user_markup0)
	if message.text == 'Р-42':
		bot.send_message(message.from_user.id, R_42, reply_markup=user_markup0)

	if message.text == 'К-4':
		user_markup_kurs4k = telebot.types.ReplyKeyboardMarkup(True)
		user_markup_kurs4k.row('К-41', 'К-42', 'К-43', 'К-44')
		bot.send_message(message.from_user.id, 'Выбери группу', reply_markup=user_markup_kurs4k)
	if message.text == 'К-41':
		bot.send_message(message.from_user.id, K_41, reply_markup=user_markup0)
	if message.text == 'К-42':
		bot.send_message(message.from_user.id, K_42, reply_markup=user_markup0)
	if message.text == 'К-43':
		bot.send_message(message.from_user.id, K_43, reply_markup=user_markup0)
	if message.text == 'К-44':
		bot.send_message(message.from_user.id, K_44, reply_markup=user_markup0)

	if message.text == 'Д-4':
		bot.send_message(message.from_user.id, D_41, reply_markup=user_markup0)

	if message.text == 'А-4':
		bot.send_message(message.from_user.id, A_41, reply_markup=user_markup0)

	if message.text == 'О-4':
		bot.send_message(message.from_user.id, O_41, reply_markup=user_markup0)



bot.polling(none_stop=True, interval=0)



