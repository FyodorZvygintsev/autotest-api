"""WebSocket-клиент: после отправки сообщения получает пять ответов сервера."""
import asyncio

import websockets


async def client():
    """Отправляет сообщение по WebSocket и последовательно читает пять ответов."""
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message)  # Отправляем сообщение

        for _ in range(5):
            message = await websocket.recv()
            print(message)


asyncio.run(client())