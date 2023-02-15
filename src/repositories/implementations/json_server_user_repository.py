from repositories.user_repository import IUserRepository
from entities.user import User

import json
import requests

class JSONServerUserRepository(IUserRepository):
  def find_many(self) -> list[User]:
    request = requests.get('http://192.168.2.130:3000/users')

    if(request.status_code >= 200 and request.status_code < 300):
      response = request.json()
      return response

    raise Exception('Error: ' + request.text)

  def save(self, user: User) -> None:
    payload = {
      "username": user.username,
      "email": user.email
    }

    request = requests.post('http://192.168.2.130:3000/users', json=payload)

    if(request.status_code >= 300):
      raise Exception('Error: ' + request.text)