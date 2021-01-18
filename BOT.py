from chatexchange.client import Client
import os

email = os.environ['EMAIL']
password = os.environ['PASSWORD']
se_chat = Client(os.environ['CLIENT'])
se_chat.login(email, password)
room = se_chat.get_room(os.environ['ROOM'])

def on_event(event, _):
    if event.data['event_type'] == 1:
        msg = event.message.content_source
        # Make a bot similar to Smokey

room.join()
room.watch_socket(on_event)
while True:
    pass
