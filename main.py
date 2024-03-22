import telebot
import keyboards

bot = telebot.TeleBot('6781026273:AAFkx_-yQoE5gdi3e2Gyy1ps_mFLcAwYfZg')


@bot.message_handler(commands=['help', 'start'])
def cmd_start(message):
    bot.send_message(
        message.chat.id, f"""Привет, {message.from_user.username}""",
        reply_markup=keyboards.main_kb()
    )


@bot.message_handler(func=lambda message: True)
def cmd_create_report(message):
    if message.text == "Создать отчет":
        msg = bot.reply_to(message, "ФИО:")
        bot.register_next_step_handler(msg, cmd_create_report2)


def cmd_create_report2(message):
    name = message.text
    msg = bot.reply_to(message, "Описание проведенного мероприятия:")
    bot.register_next_step_handler(msg, cmd_create_report3)


def cmd_create_report3(message):
    description = message.text
    msg = bot.reply_to(message, "Фотоотчет:")
    bot.register_next_step_handler(cmd_create_report4)

bot.infinity_polling()
