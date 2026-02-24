# users/models.py
class UserAlreadyExistsError(Exception):
    """Исключение, выбрасываемое при попытке добавить существующего пользователя"""
    pass


class UserNotFoundError(Exception):
    """Исключение, выбрасываемое если пользователь не найден"""
    pass


class User:
    """Класс пользователя"""
    
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age
    
    def __str__(self) -> str:
        return f"User(username={self.username}, email={self.email}, age={self.age})"


class UserManager:
    """Менеджер пользователей"""
    
    def __init__(self):
        self.users = {}  # словарь username -> User объект
    
    def add_user(self, user: User):
        """Добавляет пользователя. Если пользователь уже есть - UserAlreadyExistsError"""
        if user.username in self.users:
            raise UserAlreadyExistsError(f"Пользователь с именем '{user.username}' уже существует")
        self.users[user.username] = user
    
    def remove_user(self, username: str):
        """Удаляет пользователя. Если пользователя нет - UserNotFoundError"""
        if username not in self.users:
            raise UserNotFoundError(f"Пользователь с именем '{username}' не найден")
        del self.users[username]
    
    def find_user(self, username: str) -> User:
        """Находит пользователя. Если пользователя нет - UserNotFoundError"""
        if username not in self.users:
            raise UserNotFoundError(f"Пользователь с именем '{username}' не найден")
        return self.users[username]