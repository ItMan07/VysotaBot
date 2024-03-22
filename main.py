from loader import bot

import handlers

if __name__ == "__main__":
    print("[INFO] START")
    bot.remove_webhook()
    bot.infinity_polling()
    print(bot)
