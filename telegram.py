import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print (chat_id)
    print ('Got command: %s' % command)

    if command == 'on':
       bot.sendMessage(chat_id, str('hello'))
    elif command =='off':
       bot.sendMessage(chat_id, str('hi'))

bot = telepot.Bot('')   #Enter telegram API key here
bot.message_loop(handle)
print ('I am listening...')

while 1:
     time.sleep(10)
