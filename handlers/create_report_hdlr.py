import os

import keyboards
from loader import bot


@bot.message_handler(func=lambda message: True)
def cmd_create_report(message):
    if message.text == "Создать отчет":
        bot.send_message(
            # message.chat.id, "Введите ваше ФИО",
            message.chat.id, "Отправьте фотографию мероприятия (пока только одну)",
            reply_markup=keyboards.cancel_kb(),
            parse_mode='html'
        )
        bot.register_next_step_handler(message, get_full_name)
        # bot.register_next_step_handler(message, save_photos)

    # if message.text == "Отмена":
    #     bot.send_message(
    #         message.chat.id, "ОК",
    #         reply_markup=keyboards.main_kb(),
    #         parse_mode='html'
    #     )


def get_full_name(message):
    full_name = message.text
    bot.send_message(
        message.chat.id, "Введите дату мероприятия (в формате ДД.ММ.ГГГГ)",
        parse_mode='html'
    )
    bot.register_next_step_handler(message, get_event_date, full_name)


def get_event_date(message, full_name):
    event_date = message.text
    bot.send_message(
        message.chat.id, "Введите описание мероприятия",
        parse_mode='html'
    )
    bot.register_next_step_handler(message, get_description, full_name, event_date)


def get_description(message, full_name, event_date):
    description = message.text
    bot.send_message(
        message.chat.id, "Отправьте фото мероприятия БЕЗ СЖАТИЯ (пока только одну)",
        parse_mode='html'
    )
    bot.register_next_step_handler(message, save_photos, full_name, event_date, description)


def save_photos(message):
    full_name = "name"
    event_date = "01.01.2024"
    description = "description"

    # print(message, sep="\n=sep=\n", end="\n=end=\n")
    if message.document:
        photo_folder_name = f"{full_name}_{event_date}"
        photo_folder = os.path.join("data", photo_folder_name)
        if not os.path.exists(photo_folder):
            os.makedirs(photo_folder)

        # for index, photo in enumerate(message.document):
        photo = message.document
        photo_info = bot.get_file(photo.file_id)
        _, file_extension = os.path.splitext(photo.file_name)
        # photo_filename = f"{full_name}_{event_date}_{index}{file_extension}"
        photo_filename = f"{full_name}_{event_date}{file_extension}"
        photo_path = os.path.join(photo_folder, photo_filename)
        downloaded_photo = bot.download_file(photo_info.file_path)
        with open(photo_path, 'wb') as new_photo:
            new_photo.write(downloaded_photo)
        bot.send_message(message.chat.id, "Фото успешно сохранено(ы)")
    else:
        bot.send_message(message.chat.id, "Вы не отправили ни одного фото. Попробуйте еще раз")

# @bot.message_handler(content_types=['photo'])
# def save_photos(message):
#     full_name = "123"
#     event_date = "456"
#     description = "789"
#
#     file_info_1 = bot.get_file(message.photo[-1].file_id)
#     bot.send_message(message.chat.id, file_info_1)
#     downloaded_file = bot.download_file(file_info_1.file_path)
#
#     src = dir + '\\' + file_info_1.file_path.split('/')[-1]
#     bot.send_message(message.chat.id, src)
#     with open(src, 'wb') as new_file:
#         new_file.write(downloaded_file)


# @bot.message_handler(content_types=['document'])
# def save_photos(message):
#     full_name = "123"
#     event_date = "456"
#     description = "789"
#
#     chat_id = message.chat.id
#     photo_folder_name = f"{full_name}_{event_date}"
#     photo_folder = os.path.join("event_photos", photo_folder_name)
#     if not os.path.exists(photo_folder):
#         os.makedirs(photo_folder)
#
#     print(message, sep="\n=separator=\n", end="\n=end=\n")
#     print(type(message))

# for msg in message:
#     if msg.document:
#         for index, photo in enumerate(msg.document):
#             photo_id = photo.file_id
#             photo_info = bot.get_file(photo_id)
#             _, file_extension = os.path.splitext(photo.file_name)
#             photo_filename = f"{full_name}_{event_date}_{index}{file_extension}"
#             photo_path = os.path.join(photo_folder, photo_filename)
#             downloaded_photo = bot.download_file(photo_info.file_path)
#             with open(photo_path, 'wb') as new_photo:
#                 new_photo.write(downloaded_photo)
#         bot.send_message(chat_id, "Фотографии успешно сохранены.")
#     else:
#         bot.send_message(chat_id, "Вы не отправили ни одной фотографии. Пожалуйста, повторите попытку.")

# def save_photos(message):
#     full_name = "123"
#     event_date = "456"
#
#     chat_id = message.chat.id
#     photo_folder_name = f"{full_name}_{event_date}"
#     photo_folder = os.path.join("event_photos", photo_folder_name)
#     if not os.path.exists(photo_folder):
#         os.makedirs(photo_folder)
#
#     if message.document:
#         for index, photo in enumerate(message.document):
#             if photo.mime_type.startswith('image'):  # Проверяем, что это изображение
#                 photo_id = photo.file_id
#                 photo_info = bot.get_file(photo_id)
#                 file_extension = photo.file_name.split('.')[-1]  # Получаем расширение файла
#                 photo_filename = f"{full_name}_{event_date}_{index}.{file_extension}"
#                 photo_path = os.path.join(photo_folder, photo_filename)
#                 downloaded_photo = bot.download_file(photo_info.file_path)
#                 with open(photo_path, 'wb') as new_photo:
#                     new_photo.write(downloaded_photo)
#             else:
#                 bot.send_message(chat_id, f"Файл '{photo.file_name}'
#                 не является изображением и будет проигнорирован.")
#         bot.send_message(chat_id, "Фотографии успешно сохранены.")
#     else:
#         bot.send_message(chat_id,
#                          "Вы не отправили ни одного файла. Пожалуйста, отправьте файлы фотографий мероприятия.")
