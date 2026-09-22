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

def test_join(bot, message):
result = bot.check_join(CHANNEL_GUID, message.chat_id)
message.reply("RESULT = " + repr(result) + "\nCHAT_ID = " + str(message.chat_id) + "\nCHANNEL = " + CHANNEL_GUID)

bot.on_message(commands=["start"])(test_join)

print("BOT STARTED")
bot.run()
