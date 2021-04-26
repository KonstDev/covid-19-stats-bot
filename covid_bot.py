import pyrogram
from pyrogram import Client, filters
#from pyrogram.errors import FloodWait
#from pyrogram.types import ChatPermissions
import datetime
import os

from time import sleep
import random
from covid.api import CovId19Data

api = CovId19Data(force=False)

app = Client("my_account")

chat_id = 'covid19_belarus_dailystats'

hou_r = 0;



print('YES')
@app.on_message(filters.command("start", prefixes=".") & filters.me)
def parse(_, msg):
	app.send_message(chat_id, 'Bot started!' + str(datetime.datetime.now()))
	while(True):
		timebnow = datetime.datetime.now()
		if timebnow.minute == 0 and timebnow.second == 0:# and timebnow.hour == hou_r: #True: 
		    	location = res = api.filter_by_country('belarus')
		    	recovered = location['recovered']
		    	deaths = location['deaths']
		    	confirmed = location['confirmed']
		    	message = 'Данные на сегодня: ' + str(confirmed) + ' подтвержденных случаев, ' + str(deaths) + ' смерть(ей), ' + str(confirmed) + ' случаев выздоровления.';
		    	app.send_message(chat_id, message)
		    	sleep(10)
	    #msg.edit("YES, CAPTAIN! SPAMMING " + str(n) + " TIMES")

app.run()