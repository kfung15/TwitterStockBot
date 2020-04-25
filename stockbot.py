import requests
import json
import random
import time

def validateStock(stockTicker):
    profile_base_url = "https://financialmodelingprep.com/api/v3/company/profile/"
    profile_complete_url = profile_base_url + stockTicker
    profile_response = requests.get(profile_complete_url)
    if len(profile_response.json()) > 0:
	    symbol = profile_response.json().get("symbol")
	    name = profile_response.json().get("profile").get("companyName")
	    price = profile_response.json().get("profile").get("price")

	    dcf_base_url = "https://financialmodelingprep.com/api/v3/company/discounted-cash-flow/"
	    dcf_complete_url = dcf_base_url + stockTicker
	    dcf_response = requests.get(dcf_complete_url)

	    if len(dcf_response.json()) == 4:
	    	dcf_analysis = dcf_response.json().get("Stock Price")	    
	    	return [name, symbol, price, dcf_analysis]

def generateTweet(profileData):
    firstline = profileData[0] + " ($" + profileData[1] + ") " + "is currently trading at $" + str(profileData[2])
    secondline = "Based on a DCF analysis, the fair price of " + profileData[1] + " is probably $" + str(profileData[3])
    difference = round((((float(profileData[2])/float(profileData[3])) * 100.0) - 100.0),2)
    if difference < 0.0:
    	thirdline = profileData[1] + " might be undervalued by " + str(difference) + "%"
    elif difference > 0.0:
    	thirdline = profileData[1] + " might be overvalued by " + str(difference) + "%"
    else:
    	thirdline = profileData[1] + " might be trading at fair value"
    fourthline = "Disclaimer: Use this info at your own risk"
    fifthline = "Long or short, the choice is yours!"
    final_tweet = firstline + "\n" + secondline + "\n" + thirdline + "\n" + fourthline + "\n" + fifthline
    if len(final_tweet) <= 280:
    	return final_tweet


