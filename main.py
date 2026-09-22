import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from rubka import Robot
from rubka.context import Message


PORT = int(os.getenv("PORT", 10000))

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_LINK = "https://rubika.ir/AMIRTROOLER"

# GUID کانال
CHANNEL_GUID = "c0Dyv860ea2948530b600134bf21467a"


# برای Render
server = HTTPServer(
    ("0.0.0.0", PORT),
    SimpleHTTPRequestHandler
)

threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()


if not TOKEN:
    raise Exception("BOT_TOKEN تنظیم نشده است")


bot = Robot(TOKEN)


# ذخیره تعداد درخواست کاربران
users = {}


@bot.on_message()
async def main(bot, message: Message):

    user = message.chat_id
    text = message.text.strip()

    if user not in users:
        users[user] = 0


    # شروع ربات
    if text == "/start":

        await message.reply(
            "درود 👋🔥\n\n"
            "برای دریافت اکانت رایگان یا سی پی رایگان، "
            "یکی از متن های زیر را تایپ کنید و برای بات ارسال کنید 👇\n\n"
            "🎁 اکانت رایگان\n"
            "💎 سی پی رایگان\n\n"
            "بعد از ارسال درخواست، مراحل دریافت برای شما نمایش داده می‌شود ✅"
        )

        return



    # درخواست اکانت یا سی پی
    if text in ["اکانت رایگان", "سی پی رایگان"]:

        users[user] += 1

        print("USER:", user)
        print("REQUEST:", text)
        print("TRY:", users[user])


        # بررسی عضویت
        try:
            joined = await bot.check_join(
                CHANNEL_GUID,
                user
            )

        except Exception as e:
            print("CHECK JOIN ERROR:", e)
            joined = False



        if not joined and users[user] < 6:

            await message.reply(
                "❌ هنوز عضو کانال نشدی\n\n"
                "اول داخل کانال زیر عضو شو:\n\n"
                f"{CHANNEL_LINK}\n\n"
                f"تلاش شما: {users[user]} از 6"
            )

            return



        # بعد از 6 بار
        await message.reply(
            "🎉 درخواست شما تایید شد\n\n"
            "🎁 اطلاعات اکانت تستی:\n\n"
            "📧 Gmail:\n"
            "test.account@gmail.com\n\n"
            "🔑 Password:\n"
            "Test123456\n\n"
            "⚠️ این اطلاعات فقط برای تست سیستم است."
        )

        return



    # پیام های دیگر

    await message.reply(
        "❌ دستور نامعتبر است\n\n"
        "یکی از این ها را ارسال کن:\n\n"
        "🎁 اکانت رایگان\n"
        "💎 سی پی رایگان"
    )



print("BOT STARTED")

bot.run()
