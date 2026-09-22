import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from rubka import Robot

PORT = int(os.getenv("PORT", 10000))

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_GUID = os.getenv("CHANNEL_GUID")

# برای Render
server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()


bot = Robot(token=TOKEN)


@bot.on_message()
def main(bot, message):

    try:
        user = message.chat_id

        print("USER:", user)
        print("CHANNEL:", CHANNEL_GUID)

        joined = bot.check_join(
            CHANNEL_GUID,
            user
        )

        print("JOIN RESULT:", joined)

        if joined:
            message.reply(
                "✅ عضویت شما تایید شد"
            )
        else:
            message.reply(
                "❌ شما عضو کانال نیستید\n\n"
                "ابتدا عضو شوید:\n"
                "https://rubika.ir/AMIRTROOLER"
            )

    except Exception as e:
        print("ERROR:", repr(e))
        message.reply(
            "خطا در بررسی عضویت"
        )


print("BOT STARTED")
bot.run()
