import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from rubka import Robot, Message
from rubka.keypad import ChatKeypadBuilder


# =========================
# تنظیمات
# =========================

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

CHANNEL_GUID = os.getenv("CHANNEL_GUID")

if not CHANNEL_GUID:
    raise ValueError("CHANNEL_GUID is not set")

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
        pass


def start_web_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)

    print(f"🌐 Web server started on port {PORT}")

    server.serve_forever()


threading.Thread(
    target=start_web_server,
    daemon=True
).start()


# =========================
# دکمه بررسی عضویت
# =========================

def membership_keypad():

    builder = ChatKeypadBuilder()

    keypad = (
        builder
        .row(
            builder.button(
                id="check_membership",
                text="🔎 بررسی عضویت"
            )
        )
        .build()
    )

    return keypad


# =========================
# /start
# =========================

@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):

    await message.reply_keypad(
        "سلام 👋\n\n"
        "ربات روشن است. 🤖\n\n"
        "برای استفاده از ربات ابتدا در کانال زیر عضو شوید:\n\n"
        "📢 @AMIRTROOLER\n\n"
        "بعد از عضویت روی دکمه زیر بزنید:",
        membership_keypad()
    )


# =========================
# دریافت پیام بررسی
# =========================

@bot.on_message()
async def messages(bot: Robot, message: Message):

    text = (message.text or "").strip()

    print("================================")
    print("📩 پیام جدید دریافت شد")
    print(f"👤 Chat ID: {message.chat_id}")
    print(f"📝 Text: {text}")
    print("================================")

    if text != "🔎 بررسی عضویت":
        return

    print("🔎 شروع بررسی عضویت...")
    print(f"📢 Channel GUID: {CHANNEL_GUID}")
    print(f"👤 User GUID: {message.chat_id}")

    try:

        result = bot.check_join(
            CHANNEL_GUID,
            message.chat_id
        )

        print(f"📌 check_join result: {result}")

        if result:

            await message.reply(
                "✅ عضویت شما تأیید شد.\n\n"
                "شما عضو کانال @AMIRTROOLER هستید. 🎉"
            )

        else:

            await message.reply_keypad(
                "❌ هنوز عضو کانال نیستید.\n\n"
                "ابتدا در کانال @AMIRTROOLER عضو شوید، "
                "سپس دوباره روی دکمه «🔎 بررسی عضویت» بزنید.",
                membership_keypad()
            )

    except Exception as e:

        print("❌ خطا در check_join")
        print(f"نوع خطا: {type(e).__name__}")
        print(f"متن خطا: {e}")

        await message.reply(
            "❌ هنگام بررسی عضویت خطایی رخ داد.\n\n"
            "لطفاً دوباره تلاش کنید."
        )


# =========================
# شروع ربات
# =========================

print("================================")
print("🤖 Rubika bot is starting...")
print(f"📢 Channel: @{CHANNEL_USERNAME}")
print(f"📌 Channel GUID: {CHANNEL_GUID}")
print("================================")

bot.run()
