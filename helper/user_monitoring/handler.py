from datetime import datetime
from zoneinfo import ZoneInfo
import json
import os

def read_data():
    with open("./data/DbUser.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def user_monitoring():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        data = read_data()
        time_wita = datetime.now(ZoneInfo("Asia/Makassar")).strftime("%d-%m-%Y %H:%M:%S %Z")
        duration = []
        for i in data: duration.append(i['duration'])

        average_duration = sum(duration) / len(duration)

        print("-" * 74)
        print(f"{'Total active users':<25}: {len(data):<10} {time_wita:>35}")
        print(f"{'Average user duration':<25}: {average_duration:<10}")
        print("-" * 74)

        print(f"{'ID':<5} | {'Nama':<15} | {'Duration':<10} | {"Time_start":<15} | {"Time_finish":<15} |")
        print("-" * 74)

        for item in data:
            print(f"{item['id']:<5} | {item['name']:<15} | {item['duration']:<10} | {item['time_start']:<15} | {item['time_finish']:<15} |")

        print("-" * 74)
            
    except Exception as err:
        print(err)