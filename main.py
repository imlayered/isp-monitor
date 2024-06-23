import time
import requests
import json
import datetime
import signal
import sys
from threading import Event

# Made by Auri (github.com/isp-monitor)
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

url = config['url']
interval = config['interval']
discord_webhook_url = config['discord_webhook_url']

stop_event = Event()

def send_discord_message(message):
    data = {
        "content": message
    }
    response = requests.post(discord_webhook_url, json=data)
    if response.status_code != 204:
        print(f"Failed to send message to Discord: {response.status_code}, {response.text}")

def ping_website(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def signal_handler(sig, frame):
    send_discord_message("Stopped monitoring.")
    print("Stopped monitoring.")
    stop_event.set()
    sys.exit(0)

def main():
    send_discord_message("Started monitoring.")
    print("Started monitoring.")
    
    connection_lost_time = None
    
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        while not stop_event.wait(interval):
            if ping_website(url):
                if connection_lost_time is not None:
                    down_time = datetime.datetime.now() - connection_lost_time
                    send_discord_message(f"Connection failed for {down_time}. Connection restored as of {datetime.datetime.now()}.")
                    print(f"Connection failed for {down_time}. Connection restored as of {datetime.datetime.now()}.")
                    connection_lost_time = None
            else:
                if connection_lost_time is None:
                    connection_lost_time = datetime.datetime.now()
    except KeyboardInterrupt:
        signal_handler(signal.SIGTERM, None)

if __name__ == "__main__":
    main()
