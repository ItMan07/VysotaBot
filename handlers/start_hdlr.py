import keyboards
from loader import bot


@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.username}. Нажмите кнопку <b>Создать отчет</b>, чтобы начать",
        reply_markup=keyboards.main_kb(),
        parse_mode="html",
    )
