from telegram.ext.updater import Updater 
from telegram.update import Update 
from telegram.ext.filters import Filters
from telegram import Bot, ChatPermissions
from telegram import ParseMode
import requests
import json
import time
import datetime
import pytz
from twikit import Client

BOT_TOKEN = "Your_BOT_TOKEN)
updater = Updater(BOT_TOKEN, use_context=True)
raid = 0

# Initialize client
client = Client('en-US')

with open('cookies.json', 'r', encoding='utf-8') as f:
    client.set_cookies(json.load(f))

# Function to fetch tweet by ID
def fetch_tweet(tweet_id):
    tweet = client.get_tweet_by_id(tweet_id)
    return tweet

# Define a function to check if the user is an admin
def is_admin(update):
    return chat_member.status == 'administrator' or chat_member.status == 'creator'

def is_group(update: Update) -> bool:
    return update.message.chat.type in ['group', 'supergroup']

def start(update: Update, context: CallbackContext): 
    if is_group(update):
        if is_admin(update):
            update.message.reply_text("""
🔰 Instructions on using SHIELD 🔰

1️⃣ Add @Aegis_AI_Bot to your Telegram group

2️⃣ MAKE THE BOT AN ADMIN.
       Must be Admin to function. Refer to screenshot above for permissions.

3️⃣ Only Admins can run the Shield Bot

4️⃣ To Start A Raid:

    ➡️ Enter /aegis,
             Chat Locks
    ➡️ Follow onscreen prompts

    ➡️ Enter /cancel to force stop current raid and unlock TG.
""")
    else:
        update.message.reply_text("""
🔰 Instructions on using SHIELD 🔰

1️⃣ Add @Aegis_AI_Bot to your Telegram group

2️⃣ MAKE THE BOT AN ADMIN.
       Must be Admin to function. Refer to screenshot above for permissions.

3️⃣ Only Admins can run the Shield Bot

4️⃣ To Start A Raid:

    ➡️ Enter /aegis,
          Chat Locks
    ➡️ Follow onscreen prompts

    ➡️ Enter /cancel to force stop current raid and unlock TG.
""") 

def help(update: Update, context: CallbackContext): 
    if is_admin(update):
        update.message.reply_text("Try /start instead") 

def shield(update: Update, context: CallbackContext):
    if is_group(update):
        if is_admin(update):
            global raid, CURRENT_STEP, chat_id
            raid = 1
            CURRENT_STEP = 0
            chat_id = update.message.chat_id
            permissions = ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
            )

            # Set the permissions for the chat
            bot.set_chat_permissions(chat_id, permissions)

            video_file_path = "start.mp4"
            update.message.reply_video(video=open(video_file_path, 'rb'),
                                       caption="""
        Group has been locked \N{Lock} and ready for the raid
        <b>Type in your twitter URL to continue</b>
                                       """, parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text("This command works only in group chats.")


                # Set the permissions for the chat
                bot.set_chat_permissions(chat_id, permissions)
                # Get the current date and time again
                end_time = datetime.datetime.now()
                
                # Calculate the time difference
                time_taken = end_time - start_time
                
                # Extract days, hours, minutes, and seconds
                days = time_taken.days
                hours, remainder = divmod(time_taken.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                
                # Format the time duration
                if days > 0:
                    time_taken_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
                elif hours > 0:
                    time_taken_str = f"{hours} hours, {minutes} minutes, {seconds} seconds"
                elif minutes > 0:
                    time_taken_str = f"{minutes} minutes, {seconds} seconds"
                else:
                    time_taken_str = f"{seconds} seconds"



updater.dispatcher.add_handler(CommandHandler('start', start)) 
updater.dispatcher.add_handler(CommandHandler('help', help)) 
updater.dispatcher.add_handler(CommandHandler('aegis', shield)) 
updater.dispatcher.add_handler(CommandHandler('cancel', cancel)) 

# Filters out unknown messages. 
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) 

updater.start_polling()
