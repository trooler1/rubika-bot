import os
from rubka import Robot, Message

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Robot(token=TOKEN)


@bot.on_message()
async def messages(bot: Robot, message: Message):
    print("================================")
    print("CHAT ID:", message.chat_id)
    print("TEXT:", message.text)
    print("================================")

    await message.reply(
        f"شناسه این چت:\n\n{message.chat_id}"
    )


print("BOT STARTED")
bot.run()
