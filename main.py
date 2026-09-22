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

    user_id = message.chat_id

    print("USER:", user_id)
    print("CHANNEL:", CHANNEL_GUID)

    try:
        print(
            [
                x for x in dir(bot)
                if "member" in x.lower()
                or "channel" in x.lower()
                or "join" in x.lower()
            ]
        )

        await message.reply("تست انجام شد، لاگ را ببین")

    except Exception as e:
        print("ERROR:", e)


print("BOT STARTED")

bot.run()
