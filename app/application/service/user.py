from app.domain.entity import User


def create_user(usr_name: str):
    user = User(name=user_name)
    return user
