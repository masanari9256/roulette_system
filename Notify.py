import requests
import os
from dotenv import load_dotenv

# .envの読み込み
load_dotenv()

def send_line_notify(notification_message):
    # LINEに通知する
    line_notify_token = os.environ['LINE_NOTIFY_TOKEN']
    line_notify_api = os.environ['LINE_NOTIFY_API']
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers=headers, data=data)


if __name__ == "__main__":
    send_line_notify("てすと")
