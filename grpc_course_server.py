"""Учебный gRPC-сервис курсов на порту 50051 с фиксированным ответом."""
from concurrent import futures  # Импорт пула потоков для асинхронного выполнения

import grpc  # Импорт библиотеки gRPC

import course_service_pb2 # Сгенерированные классы для работы с gRPC-сообщениями
import course_service_pb2_grpc  # Сгенерированный класс для работы с сервисом


class CourseService(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация CourseServiceServicer с одним учебным RPC получения курса."""
    def GetCourse(self, request, context):
        """Возвращает фиксированные название и описание курса с ID из запроса."""
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов",
        )

# Функция для запуска gRPC-сервера
def serve():
    """Регистрирует сервис, запускает gRPC-сервер на порту 50051 и ждёт завершения."""

    # Создаем сервер с использованием пула потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Регистрируем реализацию CourseService на сервере.
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
    CourseService(),
    server,
)

    # Настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination()


# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()
