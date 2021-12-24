#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Ns_AnoNymouS 

# the logging things
import os
import logging
"""logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from configs import SESSION, API_ID, API_HASH, API_TOKEN
from pyrogram import Client, __version__
import pyromod.listen

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from configs import Config

import pyrogram


logging.getLogger("pyrogram").setLevel(logging.WARNING)

 
class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=API_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

"""if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = bot(
        "pdf2img",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    #Config.AUTH_USERS.add(1337144652)
    
    async def start(self):
        
        #b_users, b_chats = await db.get_banned()
        #temp.BANNED_USERS = b_users
        #temp.BANNED_CHATS = b_chats
        
       
        await super().start()
        #await Media.ensure_indexes()
        me = await self.get_me()
        #temp.ME = me.id
        #temp.U_NAME = me.username
        #temp.B_NAME = me.first_name
        self.username = '@' + me.username
           
        
        #print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
       
        
       

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")"""


app = Bot()
app.run()    
    
    
    
   # app.run()
