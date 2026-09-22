import os
from rubka import Robot

TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_GUID = os.getenv("CHANNEL_GUID", "")

bot = Robot(token=TOKEN)

print("BOT STARTED")
print("CHANNEL:", CHANNEL_GUID)

bot.run()
