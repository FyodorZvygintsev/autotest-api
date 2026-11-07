"""HTTP-операции с курсами и разбор ответа создания в Pydantic-модель."""

from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from clients.courses.course_schema import CourseSchema, CreateCourseRequestSchema, UpdateCourseRequestSchema, CreateCourseResponseSchema, GetCoursesQwerySchema



class CoursesClient(APIClient):
    """Предоставляет операции с /courses через авторизованный HTTP-клиент."""

    def get_courses_api(self, query : GetCoursesQwerySchema) -> Response:
        """Передаёт параметры поиска из модели в query string и возвращает список в Response."""
        return self.get("/api/v1/courses", params = query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """Получает HTTP-ответ с данными одного курса по его ID."""
        return self.get(f"/api/v1/courses/{course_id}/")

    def create_course_api(self, request: GetCoursesQwerySchema) -> Response:
        """Отправляет данные курса как JSON с aliases и возвращает ответ создания."""
        return self.post("/api/v1/courses", json = request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: GetCoursesQwerySchema) -> Response:
        """Отправляет PATCH с новыми данными курса по указанному ID."""
        return self.patch(f"/api/v1/courses/{course_id}", json = request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """Отправляет запрос удаления курса и возвращает статус и тело ответа."""
        return self.delete(f"/api/v1/courses/{course_id}/")


    def create_courses(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """Создаёт один курс и разбирает ответ в CreateCourseResponseSchema."""
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """Получает токен по учётным данным и создаёт клиент операций с курсами."""
    return CoursesClient(client=get_private_http_client(user))
