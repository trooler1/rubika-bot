```python
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from rubka import Robot, Message


# =========================
# تنظیمات
# =========================

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_GUID = os.getenv("CHANNEL_GUID")
PORT = int(os.getenv("PORT", "10000"))

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

if not CHANNEL_GUID:
    raise ValueError("CHANNEL_GUID is not set")


# =========================
# وب‌سرور برای Render
# =========================

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass


def start_web_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    print(f"WEB SERVER STARTED ON PORT {PORT}")
    server.serve_forever()


threading.Thread(
    target=start_web_server,
    daemon=True
).start()


# =========================
# ساخت ربات
# =========================

bot = Robot(token=TOKEN)


# =========================
# دستور /start
# =========================

@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):

    try:
        is_joined = bot.check_join(
            CHANNEL_GUID,
            message.chat_id
        )

        if is_joined:
            await message.reply(
                "✅ شما عضو کانال هستید.\n\n"
                "خوش آمدید 🌹"
            )
        else:
            await message.reply(
                "❌ برای استفاده از ربات ابتدا باید عضو کانال شوید.\n\n"
                "📢 کانال:\n"
                "@AMIRTROOLER\n\n"
                "بعد از عضویت دوباره /start را بفرستید."
            )

    except Exception as e:
        print("CHECK JOIN ERROR:", e)

        await message.reply(
            "⚠️ هنگام بررسی عضویت خطایی رخ داد.\n"
            "لطفاً چند لحظه بعد دوباره تلاش کنید."
        )


# =========================
# اجرای ربات
# =========================

print("BOT STARTED")
print("CHANNEL GUID:", CHANNEL_GUID)

bot.run()
```
