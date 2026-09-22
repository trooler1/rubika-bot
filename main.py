import os
from rubka import Robot, Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Robot(token=TOKEN)

@bot.on_message()
def handle_message(bot: Robot, message: Message):
    text = (message.text or "").strip()

    if text == "/start":
        message.reply(
            "سلام 👋\n\n"
            "من ربات اکانت رایگان کالاف هستم 🎮\n\n"
            "برای دریافت اکانت، کلمه «کالاف» رو بفرست."
        )

    elif "کالاف" in text:
        message.reply(
            "✅ درخواستت ثبت شد!\n\n"
            "فعلاً این بخش تستی است."
        )

bot.run()
