import secret
print(secret.token)
import telegram
 
users = {}
bot = telegram.Bot(token=secret.token)
updates = bot.getUpdates()
for u in updates:
    users[u.message.chat.id] = u.message.from_user.last_name
    print(u.message)
print(users)
bot.sendMessage(chat_id=secret.test_id, text="Testing..")

