import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from rubka import Robot

PORT = int(os.getenv("PORT", 10000))

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_GUID = os.getenv("CHANNEL_GUID")


server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()


bot = Robot(token=TOKEN)


@bot.on_message()
async def main(bot, message):

    try:
        user_id = message.chat_id

        print("USER:", user_id)
        print("CHANNEL:", CHANNEL_GUID)

        result = await bot.check_join(
            CHANNEL_GUID,
            user_id
        )

        print("JOIN RESULT:", result)

        if result:
            await message.reply(
                "✅ عضویت شما تایید شد"
            )
        else:
            await message.reply(
                "❌ شما عضو کانال نیستید\n\n"
                "اول عضو شوید:\n"
                "https://rubika.ir/AMIRTROOLER"
            )

    except Exception as e:
        print("ERROR:", repr(e))

        await message.reply(
            "خطا در بررسی عضویت"
        )


print("BOT STARTED")

bot.run()
