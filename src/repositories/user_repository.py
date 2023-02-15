from entities.user import User

class IUserRepository:

  def find_by_email(self, email:str) -> User:
    pass

  def save(self, user: User) -> None:
    pass