import telepot
import time
import requests

bot = telepot.Bot('5427244127:AAGj7pGJSX5jg26yje-FdkWGGrfOqHH0LT8') # Access Token. Gen>


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':

        print("text content")
        no = msg["text"]

        if no.isdigit():
            # id to number
            print("Searching for " + no)
            bot.sendMessage(chat_id, "Searching for " + no)
            contenturl = "https://redthryssa.xyz/prp.php?id="+no
            r = requests.get(contenturl)
            print(r.text)

            bot.sendMessage(chat_id, r.text)
            bot.sendMessage(chat_id, "powerd by @misfitsDEV. Join for more tools.")
        else:
           # number to id
            print("Searching for " + no)
            bot.sendMessage(chat_id, "Searching for " + no)
            contenturl = "https://redthryssa.xyz/prp.php?id="+no
            r = requests.get(contenturl)
            print(r.text)

            bot.sendMessage(chat_id, r.text)
            bot.sendMessage(chat_id, "powerd by @misfitsDEV. Join for more tools.")

    else:
        print("not text")
        bot.sendMessage(chat_id, "Please give me a circle user nickname or a number..")


bot.message_loop(handle)

print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
