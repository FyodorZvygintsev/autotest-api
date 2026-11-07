"""Сценарий создания курса: пользователь, авторизация, обложка и данные курса."""
from clients.users.public_users_client import (
    get_public_users_client,
)
from clients.courses.courses_client import get_courses_client
from clients.files.files_client import get_file_client
from clients.private_http_builder import AuthenticationUserSchema
from tools.fakers import fake
from clients.users.user_schema import CreateUserRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
from clients.courses.course_schema import CreateCourseRequestSchema

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
    upload_file= './testdata/files/Nonni.jpg',
)


create_file_response = files_client.create_file(create_file_request)
print('Create file data', create_file_response)


create_course_request = CreateCourseRequestSchema(
    title = 'Python',
    description = 'python API course',
    previewFileId = create_file_response.file.id,
    maxScore= 100,
    minScore= 10,
    estimatedTime ='2 weeks',
    createdByUserId = create_user_response.user.id
)

create_file_response = courses_client.create_courses(create_course_request)

print('Create course data', create_file_response)