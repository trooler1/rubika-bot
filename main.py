import os
import threading
import asyncio
import requests
from http.server import HTTPServer, SimpleHTTPRequestHandler

from rubka import Robot
from rubka.context import Message


PORT = int(os.getenv("PORT", 10000))

TOKEN = os.getenv("BOT_TOKEN")

SELF_URL = "https://rubika-bot-9i1m.onrender.com"


CHANNEL_LINK = "https://rubika.ir/AMIRTROOLER"

CHANNEL_GUID = "c0Dyv860ea2948530b600134bf21467a"



# وب سرور برای Render
server = HTTPServer(
    ("0.0.0.0", PORT),
    SimpleHTTPRequestHandler
)

threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()



bot = Robot(TOKEN)



# بیدار نگه داشتن سرویس
async def keep_alive():

    while True:

        try:
            r = requests.get(SELF_URL, timeout=10)
            print("KEEP ALIVE:", r.status_code)

        except Exception as e:
            print("KEEP ERROR:", e)

        await asyncio.sleep(300)



users = {}



@bot.on_message()
async def main(bot, message: Message):

    user = message.chat_id
    text = message.text.strip()


    if user not in users:
        users[user] = 0



    if text == "/start":

        await message.reply(
            "درود 👋🔥\n\n"
            "برای دریافت اکانت رایگان یا سی پی رایگان، "
            "یکی از متن های زیر را تایپ کنید و ارسال کنید 👇\n\n"
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

        except Exception as e:

            print("JOIN ERROR:", e)
            joined = False



        if not joined and users[user] < 6:

            await message.reply(
                "❌ هنوز عضو کانال نیستی\n\n"
                "اول عضو شو:\n"
                f"{CHANNEL_LINK}\n\n"
                f"تلاش: {users[user]} از 6"
            )

            return



        await message.reply(
            "🎉 درخواست تایید شد\n\n"
            "🎁 اکانت تستی:\n\n"
            "📧 Email:\n"
            "test@gmail.com\n\n"
            "🔑 Password:\n"
            "12345678\n\n"
            "موفق باشی ✅"
        )

        return



    await message.reply(
        "یکی از این دو را ارسال کن:\n\n"
        "🎁 اکانت رایگان\n"
        "💎 سی پی رایگان"
    )




async def run():

    asyncio.create_task(
        keep_alive()
    )

    print("BOT STARTED")

    bot.run()



asyncio.run(run())
