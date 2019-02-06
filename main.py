#@client.event
#async def on_message(message):
#    if message.author != client.user:
#        await client.send_message(message.channel, message.content[::-1])

#ydl3.py

from __future__ import unicode_literals
#from urllib2 import Request, urlopen, URLError
#from django.core.validators import URLValidator
#from django.core.exceptions import ValidationError
import youtube_dl
import discord
import os

client = discord.Client()

ydl_opts = {}

#val = URLValidator()
try:
    url = input('enter url: ')
    req = Request(url) 
except:
    print ('not valid url')
@client.event
async def on_message(message):
  if message.author != client.user:
    with youtube_dl.YoutubeDL({}) as ydl:meta=ydl.extract_info(url, download=False) 

  print ('upload date : %s' %(meta['upload_date']))
  print ('uploader    : %s' %(meta['uploader']))
  print ('views       : %d' %(meta['view_count']))
  print ('likes       : %d' %(meta['like_count']))
  print ('dislikes    : %d' %(meta['dislike_count']))
  print ('id          : %s' %(meta['id']))
  print ('format      : %s' %(meta['format']))
  print ('duration    : %s' %(meta['duration']))
  print ('title       : %s' %(meta['title']))
  print ('description : %s' %(meta['description']))

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
