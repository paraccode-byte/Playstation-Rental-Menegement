from datetime import datetime
from zoneinfo import ZoneInfo
import json
import os

def read_data(p):
    if p == 'user':
        with open("./data/DbUser.json", "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        with open("./data/finance_data.json", "r", encoding="utf-8") as file:
            return json.load(file)
        
def financial_report():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        data_user = read_data('user')
        data_finance = read_data("finance")
        time_wita = datetime.now(ZoneInfo("Asia/Makassar")).strftime("%d-%m-%Y %H:%M:%S %Z")
        duration = []
        for i in data_user: duration.append(i['duration'])
        duration = sum(duration)

        expenditure = f"Rp{(data_finance["hpp"] * duration):,}".replace(",", ".")
        income = f"Rp{(data_finance["selling_price"] * duration):,}".replace(",", ".")
        profit = f"Rp{((data_finance["selling_price"] * duration) - (data_finance["hpp"] * duration)):,}".replace(",", ".")
        margin = f"{(data_finance["hpp"] / data_finance["selling_price"] * 100):.2f}%"
        
        print("-" * 74)
        print(f"{'Total expenditure':<25}: {expenditure} {time_wita:>35}")
        print(f"{'Total income':<25}: {income}")
        print(f"{'Total profit':<25}: {profit}")
        print('')
        print(f"{'Cost per product':<25}: {f"Rp{data_finance['hpp']:,}".replace(",", ".")}")
        print(f"{'Capital per product':<25}: {f"Rp{data_finance['selling_price']:,}".replace(",", ".")}")
        print(f"{'Profit per product':<25}: {f"Rp{(data_finance['selling_price'] - data_finance['hpp']):,}".replace(",", ".")}")
        print(f"{'Margin':<25}: {margin}")
        print("-" * 74)
    except Exception as err:
        print(err)