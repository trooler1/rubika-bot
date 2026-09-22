import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from rubka import Robot

PORT = int(os.getenv("PORT", "10000"))
TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_GUID = os.getenv("CHANNEL_GUID", "")

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()

bot = Robot(token=TOKEN)

def test(bot, message):
methods = [x for x in dir(bot) if "member" in x.lower() or "channel" in x.lower()]
message.reply("متدهای پیدا شده:\n" + "\n".join(methods))

bot.on_message(commands=["start"])(test)

print("BOT STARTED")
bot.run()
