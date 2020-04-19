import telepot
import sys
import time
import imageRecognition
from telepot.loop import MessageLoop
import tweepy
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup
import wget
from googletrans import Translator

#twitter tokens
consumer_key = "1D17vJ0PrWa5zPoXYQYKIKfM0"
consumer_secret = "POWiXHp25YzZijpNx3yZMbRV3O9VTvmf35ERcjcTI8qeZ8FLZx"
access_token = "203093437-7rKxSLfSAHg5l1ppn9ldTh76vXXZeA3FPLpb3LoR"
access_token_secret = "oepqywaodcxWbr8Q7OlBRjRevV5nkzOLlFHqBwShintdP"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
TWEETS = []

#telegram token
TOKEN = "1120761066:EENTNsr3N9quBweXRgaPHxHkXnVgaN_nrZs"
bot = telepot.Bot(TOKEN)

def handler(msg):
    msgType, chtType, chatId = telepot.glance(msg)
    if msg["text"] == "/listen":   
        bot.sendMessage(chatId,"Awaiting tweets...")  
        for tweet in api.mentions_timeline():
            status = tweet.text
            TWEETS.append(status)
        while True:
            time.sleep(10)
            for tweet in api.mentions_timeline():
                name = str("@"+tweet.user.screen_name)
                tweetId = tweet.id_str
                txtTweet = tweet.text
                cadena = str(name) + " Has mentioned you in a tweet: "+ str(txtTweet)
                if not txtTweet in TWEETS:
                    TWEETS.append(txtTweet)
                    if hasattr(tweet,'extended_entities') and 'media' in tweet.extended_entities:
                        if "video_info" in tweet.extended_entities["media"][0]:
                            video = tweet.extended_entities["media"][0]["video_info"]["variants"][0]
                            video_url = video["url"]
                            bot.sendMessage(chatId,cadena[0:-23])
                            bot.sendVideo(chatId,video_url) 
                        else:
                            bot.sendMessage(chatId,cadena[0:-23])
                            num = len(tweet.extended_entities["media"])
                            for i in range(num):
                                media = tweet.extended_entities["media"][i]
                                media_url = media["media_url"]
                                bot.sendPhoto(chatId,media_url)
                                processImage(media_url, name, tweetId, chatId)   
                    elif hasattr(tweet,'entities') and 'media' in tweet.entities:
                        media = tweet.entities["media"][0]
                        media_url = media["media_url"]
                        bot.sendMessage(chatId,cadena[0:-23])
                        bot.sendPhoto(chatId,media_url)
                        processImage(media_url, name, tweetId, chatId) 
                    else:
                        bot.sendMessage(chatId,cadena)
                                           
    else:
        bot.sendMessage(chatId,"/listen")


def processImage(media_url, name, tweetId, chatId):
    filename = wget.download(media_url)
    prediction = imageRecognition.reconocerImagen(filename)
    message = "Image detection: " + prediction["element"] + " with a probability of " + str(int(prediction["probability"]*100)) + "%" 
    messageTrans = translateText(message, 'en')
    api.update_status(name+' '+messageTrans.text, tweetId)
    bot.sendMessage(chatId, messageTrans.text)
 
def translateText(text, lang):
    translator = Translator(service_urls=[
      'translate.google.com'
    ])

    translation = translator.translate(text, dest=lang, src='en')
    return translation

MessageLoop(bot,handler).run_as_thread()

while True:
    time.sleep(10)
                

    