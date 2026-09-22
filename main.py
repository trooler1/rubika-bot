import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from rubka import Robot, Message

TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_GUID = os.getenv("CHANNEL_GUID", "")
PORT = int(os.getenv("PORT", "10000"))

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()

print("WEB SERVER STARTED:", PORT)
print("CHANNEL:", CHANNEL_GUID)

bot = Robot(token=TOKEN)

@bot.on_message(commands=["start"])
def start(bot, message):
if bot.check_join(CHANNEL_GUID, message.chat_id):
message.reply("✅ شما عضو کانال هستید!\n\nخوش آمدید 🌹")
else:
message.reply("❌ شما هنوز عضو کانال نیستید.\n\nابتدا در کانال عضو شوید و سپس دوباره /start را بزنید.")

print("BOT STARTED")

bot.run()
