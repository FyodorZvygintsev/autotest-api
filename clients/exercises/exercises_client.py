"""Клиент упражнений: запросы к API и преобразование ответов в данные."""
from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, ExerciseResponseSchema, UpdateExerciseRequestSchema, GetExercisesResponseSchema




class ExercisesClient(APIClient):
    """Управляет упражнениями и получает списки упражнений выбранного курса."""
    def get_exercises_api(self, query : GetExercisesQuerySchema) -> Response:
        """Отправляет GET с courseId из модели query и возвращает исходный Response."""
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """Запрашивает одно упражнение по ID без преобразования ответа в модель."""
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """Сериализует данные упражнения и отправляет POST на /exercises."""
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request : UpdateExerciseRequestSchema) -> Response:
        """Отправляет PATCH с изменениями упражнения по его ID."""
        return self.patch(
            f"/api/v1/exercises/{exercise_id}",
            json=request.model_dump(by_alias=True),
        )

    def delete_exercise_api(self, exercise_id : str) -> Response:
        """Удаляет упражнение по ID и возвращает HTTP-ответ."""
        return self.delete(f"/api/v1/exercises/{exercise_id}")


    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """Проверяет ответ списка по GetExercisesResponseSchema и возвращает модель."""
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> ExerciseResponseSchema:
        """Возвращает словарь из response.json(); текущая реализация не соответствует аннотации модели."""
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestSchema) -> ExerciseResponseSchema:
        """Создаёт упражнение и разбирает JSON-ответ в ExerciseResponseSchema."""
        response = self.create_exercise_api(request)
        return ExerciseResponseSchema.model_validate_json(response.text)


    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> ExerciseResponseSchema:
        """Обновляет упражнение и возвращает проверенную модель с актуальными данными."""
        response = self.update_exercise_api(exercise_id, request)
        return ExerciseResponseSchema.model_validate_json(response.text)



def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """Получает токен пользователя и создаёт клиент упражнений."""
    return ExercisesClient(client=get_private_http_client(user))