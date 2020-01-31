import requests
import telepot
from datetime import datetime
import csv

#Request the Bit Coin prices from two exchanges: Bithumb in KRW and Bitfinex in USD
def coin_price():
    payload = {'key1': 'value1', 'key2': 'value2'}
    bt = requests.get('https://api.bithumb.com/public/ticker/BTC', params=payload)
    bt_json = bt.json()
    bt_price_KRW = bt_json.get("data").get("closing_price")

    bf = requests.get('https://api.bitfinex.com/v2/tickers?symbols=tBTCUSD')
    bf_json = bf.json()
    bf_price_USD = bf_json[0][1]
    send_message(bt_price_KRW, bf_price_USD)
    store_database(bt_price_KRW, bf_price_USD)

#make telegram bot
def send_message(bt, bf):
    with open('./database.csv', 'r') as file:
        lines = file.readlines()
        pre_bt = lines[len(lines)-1].split(',')[1]
        pre_bf = lines[len(lines) - 1].split(',')[2]
        pre_bf = pre_bf.replace('\n','')
    file.close()
    bt = round(float(bt),2)
    bf = round(float(bf),2)
    pre_bt = float(pre_bt)
    pre_bf = float(pre_bf)
    up_bt = round(bt - round(pre_bt,2),2)
    up_bf = round(bf - round(pre_bf,2),2)
    token = '925614271:AAHkV-7yVUux-r52PPUOeOEz8flSd3XqqwE'
    id = "882574133"
    bot = telepot.Bot(token)
    if up_bt >= 0:
        bt_ment = ", UP : " + str(int(up_bt)) + "\n"
    else:
        bt_ment = ", DOWN : " + str(int(up_bt)*(-1)) + "\n"
    if up_bf >= 0:
        bf_ment = ", UP : " + str(float(up_bf))
    else:
        bf_ment = ", DOWN : " + str(float(up_bf)*(-1))
    bot.sendMessage(id,"Bithumb-BTC-KRW : "+ str(int(bt)) + bt_ment +
                    "Bitfinex-BTC-USD : " + str(bf) + bf_ment)

#store database
def store_database(bt, bf):
    now = datetime.now()
    date = '%s-%s-%s' % (now.year, now.month, now.day)
    time = '%02d:%02d' % (now.hour, now.minute)
    time_stamp = date + "-" + time
    store = [time_stamp,bt, bf]
    with open('./database.csv', 'a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(store)
    file.close()

#aps shceduler
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(coin_price,'interval', seconds=60)


