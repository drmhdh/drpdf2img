#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Ns_AnoNymouS 

# the logging things
import pyrogram
import os
import logging
import logging.config


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
from configs import SESSION, API_ID, API_HASH, API_TOKEN

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from configs import Config

from typing import Union
from pyromod import listen
from pyrogram import Client as RawClient
from pyrogram.storage import Storage
from configs import Config
#from bot.core.new import New

LOGGER = Config.LOGGER
log = LOGGER.getLogger(__name__)



    
#class Bot(Client):

class Client(RawClient, New):
    """ Custom Bot Class """
    
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

    async def start(self):
        await super().start()
        log.info("Bot Started!")

    async def stop(self, *args):
        await super().stop()
        log.info("Bot Stopped!")
   
        
        
app = Bot()
app.run()    
