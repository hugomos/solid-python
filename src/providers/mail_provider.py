class IAdrees:
  def __init__(self, username, email):
    self.username = username
    self.email = email

class IMessage:
  def __init__(self, to:IAdrees, by:IAdrees, subject:str, body:str):
    self.to = to
    self.by = by
    self.subject = subject
    self.body = body
    

class IMailProvider:
  def send_mail(self, message: IMessage ) -> None:
    pass