import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from rubka import Robot, Message


TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")


PORT = int(os.getenv("PORT", "10000"))


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass


def start_web_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    print(f"WEB SERVER STARTED ON PORT {PORT}")
    server.serve_forever()


threading.Thread(target=start_web_server, daemon=True).start()


bot = Robot(token=TOKEN)


@bot.on_message()
async def messages(bot: Robot, message: Message):
    print("================================")
    print("CHAT ID:", message.chat_id)
    print("TEXT:", message.text)
    print("================================")

    await message.reply(
        f"شناسه این چت:\n\n{message.chat_id}"
    )


print("BOT STARTED")
bot.run()
