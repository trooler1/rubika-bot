import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from rubka import Robot

TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_GUID = os.getenv("CHANNEL_GUID", "")
PORT = int(os.getenv("PORT", "10000"))

if not TOKEN:
raise ValueError("BOT_TOKEN is not set")

if not CHANNEL_GUID:
raise ValueError("CHANNEL_GUID is not set")

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()

print("WEB SERVER STARTED ON PORT", PORT)
print("CHANNEL:", CHANNEL_GUID)

bot = Robot(token=TOKEN)

print("BOT STARTED")

bot.run()
