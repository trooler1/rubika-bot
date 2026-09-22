import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from rubka import Robot

PORT = int(os.getenv("PORT", 10000))

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_GUID = os.getenv("CHANNEL_GUID")


# جلوگیری از Sleep رندر
server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()


bot = Robot(token=TOKEN)


async def is_member(user_id):

    try:
        members = await bot.get_channel_members(CHANNEL_GUID)

        for member in members:
            if member.get("user_guid") == user_id:
                return True

        return False

    except Exception as e:
        print("MEMBER CHECK ERROR:", e)
        return False



@bot.on_message()
async def main(bot, message):

    user_id = message.chat_id

    print("USER:", user_id)

    status = await is_member(user_id)

    print("MEMBER:", status)


    if status:
        await message.reply(
            "✅ عضویت شما تایید شد"
        )

    else:
        await message.reply(
            "❌ هنوز عضو کانال نیستید\n\n"
            "ابتدا عضو شوید:\n"
            "https://rubika.ir/AMIRTROOLER"
        )


print("BOT STARTED")

bot.run()
