import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from rubka import Robot, Message

TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_GUID = os.getenv("CHANNEL_GUID", "")
PORT = int(os.getenv("PORT", "10000"))

server = HTTPServer(
("0.0.0.0", PORT),
BaseHTTPRequestHandler
)

threading.Thread(
target=server.serve_forever,
daemon=True
).start()

print("WEB SERVER STARTED")

bot = Robot(token=TOKEN)

@bot.on_message(commands=["start"])
async def start(bot, message):
print("START COMMAND:", message.chat_id)

```
joined = bot.check_join(
    CHANNEL_GUID,
    message.chat_id
)

print("JOIN RESULT:", joined)

await message.reply(
    "✅ عضویت شما تأیید شد!\n\n🎉 خوش آمدید."
    if joined
    else
    "❌ شما عضو کانال نیستید.\n\n📢 ابتدا عضو شوید:\n@AMIRTROOLER\n\nبعد دوباره /start بفرستید."
)
```

print("BOT STARTED")
print("CHANNEL:", CHANNEL_GUID)

bot.run()
