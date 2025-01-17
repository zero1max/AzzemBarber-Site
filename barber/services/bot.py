import requests
from urllib.parse import quote
from datetime import datetime

def send_msg(*args):
    token = "7094074130:AAGTo6lf2jitG5crHhO6pxsUV2KBn1FbIc0"  # Bot token
    user_id = "5471452269"  # User ID

    message = (
    f"<b>📅 Sana:</b> {datetime.now().strftime('%d/%m/%Y')}\n"
    f"<b>⏰ Vaqt:</b> {datetime.now().strftime('%H:%M:%S')}\n"
    f"<b>🔹 Ma'lumot:</b> {', '.join(map(str, args))}")
    encoded_message = quote(message)  # Maxsus belgilarni kodlash

    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={encoded_message}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())
