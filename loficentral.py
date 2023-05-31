
import telegram.ext

Token = 'API Key'

updater = telegram.ext.Updater(Token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("""Hello! Welcome to Lofi Central! The place where you can enjoy all your favourite lofis, we'll be trying to provide you the best experience to listen to lofi. DISCLAMER: We don't own any art or music, Credits to the creators!!! It's just our way to collect some of the best lofis out there and provide you at one place. PLEASE SUPPORT US WITH WHOLE HEART ❤️❤️❤️
     (type /help to get started and understand other functions)""")
    
def help(update, context):
    update.message.reply_text("""
    /start - Starts the bot
    /help - Shows this help message
    /makers -> Information about the creators 
    /chilllofi -> lofi that will give you some chilling vibes
    /studylofi -> lofi you can listen while studying
    /vibelofi -> lofi beats to vibe to
    /fantasy -> playlist you fanatasize to
    /nights -> playlist to listen at night
    /raininglofi -> playlist for the rain lovers
    /drivinglofi -> playlist for the long drives
    /midnight -> midnight lofis are great for the moment
    
    """)

def makers(update, context):
    update.message.reply_text("""
    FOUNDER:
    - Name: DJXCROSS
    [ALL DETAILS REGARDING THIS MAN IS CONFIDENTIAL]
    
    DEVELOPER:
    - Name: Utkarsh0uchiha
    - Github: https://github.com/utkarsh0uchiha
    - Telegram: https://t.me/Utkarsh0uchiha 
    
    """)

def chilllofi(update, context):
    update.message.reply_text("playlist for chill lofi : https://youtube.com/playlist?list=PLAdT-TevBUHdqX2CTcTw2D_MpU3MRyKx_")

def vibelofi(update, context):
    update.message.reply_text("playlist for lofi to vibe of : https://youtube.com/playlist?list=PLAdT-TevBUHeSNC8TgimKWs8W2ikvlOFy")

def fantasy(update, context):
    update.message.reply_text("playlist you fanatsize to : https://youtube.com/playlist?list=PLAdT-TevBUHdCIYJWJ70ogIvvVzuVcjD2")

def nights(update, context):
    update.message.reply_text("lofi for the lovely night: https://youtu.be/2jMfeU3YpZE")

def raininglofi(update, context):
    update.message.reply_text("lofi for the rain lovers: https://youtu.be/YQs7IVvvVYw")

def drivinglofi(update, context):
    update.message.reply_text("lofi for the long drives: https://youtu.be/25BkVBgFD9Y")

def midnight(update, context):
    update.message.reply_text("midnight lofis are great for the moment: https://open.spotify.com/playlist/0aYyOFjmYmpVM0D6mjeZxy?si=359c4dc6f98e4815 ")

def studylofi(update, context):
    update.message.reply_text("lofi you can listen while studying: https://open.spotify.com/playlist/6l1TV7C21d3pNuM0EKPSkw?si=0581f08e99954c3d")

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('makers', makers))
dispatcher.add_handler(telegram.ext.CommandHandler('chilllofi', chilllofi))
dispatcher.add_handler(telegram.ext.CommandHandler('vibelofi', vibelofi))
dispatcher.add_handler(telegram.ext.CommandHandler('fantasy', fantasy))
dispatcher.add_handler(telegram.ext.CommandHandler('nights', nights))
dispatcher.add_handler(telegram.ext.CommandHandler('raininglofi', raininglofi))
dispatcher.add_handler(telegram.ext.CommandHandler('drivinglofi', drivinglofi))
dispatcher.add_handler(telegram.ext.CommandHandler('midnight', midnight))
dispatcher.add_handler(telegram.ext.CommandHandler('studylofi', studylofi))


updater.start_polling()
updater.idle()
