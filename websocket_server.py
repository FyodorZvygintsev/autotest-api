"""WebSocket-сервер: отвечает на каждое принятое сообщение с текстовым префиксом."""
import asyncio

import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    """Читает сообщения соединения и отправляет ответ для каждого полученного сообщения."""
    async for message in websocket:
        print(f"Получено сообщение: {message}")
        response = f"Сервер получил: {message}"
        await websocket.send(response)  # Отправляем ответ


# Запуск WebSocket-сервера на порту 8765
async def main():
    """Запускает обработчик echo на localhost:8765 и ожидает закрытия сервера."""
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())