import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from rubka import Robot

PORT = int(os.getenv("PORT", 10000))

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_GUID = "c0Dyv860ea2948530b600134bf21467a"


# جلوگیری از خاموش شدن Render
server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)

threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()


bot = Robot(token=TOKEN)


@bot.on_message()
async def check_member(bot, message):

    user_id = message.chat_id

    print("----------------")
    print("USER:", user_id)
    print("CHANNEL:", CHANNEL_GUID)

    try:
        result = bot.check_join(
            CHANNEL_GUID,
            user_id
        )

        print("RESULT:", result)

        if result:
            await message.reply(
                "✅ عضویت شما تایید شد"
            )

        else:
            await message.reply(
                "❌ شما هنوز عضو کانال نیستید\n\n"
                "ابتدا عضو شوید:\n"
                "https://rubika.ir/AMIRTROOLER"
            )

    except Exception as e:
        print("ERROR:", repr(e))

        await message.reply(
            "⚠️ خطا در بررسی عضویت"
        )


print("BOT STARTED")

bot.run()
