#https://hatpub.tistory.com/61


import urllib.request
import json
import requests
import schedule
import time


# 반복될 작업을 함수로 정의
def scd():
    # API 링크 가져와서 data 변수에 담기
    with urllib.request.urlopen("https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&count=1&reverse=true") as url:
        data = url.read()
    # json 데이터로 j 변수에 담기
    j = json.loads(data)

    # teleurl 변수에 텔레그램 botfather 한테 받은 자신의 API 넣기
    teleurl = "https://api.telegram.org/bot925614271:AAHkV-7yVUux-r52PPUOeOEz8flSd3XqqwE/sendMessage"

    # 챗 id 와 symbol : price 값을 텔레그램에 보내기
    params = {'chat_id': '-1001243756825', 'text': j[0]["symbol"] + " : " + str(j[0]["price"])}

    # 텔레그램으로 메시지 전송
    res = requests.get(teleurl, params=params)


# 스케쥴 설정 매분마다 실행
schedule.every().minute.do(scd)

# while 문을 사용하여 스케쥴러 실행
while 1:
    schedule.run_pending()
    time.sleep(2)
