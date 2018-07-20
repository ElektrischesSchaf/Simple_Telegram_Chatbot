import sys
from io import BytesIO
import telegram
from flask import Flask, request, send_file
API_TOKEN = '***'
WEBHOOK_URL = 'https://***.herokuapp.com/'
app = Flask(__name__)
bot = telegram.Bot(token='***')

@app.route('/',methods=['GET'] )
def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))
    return "Hello World<p> This is ElektrishcesSchaf first Heroku-deployed python program !!!",200

@app.route('/', methods=['POST'])
def webhook_handler():   
    if request.method == "POST": 

        update = telegram.Update.de_json(request.get_json(force=True),bot)
        chat_id = update.message.chat.id
        text = update.message.text.encode('utf-8')        
        if text.startswith("Hi"):
            bot.sendMessage(chat_id=chat_id, text="Hello")
            print(text)
        if text.startswith("Nordling Lab"):
            print(text)
            bot.send_photo(chat_id=chat_id, photo='http://i.imgur.com/pZLI5rN.png')
        if text.startswith ("echo"):
            text=text[5:]
            if text.startswith("1"):
                text=text[1:]
                bot.sendMessage(chat_id=chat_id, text=text)
            if text.startswith("2"):
                text=text[1:]
                bot.sendMessage(chat_id=chat_id, text=text+text)
            if text.startswith("3"):
                text=text[1:]
                bot.sendMessage(chat_id=chat_id, text=text+text+text)
        if text.startswith ("math"):
            if "+" in text:
                index=text.index("+")
                text1=text[5:index]
                text2=text[index+1:]
                num1=float(text1)
                num2=float(text2)
                num3=num1+num2
                text=str(num3)
                bot.sendMessage(chat_id=chat_id, text="Answer="+text)
            if "-" in text:
                index=text.index("-")
                text1=text[5:index]
                text2=text[index+1:]
                num1=float(text1)
                num2=float(text2)
                num3=num1-num2
                text=str(num3)
                bot.sendMessage(chat_id=chat_id, text="Answer="+text)
            if "*" in text:
                index=text.index("*")
                text1=text[5:index]
                text2=text[index+1:]
                num1=float(text1)
                num2=float(text2)
                num3=num1*num2
                text=str(num3)
                bot.sendMessage(chat_id=chat_id, text="Answer="+text)
            if "/" in text:
                index=text.index("/")
                text1=text[5:index]
                text2=text[index+1:]
                num1=float(text1)
                num2=float(text2)
                num3=num1/num2
                text=str(num3)
                bot.sendMessage(chat_id=chat_id, text="Answer="+text)
         
        if text.startswith("media"):
            if "pokemon" in text:
               if "charmander" in text:

                    bot.send_video(chat_id=chat_id, video='https://media.giphy.com/media/yhfTY8JL1wIAE/giphy.gif')
               if "pikachu" in text:

                   bot.send_video(chat_id=chat_id, video='https://media.giphy.com/media/OazoCyXHeGyDm/giphy.gif')
        if text.startswith("search"):
            text=text[7:]
            if  text.startswith("google"):
                text=text[7:]
                bot.send_message(chat_id=chat_id, text="https://www.google.com.tw/search?q="+text)
            if text.startswith("yahoo"):
               text=text[6:]
               bot.send_message(chat_id=chat_id, text="https://tw.search.yahoo.com/search?fr=yfp-search-sb&p="+text)
            if text.startswith("bing"):
                text=text[5:]
                bot.send_message(chat_id=chat_id, text="http://www.bing.com/search?q="+text)
            if text.startswith("youtube"):
                text=text[8:]
                bot.send_message(chat_id=chat_id, text="https://www.youtube.com/results?search_query="+text)
                                                    
    return 'ok'
 
if __name__ == "__main__":
    _set_webhook()
    app.run()
