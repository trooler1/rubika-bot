import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from rubka import Robot
from rubka.context import Message

PORT = int(os.getenv("PORT", 10000))

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_LINK = "https://rubika.ir/AMIRTROOLER"

CHANNEL_GUID = "c0Dyv860ea2948530b600134bf21467a"


# جلوگیری از خاموش شدن Render
server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)

threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()


bot = Robot(TOKEN)


users = {}


@bot.on_message()
async def main(bot, message: Message):

    user = message.chat_id
    text = message.text.strip()

    if user not in users:
        users[user] = 0


    # استارت
    if text == "/start":

        await message.reply(
            "درود 👋\n\n"
            "برای دریافت اکانت و سی پی رایگان "
            "یکی از گزینه های زیر را تایپ کنید و برای بات ارسال کنید >>>\n\n"
            "🎁 اکانت رایگان\n"
            "💎 سی پی رایگان"
        )
        return


    if text in ["اکانت رایگان", "سی پی رایگان"]:

        users[user] += 1

        try:
            joined = await bot.check_join(
                CHANNEL_GUID,
                user
            )
        except:
            joined = False


        if not joined:

            if users[user] < 6:

                await message.reply(
                    "❌ هنوز عضو کانال نشدی\n\n"
                    "اول عضو شو:\n"
                    f"{CHANNEL_LINK}\n\n"
                    f"تلاش {users[user]} از 6"
                )
                return


        # بعد از بار ششم
        await message.reply(
            "🎉 درخواست شما تایید شد\n\n"
            "اطلاعات تستی:\n\n"
            "📧 Gmail:\n"
            "test.account@example.com\n\n"
            "🔑 Password:\n"
            "Test123456\n\n"
            "."
        )

        return


    await message.reply(
        "لطفا یکی از گزینه ها را انتخاب کن:\n\n"
        "🎁 اکانت رایگان\n"
        "💎 سی پی رایگان"
    )


print("BOT STARTED")

bot.run()
