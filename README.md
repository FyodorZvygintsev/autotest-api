# Учебные примеры API на Python

Материалы курса по API-автоматизации: сетевые протоколы, HTTPX, собственные
API-клиенты, Pydantic, JSON Schema и генерация тестовых данных через Faker.
Короткие docstring в модулях, классах и функциях объясняют их назначение.

## Темы и файлы

| Тема | Где смотреть | Что изучается |
| --- | --- | --- |
| TCP/IP | `tcp_users_server.py`, `tcp_users_client.py` | Сокеты, отправка текста и история сообщений |
| WebSocket | `websocket_server.py`, `websocket_client.py`, `websocket_users_*.py` | Асинхронный обмен одним или несколькими ответами |
| gRPC | `course_service.proto`, `grpc_course_server.py`, `grpc_course_client.py` | Контракт RPC, сервис и клиентский stub |
| HTTPX | `httpx_*.py` | Прямые HTTP-запросы, токен, заголовки и загрузка файла |
| API-клиенты | `clients/` | Общая HTTP-обёртка и операции с пользователями, файлами, курсами и упражнениями |
| Pydantic | `Pydantic_basics.py`, `pydantic_create_user.py`, `clients/**/*schema.py` | Модели, вложенные объекты, aliases и сериализация |
| JSON Schema | `json_schema_exemple.py`, `pydantic_json_schema_*.py`, `tools/assertions/schema.py` | Проверка фактического JSON по ожидаемому контракту |
| Faker | `tools/fakers.py`, `httpx_create_user.py` | Генерация значений через объект `fake`; `faker_exemple.py` пока заготовка |
| Связанные сценарии | `api_client_create_course.py`, `api_client_create_exercise.py` | Передача ID созданных объектов между запросами |

`course_service_pb2.py` и `course_service_pb2_grpc.py` сгенерированы из `.proto`:
их вручную не документируют и не редактируют.

## Как читать сценарий

Начать удобно с `api_client_get_user.py`. От вызова функции переходите к её
определению, затем смотрите `return` и класс возвращаемого объекта.

```text
Сценарий → предметный клиент → APIClient → httpx.Client → сервер
                                                        ↓
Данные ← Pydantic-модель или Response.json() ← HTTP-ответ
```

В текущих клиентах методы с окончанием `_api` возвращают `httpx.Response`.
Методы `create_user`, `get_user`, `login` дополнительно разбирают ответ
в Pydantic-модель. Оба уровня используют один HTTP-запрос на операцию.

| Операция | Результат |
| --- | --- |
| `response.json()` у HTTPX | Python-данные из тела ответа, обычно словарь |
| `request.model_dump(by_alias=True)` | Словарь для отправки с именами полей API |
| `Schema.model_validate_json(response.text)` | Проверенная Pydantic-модель из JSON-строки |
| `Schema.model_json_schema()` | Словарь правил JSON Schema |
| `validate_json_schema(instance=data, schema=rules)` | `None` при успехе или `ValidationError` при нарушении правил |

## Запуск

Для HTTP-сценариев нужен отдельно запущенный учебный сервер на
`http://127.0.0.1:8000`; Swagger UI находится по адресу `/docs`.
Эти сценарии создают и изменяют данные сервера.

Используйте Python 3.12 или новее. В терминале из корня этого репозитория:

```powershell
.\venv312\Scripts\python.exe httpx_create_user.py
```

HTTP-часть использует `httpx`, Pydantic 2 с `email-validator`, `jsonschema`
и `Faker`. Для WebSocket нужен `websockets`, для gRPC — `grpcio` и `protobuf`.
Версии gRPC/protobuf должны соответствовать требованиям в заголовках
сгенерированных файлов. Созданное окружение `venv312` в Git не включается.

Для TCP, WebSocket и gRPC сначала запускается сервер, затем соответствующий
клиент во втором терминале. Порты: TCP — 12345, WebSocket — 8765, gRPC — 50051.
Два WebSocket-сервера используют один порт: выбирайте одну пару примеров.

## Незавершённые учебные места

В репозитории сохранены текущие черновики; наличие docstring не означает,
что все сценарии уже готовы к запуску.

- Переход на Faker в `api_client_*.py` и `pydantic_json_schema_*.py` ещё не
  завершён: местами импортирован `fake`, но остался вызов `get_random_email()`,
  а в `api_client_get_user.py` в email передаётся сам объект `fake`.
- `Fake.estimated_time` обращается к отсутствующему `Faker.integer`,
  `FilesClient.delite_file_api` — к отсутствующему `APIClient.delite`.
- `ExercisesClient.get_exercise` возвращает словарь при аннотации модели;
  аннотации запросов создания и обновления курса тоже требуют уточнения.
- В `Pydantic_basics.py` остались вызовы `model_damp*`; метод `get_username`
  расположен у модели файла, у которой нет полей имени.
- Сценарий упражнения ссылается на `testdata/files/Nonni-2.jpg`, а в проект
  добавлен `testdata/files/Nonni.jpg`. Путь нужно согласовать перед запуском.

Эти пункты перечислены отдельно, чтобы отличать готовые инструменты
от мест для самостоятельной доработки.
