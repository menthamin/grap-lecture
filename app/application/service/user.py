from app.application.interfaces.user_repository import AbstractRepository
from app.domain.entity import User


class UserService:
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    def create_user(self, user_name: str):
        # Save to DB
        _user = User(name=user_name)
        # 데이터베이스에서 해당 이름이 있는지 확인하고, 있다면 Exception을 발생
        # Check user name in database, when user name in database
        if self.repository.find_one(model=_user):
            raise ValueError("User name is duplicated")
        user = self.repository.create(_user)
        return user
