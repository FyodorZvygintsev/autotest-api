"""Контракт упражнений: запросы, отдельное упражнение и список упражнений курса."""
from pydantic import BaseModel

class GetExercisesQuerySchema(BaseModel):
    """Параметр courseId для запроса списка упражнений конкретного курса."""
    courseId: str


class CreateExerciseRequestSchema(BaseModel):
    """Данные создания упражнения: связь с курсом, порядок, баллы и описание."""
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str

class ExerciseSchema(BaseModel):
    """Структура одного упражнения, включая его ID и ID курса."""
    id : str
    title : str
    courseId : str
    maxScore : int
    minScore : int
    orderIndex : int
    description : str
    estimatedTime : str

class GetExercisesResponseSchema(BaseModel):
    """Ответ со списком exercises; каждый элемент проверяется по ExerciseSchema."""
    exercises: list[ExerciseSchema]


class UpdateExerciseRequestSchema(BaseModel):
    """Поля изменения упражнения: допускают None, но без defaults должны быть переданы."""
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExerciseResponseSchema(BaseModel):
    """Ответ с одним упражнением во вложенном поле exercise."""
    exercise: ExerciseSchema