import asyncio
import websockets
import json
import traceback
from hugchat import ChatBot
from login import Login
from Text import generatorText
#from urllib.parse import unquote
VERSION = "APPVERSION:1.0.9"
async def handle_client(websocket, path):
    try:
        clientMessage = ""
        #await websocket.send(VERSION)
        async for message in websocket:
            print(f"Received message from client: {message}")
            clientMessage = message
            data = json.loads(message)
            keywords = data['keywords']
            type = data["type"]
            prompt = generatorText(keywords=keywords,type=type)
            client = bot.message_stream(prompt)
            for text in client:
                if text is None:
                    continue
                print(text)
                await websocket.send(text)
            print("server send message done")
            await websocket.close()
    except websockets.exceptions.ConnectionClosedError:
        print("Connection closed by client.")
    except Exception as e:
        print(f"Error occurred: {e}")
        # 将异常信息包装成错误响应并发送回客户端
        traceback.print_exc()
        error = {"error": str(e), "traceback": traceback.format_exc(),"message":clientMessage}
        print(error)
async def main():
    while True:
        try:
            async with websockets.serve(handle_client, "0.0.0.0", 80):
                print("WebSocket server listening on port 80...")
                await asyncio.Future()  # prevent main() from exiting
        except Exception as e:
            print(f"Error occurred: {e}")
            print("Restarting server...")
            await asyncio.sleep(1)  # wait for a second before restarting
if __name__ == "__main__":
    sign = Login("malongfei1993@gmail.com", "Mlf1526847nb")
    cookies = sign.login()
            #Save cookies to usercookies/<email>.json
    sign.saveCookies()
    bot = ChatBot(cookies=cookies.get_dict())   
    asyncio.run(main())