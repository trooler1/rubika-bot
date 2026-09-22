import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests
from rubka import Robot, Message


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")


# =========================
# Render health check
# =========================

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def log_message(self, format, *args):
        pass


def run_server():
    port = int(os.getenv("PORT", "10000"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"HTTP server running on port {port}")
    server.serve_forever()


threading.Thread(target=run_server, daemon=True).start()


# =========================
# Rubika bot
# =========================

bot = Robot(token=TOKEN)


# =========================
# پیدا کردن GUID کانال
# =========================

def find_channel_guid():

    url = f"https://botapi.rubika.ir/v3/{TOKEN}/getObjectByUsername"

    data = {
        "username": "AMIRTROOLER"
    }

    try:

        response = requests.post(
            url,
            json=data,
            timeout=15
        )

        print("========== CHANNEL LOOKUP ==========")
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        print("====================================")

    except Exception as e:

        print("CHANNEL LOOKUP ERROR:", e)


find_channel_guid()


# =========================
# تست ربات
# =========================

@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):

    await message.reply(
        "سلام 👋\n\n"
        "ربات روشن است.\n\n"
        "برای تست سیستم تشخیص عضویت، بعداً بررسی را اضافه می‌کنیم."
    )


print("================================")
print("🤖 RUBIKA BOT STARTED")
print("================================")

bot.run()
