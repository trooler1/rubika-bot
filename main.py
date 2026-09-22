```python
import os
import random

from rubka import Robot, Message
from rubka.keypad import ChatKeypadBuilder

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = Robot(token=TOKEN)

# =========================
# تنظیمات کانال اسپانسر
# =========================

CHANNEL_USERNAME = "@AMIRTROOLER"

# بعداً GUID واقعی کانال را اینجا قرار می‌دهیم
CHANNEL_GUID = "CHANNEL_GUID_HERE"


# =========================
# اکانت‌های تست
# =========================

ACCOUNTS = [
    {
        "email": "testaccount1@example.com",
        "password": "TestPassword123"
    },
    {
        "email": "testaccount2@example.com",
        "password": "TestPassword456"
    },
    {
        "email": "testaccount3@example.com",
        "password": "TestPassword789"
    }
]


# =========================
# /start
# =========================

@bot.on_message(commands=["start"])
async def start(bot: Robot, message: Message):

    builder = ChatKeypadBuilder()

    keypad = (
        builder
        .row(
            builder.button("account", "🎮 اکانت رایگان"),
            builder.button("cp", "💎 سی‌پی رایگان")
        )
        .build()
    )

    await message.reply_keypad(
        "درود بر شما 🌹\n\n"
        "خیلی به ربات اکانت رایگان خوش اومدی! ❤️\n\n"
        "لطفاً یک گزینه رو انتخاب کن 👇",
        keypad
    )


# =========================
# پیام‌های معمولی
# =========================

@bot.on_message()
async def messages(bot: Robot, message: Message):

    text = (message.text or "").strip()

    # -------------------------
    # سی پی رایگان
    # -------------------------

    if text == "💎 سی‌پی رایگان":

        await message.reply(
            "❌ فعلاً این گزینه موجود نیست.\n\n"
            "به‌زودی فعالش می‌کنیم ❤️"
        )

    # -------------------------
    # اکانت رایگان
    # -------------------------

    elif text == "🎮 اکانت رایگان":

        await message.reply(
            "🎮 برای دریافت اکانت رایگان، ابتدا در کانال اسپانسر عضو شو.\n\n"
            f"📢 کانال اسپانسر:\n{CHANNEL_USERNAME}\n\n"
            "بعد از عضویت، کلمه «بررسی» رو بفرست. ✅"
        )

    # -------------------------
    # بررسی عضویت
    # -------------------------

    elif text == "بررسی":

        if CHANNEL_GUID == "CHANNEL_GUID_HERE":

            await message.reply(
                "⚠️ بررسی عضویت هنوز تنظیم نشده.\n\n"
                "باید GUID کانال اسپانسر رو داخل کد قرار بدیم."
            )
            return

        try:

            joined = bot.check_join(
                CHANNEL_GUID,
                message.chat_id
            )

            if not joined:

                await message.reply(
                    "❌ هنوز عضو کانال اسپانسر نشدی.\n\n"
                    f"اول عضو شو:\n{CHANNEL_USERNAME}\n\n"
                    "بعد دوباره «بررسی» رو بفرست."
                )

                return

            # -------------------------
            # انتخاب تصادفی اکانت
            # -------------------------

            account = random.choice(ACCOUNTS)

            await message.reply(
                "✅ عضویت شما تأیید شد!\n\n"
                "🎮 اطلاعات اکانت:\n\n"
                f"📧 ایمیل:\n{account['email']}\n\n"
                f"🔐 رمز:\n{account['password']}\n\n"
                "⚠️ این اطلاعات فقط برای تست ربات هستند."
            )

        except Exception as e:

            await message.reply(
                "⚠️ هنگام بررسی عضویت مشکلی پیش آمد.\n"
                "لطفاً دوباره تلاش کن."
            )

            print("Membership check error:", e)


print("🤖 Rubika bot is starting...")

bot.run()
```
