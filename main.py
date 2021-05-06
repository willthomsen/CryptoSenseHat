from sense_hat import SenseHat
import json
import cfscrape
from time import sleep
from random import randint


sense=SenseHat()
scraper = cfscrape.create_scraper()



#COMMENT THIS LINE OUT IF YOU DONT HAVE YOUR SENSE HAT UPSIDE DOWN LIKE I DO
sense.set_rotation(180)
#COMMENT THIS LINE OUT IF YOU DONT HAVE YOUR SENSE HAT UPSIDE DOWN LIKE I DO




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
              url1='https://api.cryptonator.com/api/ticker/btc-usd'
              cfurl1=scraper.get(url1).content
              data1=json.loads(cfurl1)
              btcprice=data1['ticker']['price']
              # Check which direction
              if event.direction == "up":
                sense.set_pixels(doge_sym)
                #Just a little break so you can see your created symbol
                sleep(3.0)
                sense.show_message(dogeprice, scroll_speed=0.10)    # Up arrow
              elif event.direction == "down":
                
                sense.set_pixels(bitcoin_sym)
                sleep(3.0)
                sense.show_message(btcprice, scroll_speed=0.10)

              elif event.direction == "left":
                sense.show_message(dogeprice, scroll_speed=0.10)

              elif event.direction == "right":
                sense.show_message(dogeprice, scroll_speed=0.10)
                
                
              #currently used to debug and correct symbols        
              elif event.direction == "middle":
                sense.set_pixels(bitcoin_sym)
                ##sense.show_message(dogeprice, scroll_speed=0.10)





