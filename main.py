import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from rubka import Robot

PORT = int(os.getenv("PORT", "10000"))
TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_GUID = os.getenv("CHANNEL_GUID", "")

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()

print("PORT OK")
print("TOKEN OK:", bool(TOKEN))
print("CHANNEL OK:", bool(CHANNEL_GUID))

bot = Robot(token=TOKEN)

print("BOT CREATED")
bot.run()
