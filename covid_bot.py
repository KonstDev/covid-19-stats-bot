import pyrogram
from pyrogram import Client, filters
#from pyrogram.errors import FloodWait
#from pyrogram.types import ChatPermissions
import datetime
import os

from time import sleep
import random
from covid.api import CovId19Data



app = Client("my_account")

chat_id = 'covid19_belarus_dailystats'

hou_r = 0;



#print('YES')

got_it = False

#global previos


@app.on_message(filters.command("start", prefixes=".") & filters.me)
def parse(_, msg):
	previos = 352950 #351674
	app.send_message(chat_id, 'Bot started! :' + str(datetime.datetime.now()))
	while(True):
		api = CovId19Data(force=False)
		timebnow = datetime.datetime.now()
		if timebnow.minute == 40: # and timebnow.second == 0:# and timebnow.hour == hou_r: #True: 
		    	location = res = api.filter_by_country('belarus')
		    	recovered = location['recovered']
		    	deaths = location['deaths']
		    	confirmed = location['confirmed']
		    	#previos = previos1
		    	message = 'Данные на сегодня: ' + str(confirmed) + ' подтвержденных случаев, ' + str(deaths) + ' смерть(ей), ' + str(recovered) + ' случаев выздоровления.';
		    	#if previos != 0 and not (previos == confirmed):
		    	message += '\n' + 'За сутки выявлено ' + str(confirmed - previos) + ' новых случаев.'
		    	hour = datetime.datetime.now().hour
		    	if (hour == 23):
		    		previos = confirmed
		    	app.send_message(chat_id, message)
		    	sleep(50)
		else:
			sleep(50)
	    #msg.edit("YES, CAPTAIN! SPAMMING " + str(n) + " TIMES")

app.run()