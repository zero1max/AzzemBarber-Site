import requests
from urllib.parse import quote
from datetime import datetime

def send_msg(*args):
    token = "BOT_TOKEN" 
    user_id = "YOUR_USER_ID"  

    message = (
    f"<b>📅 Sana:</b> {datetime.now().strftime('%d/%m/%Y')}\n"
    f"<b>⏰ Vaqt:</b> {datetime.now().strftime('%H:%M:%S')}\n"
    f"<b>🔹 Ma'lumot:</b> {', '.join(map(str, args))}")
    encoded_message = quote(message) 

    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user_id}&text={encoded_message}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())
