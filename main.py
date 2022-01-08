
import asyncio
import websockets
import requests
import json
import time

URL = "https://factorio.zone/api/user/login"
sURL = "https://factorio.zone/api/instance/start"
USER_TOKEN = "KEaZqViTE9RUDIMzx0RLO29W"

async def hello():
    uri = "wss://factorio.zone/ws"
    async with websockets.connect(uri) as websocket:

        await websocket.send("")
        secret = await websocket.recv()
        secret = json.loads(secret)
        secret = secret["secret"]
        #print(f"> secret: {secret}")
        log_in(secret)
        wa_result = []
        is_server_on = True
        try:
            wsr = await asyncio.wait_for(websocket.recv(), timeout=10)
            wa_result.append(wsr)
            wsr = await asyncio.wait_for(websocket.recv(), timeout=10)
            wa_result.append(wsr)
            wsr = await asyncio.wait_for(websocket.recv(), timeout=10)
            wa_result.append(wsr)
            wsr = await asyncio.wait_for(websocket.recv(), timeout=10)
            wa_result.append(wsr)
            wsr = await asyncio.wait_for(websocket.recv(), timeout=10)
            wa_result.append(wsr)
            wsr = await asyncio.wait_for(websocket.recv(), timeout=10)
            wa_result.append(wsr)
            wsr = await asyncio.wait_for(websocket.recv(), timeout=10)
            wa_result.append(wsr)
            wsr = await asyncio.wait_for(websocket.recv(), timeout=5)
            wa_result.append(wsr)
        except asyncio.TimeoutError:
            #print('timeout!')
            is_server_on = False

        if is_server_on:
            #print(wa_result)
            server_ip = json.loads(wa_result[5])
            server_ip = server_ip['socket']
            print('server is running\nip:')
            print(server_ip)
        else:
            start_server(secret)
            '''
            await websocket.recv()
            await websocket.recv()
            server_ip = await websocket.recv()
            server_ip = json.loads(server_ip)
            server_ip = server_ip['line']
            '''
        return is_server_on
    

def log_in(secret):
    param = {'userToken':USER_TOKEN,
         'visitSecret':secret,
         'reconnected':False,
         'script':'https://factorio.zone/cache/main.9219ba40f72c3ac84bda.js'
         }
    r = requests.post(url = URL, data = param)
    data = r.json()
    #print (data)

def start_server(secret):
    param = {'visitSecret':secret,
         'region':'us-east-1',
         'version':'1.1.50',
         'save':'slot1'
         }
    r = requests.post(url = sURL, data = param)
    data = r.json()
    #print ('started server ',data)
print('program started\nchecking status of server...\n\n')
is_server_on = asyncio.get_event_loop().run_until_complete(hello())
if not is_server_on:
    print('server is starting please wait')
    for i in range(15):
        print ('.'*(i+1))
        time.sleep(1)
    asyncio.get_event_loop().run_until_complete(hello())

while True:
    x = 1

