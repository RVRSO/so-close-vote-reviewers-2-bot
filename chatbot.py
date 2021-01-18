from chatexchange.client import Client
email = 'secret'
password = 'secret'
se_chat = Client('meta.stackexchange.com')
se_chat.login(email,password)
