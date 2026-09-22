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

def check_member(bot, message):
user_id = str(message.chat_id)

```
try:
    method = None

    for name in dir(bot):
        low = name.lower()
        if "channel" in low and "member" in low and "all" in low:
            method = getattr(bot, name)
            break

    if method is None:
        message.reply("❌ متد بررسی اعضای کانال در این نسخه Rubka پیدا نشد.")
        return

    result = method(CHANNEL_GUID, search_text=user_id)

    text = str(result)

    if user_id in text:
        message.reply(
            "✅ عضویت شما تأیید شد!\n\n"
            "حالا می‌توانید از ربات استفاده کنید."
        )
    else:
        message.reply(
            "❌ شما هنوز عضو کانال نیستید.\n\n"
            "1️⃣ ابتدا عضو کانال شوید:\n"
            "https://rubika.ir/AMIRTROOLER\n\n"
            "2️⃣ سپس دوباره /start را بزنید."
        )

except Exception as e:
    message.reply(
        "⚠️ خطا در بررسی عضویت.\n\n"
        "لطفاً چند ثانیه بعد دوباره /start را بزنید."
    )
    print("JOIN CHECK ERROR:", repr(e))
```

@bot.on_message(commands=["start"])
def start(bot, message):
check_member(bot, message)

print("BOT STARTED")
print("CHANNEL:", CHANNEL_GUID)

bot.run()
