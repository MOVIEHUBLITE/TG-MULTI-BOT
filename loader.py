import os
import logging 
import logging.config
from pyrogram import Client
                            
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)             

BOT_TOKEN = os.environ.get("5524164088:AAGns9OppBBEPXvrvBaX_F5SE_GPLm4_FYY", "")

API_ID = int(os.environ.get("8406611", ""))

API_HASH = os.environ.get("5820bc246505e0ff60af5391d649f9a6", "")

FORCE_SUB = os.environ.get("-1001675753014",)           

class App(Client):

    def __init__(self):
        super().__init__(
            "tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"},
        )

    async def start(self):
       await super().start()
       me = await self.get_me() 
       self.mention = me.mention
       self.username = me.username 
       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)
            self.invitelink = link
         except Exception as e:
            logging.warning(e) 
            logging.warning("Make Sure Bot admin in force sub channel") 
            self.force_channel = None
       logging.info(f"{me.first_name} Started")
        
    async def stop(self, *args):
      await super().stop()
      logging.info("Bot Stopped")
        
bot = App()
bot.run()

    










