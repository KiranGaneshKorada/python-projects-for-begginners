# this program automatically sends text msgs to mobile number every day at specified time

# text built site helps us we need to post data to it and i will send msgs

import requests
import schedule
import time

def send_msg():

    resp = requests.post('https://textbelt.com/text',  # posts data to the website
    {
    'phone': '9573385356',
     'message': 'Hello good morning kiran ganesh  reply stop to stop receiving these msgs',
    'key': 'textbelt', # this key is like lisence key(only one free msg per/day)
    }
    )
    print(resp.json())

    # this resp returns wheather the msg has been sent or not and the remaining quota of how many msgs can be still sent in that day and finally the msg id

schedule.every().day.at("02:30").do(send_msg)

while True:
    schedule.run_pending()
    time.sleep(10)