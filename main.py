import telebot
import psycopg2
import datetime
from telebot import types
token = "Ваш токен"
bot = telebot.TeleBot(token)
states = dict()
conn = psycopg2.connect(database = 'schedule', user = 'postgres', password = 'rootroot', host = 'localhost', port = '5432')
cursor = conn.cursor()
week_now = ''


def week_check():
    current_date = datetime.date.today()
    days_passed = (current_date - datetime.date(current_date.year, 1, 1)).days
    week_number = (days_passed // 7) + 1
    if week_number % 2 != 0:
        week_now = "Нечетная"
    else:
        week_now = "Четная"  
    return week_now



@bot.message_handler(commands=['start'])
def start(message):
  global week_now
  keyboard = types.ReplyKeyboardMarkup()
  keyboard.row("/mtuci", "/help", "/profile", "/week", '/schedule')
  week_check()
  bot.send_message(message.chat.id, 'Привет! Я телеграмм бот, который помогает группе БИН2312 в получении информации о расписании на четную и нечетную неделю, рекомендуем воспользоваться командой /help для получения информации о всех командах', reply_markup=keyboard)

@bot.message_handler(commands=['week'])
def get_week_state(message):
  bot.send_message(message.chat.id, f"Текущая неделя: {week_check()}")


@bot.message_handler(commands=['schedule'])
def schedule(message):
  markup = types.InlineKeyboardMarkup(row_width=1)
  monday = types.InlineKeyboardButton('Понедельник', callback_data='monday')
  tuesday = types.InlineKeyboardButton('Вторник', callback_data='tuesday')
  wednesday = types.InlineKeyboardButton('Среда', callback_data='wednesday')
  thursday = types.InlineKeyboardButton('Четверг', callback_data='thursday')
  friday = types.InlineKeyboardButton('Пятница', callback_data='friday')
  saturday = types.InlineKeyboardButton('Суббота', callback_data='saturday')
  all_week = types.InlineKeyboardButton('Вся текущая неделя', callback_data='all_week')
  all_next_week = types.InlineKeyboardButton('Вся следующая неделя', callback_data='all_next_week')
  markup.add(monday, tuesday, wednesday, thursday, friday, saturday, all_week, all_next_week)
  bot.send_message(message.chat.id, 'Выберите день и вам будет предоставлено актуальное расписание', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
  global week_now
  week_check()
  if call.message:
    if call.data == 'monday' and week_now == 'Четная':
      cursor.execute("select * from public.even_week where day_of_week = 'Понедельник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'monday' and week_now == 'Нечетная':
      cursor.execute("select * from public.odd_week where day_of_week = 'Понедельник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'tuesday' and week_now == 'Четная':
      cursor.execute("select * from public.even_week where day_of_week = 'Вторник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'tuesday' and week_now == 'Нечетная':
      cursor.execute("select * from public.odd_week where day_of_week = 'Вторник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'wednesday' and week_now == 'Четная':
      cursor.execute("select * from public.even_week where day_of_week = 'Среда")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'wednesday' and week_now == 'Нечетная':
      cursor.execute("select * from public.odd_week where day_of_week = 'Среда'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'thursday' and week_now == 'Четная':
      cursor.execute("select * from public.even_week where day_of_week = 'Четверг'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'thursday' and week_now == 'Нечетная':
      cursor.execute("select * from public.odd_week where day_of_week = 'Четверг'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'friday' and week_now == 'Четная':
      cursor.execute("select * from public.even_week where day_of_week = 'Пятница'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'friday' and week_now == 'Нечетная':
      cursor.execute("select * from public.odd_week where day_of_week = 'Пятница'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'saturday' and week_now == 'Четная':
      cursor.execute("select * from public.even_week where day_of_week = 'Суббота'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'saturday' and week_now == 'Нечетная':
      cursor.execute("select * from public.odd_week where day_of_week = 'Суббота'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'all_week' and week_now == 'Четная':
      bot.send_message(call.message.chat.id, f"Четная неделя")
      cursor.execute("select * from public.even_week where day_of_week = 'Понедельник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Вторник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Среда'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Четверг'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Пятница'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Суббота'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'all_week' and week_now == 'Нечетная':
      bot.send_message(call.message.chat.id, f"Нечетная неделя")
      cursor.execute("select * from public.odd_week where day_of_week = 'Понедельник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Вторник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Среда'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Четверг'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Пятница'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Суббота'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'all_next_week' and week_now == 'Нечетная':
      bot.send_message(call.message.chat.id, f"Четная неделя")
      cursor.execute("select * from public.even_week where day_of_week = 'Понедельник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Вторник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Среда'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Четверг'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Пятница'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.even_week where day_of_week = 'Суббота'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
    if call.data == 'all_next_week' and week_now == 'Четная':
      bot.send_message(call.message.chat.id, f"Нечетная неделя")
      cursor.execute("select * from public.odd_week where day_of_week = 'Понедельник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Вторник'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Среда'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Четверг'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Пятница'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
      cursor.execute("select * from public.odd_week where day_of_week = 'Суббота'")
      records = list(cursor.fetchall())
      bot.send_message(call.message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")


@bot.message_handler(commands=['help'])
def commands_message(message):
  bot.send_message(message.chat.id, f"Дынный бот предоставляет информацию о расписании на четную и нечетную для группы БИН2312, ниже написаны команды, где можно узнать расписание, как на конкретный день недели, так и на всю неделю вцелом, для удобства можете воспользоваться командой /schedule\n/even_week - четная неделя:\n/even_week_monday - Понедельник\n/even_week_tuesday - Вторник\n/even_week_wednesday - Среда\n/even_week_thursday - Четверг\n/even_week_friday - Пятница\n/even_week_saturday - Суббота\n/odd_week - нечетная неделя:\n/odd_week_monday - Понедельник\n/odd_week_tuesday - Вторник\n/odd_week_wednesday - Среда\n/odd_week_thursday - Четверг\n/odd_week_friday - Пятница\n/odd_week_saturday - Суббота\n/week - Узнать какая неделя на данный момент\nТакже вы можете ознакомиться с актуальными новостями МТУСИ, через команду /mtuci")


@bot.message_handler(commands=['even_week_monday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.even_week where day_of_week = 'Понедельник'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['even_week_tuesday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.even_week where day_of_week = 'Вторник'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['even_week_wednesday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.even_week where day_of_week = 'Среда'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['even_week_thursday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.even_week where day_of_week = 'Четверг'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['even_week_friday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.even_week where day_of_week = 'Пятница'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['even_week_saturday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.even_week where day_of_week = 'Суббота'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")

@bot.message_handler(commands=['odd_week_monday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.odd_week where day_of_week = 'Понедельник'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['odd_week_tuesday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.odd_week where day_of_week = 'Вторник'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['odd_week_wednesday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.odd_week where day_of_week = 'Среда'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['odd_week_thursday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.odd_week where day_of_week = 'Четверг'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['odd_week_friday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.odd_week where day_of_week = 'Пятница'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['odd_week_saturday'])
def even_week_monday_message(message):
  cursor.execute("select * from public.odd_week where day_of_week = 'Суббота'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['even_week'])
def even_week_monday_message(message):
  bot.send_message(message.chat.id, f"Четная неделя")
  cursor.execute("select * from public.even_week where day_of_week = 'Понедельник'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.even_week where day_of_week = 'Вторник'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.even_week where day_of_week = 'Среда'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.even_week where day_of_week = 'Четверг'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.even_week where day_of_week = 'Пятница'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.even_week where day_of_week = 'Суббота'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Четная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['odd_week'])
def even_week_monday_message(message):
  bot.send_message(message.chat.id, f"Нечетная неделя")
  cursor.execute("select * from public.odd_week where day_of_week = 'Понедельник'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.odd_week where day_of_week = 'Вторник'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.odd_week where day_of_week = 'Среда'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.odd_week where day_of_week = 'Четверг'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.odd_week where day_of_week = 'Пятница'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  cursor.execute("select * from public.odd_week where day_of_week = 'Суббота'")
  records = list(cursor.fetchall())
  bot.send_message(message.chat.id, f"Нечетная неделя\n{records[0][1]}\n\nПервая пара:\n {records[0][2]}\n\nВторая пара:\n {records[0][3]}\n\nТретья пара:\n {records[0][4]}\n\nЧетвертая пара:\n {records[0][5]}\n\nПятая пара:\n {records[0][6]}")
  
@bot.message_handler(commands=['profile'])
def profile_message(message):
    user = message.from_user
    profile_text = f'Идентификатор: {user.id}\n'
    profile_text += f'Имя пользователя: @{user.username}\n'
    bot.send_message(message.chat.id, profile_text)
    
@bot.message_handler(commands=['mtuci'])
def mtuci_message(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')
    
@bot.message_handler(content_types=['text'])
def answer(message):
  bot.send_message(message.chat.id, 'Простите, я вас не понял')
bot.polling(non_stop=True)
