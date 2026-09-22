import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from rubka import Robot

TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_GUID = os.getenv("CHANNEL_GUID", "")
PORT = int(os.getenv("PORT", "10000"))

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()

bot = Robot(token=TOKEN)

exec('async def start(bot, message):\n    joined = bot.check_join(CHANNEL_GUID, message.chat_id)\n    message.reply("✅ شما عضو کانال هستید!" if joined else "❌ شما عضو کانال نیستید!\n\nابتدا در کانال @AMIRTROOLER عضو شوید و دوباره /start را بزنید.")')

bot.on_message(commands=["start"])(start)

print("BOT STARTED")
bot.run()
