import os
import requests

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

username = "AMIRTROOLER"

url = f"https://botapi.rubika.ir/v3/{TOKEN}/getObjectByUsername"

response = requests.post(
    url,
    json={
        "username": username
    }
)

print("STATUS:", response.status_code)
print("RESULT:")
print(response.text)
