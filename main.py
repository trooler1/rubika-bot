import os

from rubka import Robot, Message

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Robot(token=TOKEN)


@bot.on_message()
async def get_channel_id(bot: Robot, message: Message):

    if message.is_channel:
        print("================================")
        print("CHANNEL GUID:")
        print(message.chat_id)
        print("================================")

        await message.reply(
            "✅ شناسه کانال دریافت شد.\n"
            "حالا Render Logs رو باز کن."
        )


print("🤖 Bot is running...")

bot.run()
