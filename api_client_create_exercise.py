"""Связанный сценарий: создание пользователя, файла, курса и упражнения по ID курса."""
from clients.users.public_users_client import get_public_users_client
from clients.courses.courses_client import get_courses_client
from clients.courses.course_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_file_client
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.user_schema import CreateUserRequestSchema
from tools.fakers import fake
from clients.files.files_schema import CreateFileRequestSchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email= get_random_email(),
    password= "string",
    last_name= "string",
    first_name= "string",
    middle_name= "string"
)

create_user_response = public_users_client.create_user(
    create_user_request
)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

files_client = get_file_client(authentication_user)
courses_client = get_courses_client(authentication_user)



create_file_request = CreateFileRequestSchema(
    filename = 'Nonni.jpg',
    directory ='courses',
    upload_file= './testdata/files/Nonni-2.jpg',
)


create_file_data = files_client.create_file(create_file_request)
print('Create file data', create_file_data)


create_course_request = CreateCourseRequestSchema(
title = "2123",
description = '2311',
maxScore = 100,
minScore = 10,
estimatedTime = '2',
previewFileId = create_file_data.file.id,
createdByUserId = create_user_response.user.id
)


create_course_data = courses_client.create_courses(create_course_request)


exercise_client = get_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestSchema(
    title="Exercise 1",
    courseId=create_course_data.course.id ,
    maxScore = 5,
    minScore = 1,
    orderIndex = 0,
    description = "Exercise 1",
    estimatedTime = "5 minutes"
)


create_exercise_data = exercise_client.create_exercise(create_exercise_request)