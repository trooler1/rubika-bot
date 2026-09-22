import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from rubka import Robot, Message

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_GUID = os.getenv("CHANNEL_GUID")
PORT = int(os.getenv("PORT", "10000"))

TOKEN = TOKEN or ""
CHANNEL_GUID = CHANNEL_GUID or ""

class HealthHandler(BaseHTTPRequestHandler):
def do_GET(self):
self.send_response(200)
self.end_headers()
self.wfile.write(b"OK")

```
def log_message(self, format, *args):
    pass
```

def start_web_server():
server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
print("WEB SERVER STARTED ON PORT", PORT)
server.serve_forever()

threading.Thread(target=start_web_server, daemon=True).start()

bot = Robot(token=TOKEN)

@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):
print("START COMMAND FROM:", message.chat_id)

```
joined = bot.check_join(
    CHANNEL_GUID,
    message.chat_id
)

print("CHECK JOIN RESULT:", joined)

text = (
    "✅ عضویت شما تأیید شد!\n\n"
    "🎉 خوش آمدید."
    if joined
    else
    "❌ شما هنوز عضو کانال نیستید.\n\n"
    "📢 ابتدا عضو کانال شوید:\n"
    "@AMIRTROOLER\n\n"
    "بعد از عضویت دوباره /start را بفرستید."
)

await message.reply(text)
```

print("================================")
print("BOT STARTED")
print("CHANNEL GUID:", CHANNEL_GUID)
print("================================")

bot.run()
