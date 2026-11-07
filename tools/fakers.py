"""Генерация тестовых данных: прежний email по времени и обёртка над русской локалью Faker."""
import time

from faker import Faker

def get_random_email():
    """Собирает тестовый email с текущим временем; оставлен для ранних примеров без Faker."""
    return f"test.{time.time()}@exemple.com"

class Fake:
    """Адаптирует библиотечный Faker к данным пользователей, курсов и упражнений проекта."""
    def __init__(self, faker: Faker):
        """Сохраняет переданный генератор; локаль и правила генерации задаются при его создании."""
        self.faker = faker

    def text(self):
        """Генерирует произвольный текст для длинных описаний."""
        return str(self.faker.text())

    def uuid4(self):
        """Возвращает случайный UUID версии 4 в виде строки."""
        return str(self.faker.uuid4())

    def email(self):
        """Генерирует email-строку; уникальность относительно базы сервера не проверяется."""
        return str(self.faker.email())

    def sentence(self):
        """Возвращает короткое предложение для названий и кратких описаний."""
        return str(self.faker.sentence())

    def password(self):
        """Создаёт тестовую строку пароля средствами переданного Faker."""
        return str(self.faker.password())

    def last_name(self):
        """Генерирует фамилию согласно локали Faker."""
        return str(self.faker.last_name())

    def first_name(self):
        """Генерирует имя согласно локали Faker."""
        return str(self.faker.first_name())

    def middle_name(self):
        """Генерирует отчество; используемая в проекте локаль ru_RU поддерживает middle_name."""
        return str(self.faker.middle_name())

    def estimated_time(self):
        """Черновик срока в неделях: у Faker нет integer, поэтому вызов требует замены на self.integer."""
        return f"{self.faker.integer(1,10)} weeks"

    def integer (self, start: int = 1 , end: int = 100) -> int:
        """Возвращает целое число от start до end включительно."""
        return int(self.faker.random_int(start, end))

    def min_score(self):
        """Генерирует минимальный балл в диапазоне от 1 до 40."""
        return int(self.faker.random_int(1, 40))

    def max_score(self):
        """Генерирует максимальный балл в диапазоне от 50 до 100."""
        return int(self.faker.random_int(50, 100))



fake = Fake(faker=Faker("ru_RU"))