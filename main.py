import secret
print(secret.token)
import telegram
 
user_id = {}
bot = telegram.Bot(token=secret.token)
updates = bot.getUpdates()
for u in updates:
    user_id[u.message.chat.id] = 1
    
bot.sendMessage(chat_id=secret.test_id, text="Testing..")


