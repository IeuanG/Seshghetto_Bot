from fbchat import log, Client
from fbchat.models import *

group_id = '1405725802798021'
banned_users = []
with open('banned_users.txt', 'r') as filestream:
	for line in filestream:
		banned_users.append(line.split("#")[0].strip())
print("Loaded banned users. {} found.".format(len(banned_users)))

class KeepBot(Client):

    def onPeopleAdded(self, added_ids, author_id, thread_id, **kwargs):
        if group_id == thread_id and author_id != self.uid:
            for added_id in added_ids:
                if added_id in banned_users:
                    log.info("{} got added. They will be removed".format(added_ids))
                    self.removeUserFromGroup(added_id, thread_id=thread_id)


client = KeepBot("seshghetto@gmail.com", "<redacted>")
client.listen()
