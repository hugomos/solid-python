from entities.user import User
from repositories.user_repository import IUserRepository
from .create_user_dto import ICreateUserDTO

from providers.mail_provider import IMailProvider
from providers.mail_provider import IAdrees
from providers.mail_provider import IMessage


class CreateUserUseCase:

    def __init__(self, user_repository: IUserRepository, mail_provider: IMailProvider):
        self._user_repository = user_repository
        self._mail_provider = mail_provider

    def execute(self, data: ICreateUserDTO):
        user_already_exists = self._user_repository.find_by_email(data.email)

        if(user_already_exists):
            raise Exception("User already exists")

        user = User(data.username, data.email)
        self._user_repository.save(user)

        mail_to = IAdrees(user.username, user.email)
        mail_by = IAdrees("support", "vitor_osantos@athenasagricola.com.br")
        mail_message = IMessage(
            mail_to,
            mail_by,
            "Bem vindo a plataforma",
            "<p>Acesse o link para realizar o login <a href='https://google.com'>acessar</a></p>"
        )

        self._mail_provider.send_mail(mail_message)
