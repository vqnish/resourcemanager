mport psutil
import requests
import time


webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'

def get_cpu_usage():
    return psutil.cpu_percent()

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_network_usage():
    return psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

def send_to_discord(cpu_usage, ram_usage, network_usage):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "embeds": [
            {
                "title": "System Stats",
                "color": 8771498,
                "fields": [
                    {
                        "name": "CPU Usage",
                        "value": f"{cpu_usage}%",
                        "inline": True
                    },
                    {
                        "name": "RAM Usage",
                        "value": f"{ram_usage}%",
                        "inline": True
                    },
                    {
                        "name": "Network Usage",
                        "value": f"{network_usage} bytes",
                        "inline": True
                    }
                ]
            }
        ]
    }
    requests.post(webhook_url, headers=headers, json=data)

while True:
    cpu_usage = get_cpu_usage()
    ram_usage = get_ram_usage()
    network_usage = get_network_usage()
    send_to_discord(cpu_usage, ram_usage, network_usage)
    time.sleep(60)
