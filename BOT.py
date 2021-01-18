from chatexchange.client import Client
email = 'email@email.com'
password = '**************'
se_chat = Client('stackoverflow.com')
se_chat.login(email, password)
room = se_chat.get_room('227446')
def on_event(event, _):
  if event.data['event_type'] == 1:
    msg = event.message.content_source
    #Make a bot similar to Smokey
room.join()
room.watch_socket(on_event)
while True:
  pass
