import telepot
import time
import requests

bot = telepot.Bot('5356497581:AAEQiSF8eoFOHwm2o_6gWuDHMWuZKZw3di8') # Access Token. Generate with Botfather
APIToken = "" # PHPHive Truecaller API Token, Obtain it from https://tcapi.phphive.info/console/


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
    
        print("text content")
        no = msg["text"]
        
        if "hi" in no.lower():
            bot.sendMessage(chat_id, "Hello, How can i help?")
        
        else:
        
            if "hello" in no.lower():
                bot.sendMessage(chat_id, "Hmm, tell!")
        
            else:
                 if "offer" in no.lower():
                    # For Searching User Details
                    print("wait a sec, I'm sending you Today's offer.")
                    bot.sendMessage(chat_id, "wait a sec, I'm sending you Today's offer.")
                    contenturl = "https://api.redthryssa.xyz/index2.php"
                    r = requests.get(contenturl)
                    #print(r.text)
        
                    bot.sendMessage(chat_id, r.text)
                    bot.sendMessage(chat_id, "That's all i have for now..")
                    
                 else:
                    if "/start" in no.lower():
                        bot.sendMessage(chat_id, "I'm already running, dummy 😒")
                    else:
                         if "/help" in no.lower():
                            bot.sendMessage(chat_id, "To chek today's offer send /offer ")
            
    else:
        print("not text")
        bot.sendMessage(chat_id, "Please enter a valid number with country code.")


bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
