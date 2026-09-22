```python
import os
from rubka import Robot, Message
from rubka.keypad import Keypad, Button

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Robot(token=TOKEN)


@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):
    keypad = Keypad(
        rows=[
            [
                Button(text="🎮 اکانت رایگان کالاف"),
            ],
            [
                Button(text="📢 کانال ما"),
            ]
        ]
    )

    await message.reply(
        "درود بر شما 🌹\n\n"
        "خیلی خوش آمدید ❤️\n\n"
        "لطفاً یک گزینه را انتخاب کنید 👇",
        keypad=keypad
    )


@bot.on_message()
async def messages(bot: Robot, message: Message):
    text = (message.text or "").strip()

    if text == "🎮 اکانت رایگان کالاف":
        await message.reply(
            "🎮 اکانت رایگان کالاف\n\n"
            "این بخش به‌زودی فعال می‌شود."
        )

    elif text == "📢 کانال ما":
        await message.reply(
            "📢 کانال ما\n\n"
            "لینک کانال به‌زودی اضافه می‌شود."
        )


print("🤖 Rubika bot is starting...")

bot.run()
```
