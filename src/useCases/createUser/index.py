from providers.implementations.smtp_mail_provider import SMTPMailProvider
from repositories.implementations.json_server_user_repository import JSONServerUserRepository
from useCases.createUser.create_user_use_case import CreateUserUseCase
from useCases.createUser.create_user_controller import CreateUserController

smpt_mail_provider = SMTPMailProvider()
json_server_user_repository = JSONServerUserRepository()

create_user_use_case = CreateUserUseCase(
  json_server_user_repository,
  smpt_mail_provider
)

create_user_controller = CreateUserController(create_user_use_case)

