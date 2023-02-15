from uuid import uuid4

class User:
  def __init__(self, username:str, email:str, id=None) -> None:
    self._id = id if id else str(uuid4())
    self._email = email
    self._username = username

  @property
  def username(self):
    return self._username

  @property
  def email(self):
    return self._email