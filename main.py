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
# وب‌سرور Render
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
# ربات
# =========================

bot = Robot(token=TOKEN)


@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):

    print("START COMMAND FROM:", message.chat_id)

    try:
        joined = bot.check_join(
            CHANNEL_GUID,
            message.chat_id
        )

        print("CHECK JOIN RESULT:", joined)

        if joined:
            await message.reply(
                "✅ عضویت شما تأیید شد!\n\n"
                "🎉 خوش آمدید."
            )
        else:
            await message.reply(
                "❌ شما هنوز عضو کانال نیستید.\n\n"
                "📢 ابتدا عضو کانال شوید:\n"
                "@AMIRTROOLER\n\n"
                "سپس دوباره /start را بفرستید."
            )

    except Exception as e:
        print("CHECK JOIN ERROR:", repr(e))

        await message.reply(
            "⚠️ خطا در بررسی عضویت.\n"
            "لطفاً دوباره تلاش کنید."
        )


print("================================")
print("BOT STARTED")
print("CHANNEL GUID:", CHANNEL_GUID)
print("================================")

bot.run()
```
