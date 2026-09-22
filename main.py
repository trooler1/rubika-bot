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

bot.on_message(commands=["start"])(lambda bot, message: message.reply("✅ شما عضو کانال هستید!" if bot.check_join(CHANNEL_GUID, message.chat_id) else "❌ شما عضو کانال نیستید!\n\nابتدا در کانال @AMIRTROOLER عضو شوید و دوباره /start را بزنید."))

print("BOT STARTED")
bot.run()
