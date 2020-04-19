# TwitterBot
A twitter bot that analyzes images sent to it and replies with a description and an accuracy probability

How To

1. Obtain tokens from both Twitter and Telegram

To get the required tokens from twitter you need to create a twitter app and follow this guide: https://developer.twitter.com/ja/docs/basics/authentication/guides/access-tokens

To get the required tokens from telegram you need to enter the app and find the bot "@botfather" which will guide you on the process of setting up your telegram bot and getting the access tokens.

2. Download libraries

You will need to install the latest telepot library for python. As well as tensorflow for the image analysis. Run the following commands:
pip install telepot
pip install tensorflow pillow silence_tensorflow --user
pip install wget
pip install tweepy

3. Run the application

Run the application and then open your telegram bot. 
Start listening for any new mentions by entering the command /listen. 

If any mentions contain images they will be downloaded from twitter and analyzed locally by the tensorflow library, the app will then reply to the user with a description of each image and a percentage of probablity that the description is correct. You will be able to see the reply on your telegram bot messages as well.
