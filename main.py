from sense_hat import SenseHat
import json
import cfscrape
from time import sleep
from random import randint


sense=SenseHat()
scraper = cfscrape.create_scraper()
sense.set_rotation(180)

#gold
w=(255, 255, 0)

#led off
e=(0,0,0)

#white
o=(255,255,255)


###Tried my best to simulate the look of the coin
doge_sym=[
o,o,w,w,w,w,o,o,
o,w,e,e,e,e,w,o,
w,w,e,w,w,w,e,w,
w,e,e,e,w,w,e,w,
w,e,e,e,w,w,e,w,
w,w,e,w,w,w,e,w,
o,w,e,e,e,e,w,o,
o,o,w,w,w,w,o,o
]
#first pass was extremely rough.Looks okay, but probably could be better. 
bitcoin_sym=[
o,w,w,w,w,w,w,o,
w,w,w,e,w,e,w,w,
w,w,e,e,e,e,w,w,
w,w,e,w,w,w,e,w,
w,w,e,e,e,e,w,w,
w,w,e,w,w,w,e,w,
w,w,e,e,e,e,w,w,
o,w,w,e,w,e,w,o
]


#sym3
#sym4
#sym5 



while True:
  for event in sense.stick.get_events():
 
    
    
    if event.action == "pressed":
            #this updates every minute or so
              url='https://api.cryptonator.com/api/ticker/doge-usd'
              cfurl=scraper.get(url).content
              data=json.loads(cfurl)
              dogeprice=data['ticker']['price']
              # Check which direction
              if event.direction == "up":
                sense.set_pixels(doge_sym)
                #Just a little break so you can see your created symbol
                sleep(1.0)
                sense.show_message(dogeprice, scroll_speed=0.10)    # Up arrow
              elif event.direction == "down":
                sense.show_message(dogeprice, scroll_speed=0.10)

              elif event.direction == "left":
                sense.show_message(dogeprice, scroll_speed=0.10)

              elif event.direction == "right":
                sense.show_message(dogeprice, scroll_speed=0.10)
                
                
              #currently used to debug and correct symbols        
              elif event.direction == "middle":
                sense.set_pixels(bitcoin_sym)
                ##sense.show_message(dogeprice, scroll_speed=0.10)





