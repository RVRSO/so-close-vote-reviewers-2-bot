from chatexchange.client import Client
email = 'email@email.com'
password = '**************'
se_chat = Client('stackoverflow.com')
se_chat.login(email, password)
room = se_chat.get_room('227446')
room.join()
room.send_message('@ppw Are you here?! lol ;D 😉')
room.leave()
