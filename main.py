import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from rubka import Robot

PORT = int(os.getenv("PORT", 10000))

TOKEN = os.getenv("BOT_TOKEN")

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)

threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()


bot = Robot(token=TOKEN)


@bot.on_message()
def test(bot, message):

    print("========== NEW MESSAGE ==========")
    print("CHAT ID:", message.chat_id)

    try:
        print("FULL MESSAGE:")
        print(message)

    except Exception as e:
        print("ERROR:", e)

    message.reply(
        "آیدی دریافت شد:\n" + str(message.chat_id)
    )


print("BOT STARTED")

bot.run()
