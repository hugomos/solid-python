from useCases.createUser.index import (create_user_use_case, create_user_controller)
from entities.user import User
from useCases.createUser.create_user_dto import ICreateUserDTO

user = ICreateUserDTO(username='vitor_osantos', email='vitor_osantos@hotmail.com')

create_user_controller.handle(user)