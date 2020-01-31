import asyncio
import websockets
import json

async def run():
    uri = "wss://api.upbit.com/websocket/v1"
    async with websockets.connect(uri) as websocket:
        await websocket.send(
            '[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW-BTC"]},{"type":"orderbook","codes":["KRW-BTC"]}]')
        while(True):
            rcv = await websocket.recv()
            data = json.loads(rcv)
            if data['type'] == 'orderbook':
                val = data["orderbook_units"][0]
                print('ask_price :',val['ask_price'],',  bid_price :',val['bid_price'],',  ask_size :',val['ask_size'],',  bid_size : ',val['bid_size'])
            else:
                print('trade_price : ',data['trade_price'],',  trade_volume : ',data['trade_volume'],',  ask_bid : ',data['ask_bid'])

asyncio.get_event_loop().run_until_complete(run())import asyncio
import websockets
import json

async def run():
    uri = "wss://api.upbit.com/websocket/v1"
    async with websockets.connect(uri) as websocket:
        await websocket.send(
            '[{"ticket":"UNIQUE_TICKET"},{"type":"trade","codes":["KRW-BTC"]},{"type":"orderbook","codes":["KRW-BTC"]}]')
        while(True):
            rcv = await websocket.recv()
            data = json.loads(rcv)
            if data['type'] == 'orderbook':
                val = data["orderbook_units"][0]
                print('ask_price :',val['ask_price'],',  bid_price :',val['bid_price'],',  ask_size :',val['ask_size'],',  bid_size : ',val['bid_size'])
            else:
                print('trade_price : ',data['trade_price'],',  trade_volume : ',data['trade_volume'],',  ask_bid : ',data['ask_bid'])

asyncio.get_event_loop().run_until_complete(run())