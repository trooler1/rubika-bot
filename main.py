import os
from rubka import Robot, Message

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Robot(token=TOKEN)


@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):
    await message.reply(
        "سلام 👋\n\n"
        "من ربات اکانت رایگان کالاف هستم 🎮\n\n"
        "اگه اکانت رایگان کالاف میخوای، "
        "کلمه «کالاف» رو بفرست."
    )


@bot.on_message()
async def messages(bot: Robot, message: Message):
    text = (message.text or "").strip()

    if "کالاف" in text:
        await message.reply(
            "✅ درخواستت ثبت شد!\n\n"
            "این بخش فعلاً آزمایشی است."
        )


print("🤖 Rubika bot is starting...")

bot.run()
