from .create_user_dto import ICreateUserDTO
from .create_user_use_case import CreateUserUseCase


class CreateUserController:
  def __init__(self, create_user_use_case: CreateUserUseCase) -> None:
    self._create_user_use_case = create_user_use_case

  def handle(self, data: ICreateUserDTO) -> None:
    try:
      self._create_user_use_case.execute(data)
      print('User created successfully')
    except Exception as e:
      raise e