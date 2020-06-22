import json
import requests
from time import sleep

############## CONFIG ###############

item_appid = '264710'							# The steam 'APP ID'
item_currency = '1'								# The currency to retrieve the price in
item_hash_name = 'Planet%204546B%20Postcard'	# The 'hashed name' of that specific market item , can be found from it's page's URL

#####################################

item_url = 'https://steamcommunity.com/market/priceoverview/?appid=' + item_appid + '&currency=' + item_currency + '&market_hash_name=' + item_hash_name

#####################################

def GetItemData () :

	result = requests.get (item_url)

	json_data = json.loads (result.text)

	return json_data

while True :

	data = GetItemData ()

	for i in data :

		print (i + " : " + "%s" % (data[i]))


	sleep (300) # Don't decrease this, you can increase if you want.

# Happy Ending
