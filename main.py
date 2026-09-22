import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from rubka import Robot, Message
from rubka.keypad import Keypad, Button


# =========================
# تنظیمات
# =========================

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

CHANNEL_USERNAME = "AMIRTROOLER"

bot = Robot(token=TOKEN)


# =========================
# پورت Render
# =========================

PORT = int(os.getenv("PORT", "10000"))


class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Rubika bot is running")

    def log_message(self, format, *args):
        return


def start_web_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    print(f"🌐 Web server started on port {PORT}")
    server.serve_forever()


threading.Thread(
    target=start_web_server,
    daemon=True
).start()


# =========================
# پیدا کردن GUID کانال
# =========================

def get_channel_guid():
    print("🔎 در حال پیدا کردن GUID کانال...")
    print(f"📢 Username: @{CHANNEL_USERNAME}")

    try:
        # اگر نسخه Rubka این متد را در Robot ارائه کند
        result = bot.get_object_by_username(CHANNEL_USERNAME)

        print("📦 نتیجه دریافت شد:")
        print(result)

        if isinstance(result, dict):
            guid = result.get("object_guid")

            if guid:
                print(f"✅ Channel GUID: {guid}")
                return guid

            obj = result.get("object")
            if isinstance(obj, dict):
                guid = obj.get("object_guid")

                if guid:
                    print(f"✅ Channel GUID: {guid}")
                    return guid

        print("❌ از نتیجه، GUID کانال پیدا نشد.")
        return None

    except Exception as e:
        print("❌ خطا هنگام پیدا کردن GUID کانال:")
        print(type(e).__name__, str(e))
        return None


CHANNEL_GUID = get_channel_guid()


# =========================
# /start
# =========================

@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):

    keypad = Keypad(
        rows=[
            [
                Button(text="🔎 بررسی عضویت")
            ]
        ]
    )

    await message.reply(
        "سلام 👋\n\n"
        "ربات روشن است.\n\n"
        "برای تست سیستم تشخیص عضویت، "
        "ابتدا در کانال زیر عضو شوید:\n\n"
        "📢 @AMIRTROOLER\n\n"
        "بعد روی «🔎 بررسی عضویت» بزنید.",
        keypad=keypad
    )


# =========================
# بررسی عضویت
# =========================

@bot.on_message()
async def check_membership(bot: Robot, message: Message):

    text = (message.text or "").strip()

    if text != "🔎 بررسی عضویت":
        return

    print("================================")
    print("🔎 درخواست بررسی عضویت دریافت شد")
    print(f"👤 Chat ID: {message.chat_id}")
    print(f"📢 Channel GUID: {CHANNEL_GUID}")
    print("================================")

    if not CHANNEL_GUID:
        await message.reply(
            "❌ GUID کانال هنوز پیدا نشده.\n\n"
            "لطفاً لاگ Render را بررسی کنید."
        )
        return

    try:

        is_member = bot.check_join(
            CHANNEL_GUID,
            message.chat_id
        )

        print(f"📌 نتیجه check_join: {is_member}")

        if is_member:
            await message.reply(
                "✅ عضویت شما تأیید شد.\n\n"
                "شما عضو کانال هستید."
            )
        else:
            await message.reply(
                "❌ شما هنوز عضو کانال نیستید.\n\n"
                "ابتدا در @AMIRTROOLER عضو شوید و دوباره "
                "روی «🔎 بررسی عضویت» بزنید."
            )

    except Exception as e:

        print("❌ خطا در check_join:")
        print(type(e).__name__, str(e))

        await message.reply(
            "❌ هنگام بررسی عضویت خطایی رخ داد.\n\n"
            "لاگ Render را بررسی کنید."
        )


# =========================
# اجرای ربات
# =========================

print("================================")
print("🤖 Rubika bot is starting...")
print(f"📢 Channel: @{CHANNEL_USERNAME}")
print("================================")

bot.run()
