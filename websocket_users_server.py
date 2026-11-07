"""WebSocket-сервер: на каждое сообщение отправляет пять пронумерованных ответов."""
import asyncio

import websockets
from  websockets import ServerConnection


async def echo(websocket: ServerConnection):
    """На каждое сообщение клиента отправляет пять ответов с порядковыми номерами."""
    async for message in websocket:
        print(f"Получено сообщение от пользователя {message}")
        for number in range(1, 6):

            response = f"{number} Сообщение пользователя: {message}"
            await websocket.send(response)







async def main():
    """Запускает WebSocket-сервер учебного обмена сообщениями на порту 8765."""
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocet сервер запущен на ws://localhost:8765")
    await server.wait_closed()




asyncio.run(main())