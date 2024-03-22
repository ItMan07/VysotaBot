import os

import keyboards
from loader import bot


@bot.message_handler(func=lambda message: True)
def cmd_create_report(message):
    if message.text == "Создать отчет":
        bot.send_message(
            message.chat.id,
            "Введите ваше ФИО",
            parse_mode="html",
        )
        bot.register_next_step_handler(message, get_full_name)
        # bot.register_next_step_handler(message, save_photos)


def get_full_name(message):
    full_name = message.text
    bot.send_message(
        message.chat.id,
        "Введите дату мероприятия (в формате ДД.ММ.ГГГГ)",
        parse_mode="html",
    )
    bot.register_next_step_handler(message, get_event_date, full_name)


def get_event_date(message, full_name):
    event_date = message.text
    bot.send_message(message.chat.id, "Введите описание мероприятия", parse_mode="html")
    bot.register_next_step_handler(message, get_description, full_name, event_date)


def get_description(message, full_name, event_date):
    description = message.text
    bot.send_message(
        message.chat.id,
        "Отправьте фото мероприятия без сжатия (пока только одну)",
        parse_mode="html",
    )
    bot.register_next_step_handler(
        message, save_photos, full_name, event_date, description
    )


def save_photos(
    message, full_name="name", event_date="01.01.2024", description="description"
):
    # print(message, sep="\n=sep=\n", end="\n=end=\n")
    if message.document:
        photo_folder_name = f"{full_name}_{event_date}"
        photo_folder = os.path.join("data", photo_folder_name)
        if not os.path.exists(photo_folder):
            os.makedirs(photo_folder)
        try:
            # for index, photo in enumerate(message.document):
            photo = message.document
            photo_info = bot.get_file(photo.file_id)
            _, file_extension = os.path.splitext(photo.file_name)
            # photo_filename = f"{full_name}_{event_date}_{index}{file_extension}"
            photo_filename = f"{full_name}_{event_date}{file_extension}"
            photo_path = os.path.join(photo_folder, photo_filename)
            downloaded_photo = bot.download_file(photo_info.file_path)
            with open(photo_path, "wb") as new_photo:
                new_photo.write(downloaded_photo)
            bot.send_message(
                message.chat.id,
                "Фото успешно сохранено(ы)",
                reply_markup=keyboards.main_keyboard,
                parse_mode="html",
            )
        except Exception as er:
            print("[ERROR in func save_photos]", er)
    else:
        bot.send_message(
            message.chat.id,
            "Вы не отправили ни одного фото. Попробуйте отправить без сжатия",
            reply_markup=keyboards.main_keyboard,
            parse_mode="html",
        )
