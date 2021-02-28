from chatexchange.client import Client
import os, random

email = os.environ['EMAIL']
password = os.environ['PASSWORD']
se_chat = Client(os.environ['CLIENT'])
se_chat.login(email, password)
room = se_chat.get_room(os.environ['ROOM'])

ALIVE_MSG = [
    'Yup', 'You doubt me?', 'Of course', '... did I miss something?', 'plz send teh coffee',
    'Watching this endless list of new questions *never* gets boring', 'Kinda sorta',
    'You should totally drop that and use jQuery', r'¯\\_(ツ)\_/¯', '... good question',
]

def run(command):
    if command == 'alive':
        return random.choice(ALIVE_MSG)
    else:
        room.send_message("No such command '{0}'".format(command))

def on_event(event, _):
    if event.data['event_type']:
        msg = event.message.content_source
        if msg.lower().startswith('rpb ') or msg.lower.startswith('!!/'):
            # Make a bot like Smokey
            event.message.reply(run(msg[3:]))
            
room.join()
room.watch_socket(on_event)

while True:
    pass
