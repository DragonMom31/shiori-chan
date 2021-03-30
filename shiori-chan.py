#Shiori-chan Discord Bot
#Author: Erika Marie (@ladymeido)

import os
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

#retrieve bot token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#retrieve user token from .env file
ERIKA_ID = os.getenv('ERIKA_ID')

#declaring logger for errors
shioriLogger = logging.getLogger('discord')
#logger info level
shioriLogger.setLevel(logging.DEBUG)
#log file to write info
shioriHandler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#setting format for discord.log
shioriHandler.setFormatter(logging.Formatter(
	'%(asctime)s:%(levelname)s:%(name)s: %(message)s'
	)
)
shioriLogger.addHandler(shioriHandler)

#declaring bot object
shioriBot = commands.Bot(command_prefix='!')

#COMMANDS#

#aya command, responds "ayayayaya!"
@shioriBot.command(name='aya', help='ayayayayaya!')
async def aya(ctx):
	await ctx.send('Ayayayaya~!')

#hello command
@shioriBot.command(name='hello', help='tell shiori-chan to say hi!')
async def hello(ctx):
	await ctx.send('hiiiii~ what\'s bracking~?')

#EVENTS#

#prints login message to the command line 
@shioriBot.event
async def on_ready():
	print('{0.user} up and running!'.format(shioriBot))

@shioriBot.listen('on_message')
async def response(message):
	if message.author == shioriBot.user:
		return

	if message.author == shioriBot.get_user(ERIKA_ID):
		await message.channel.send(
			'erika pls stfu and go code or write or something! dumb bitch'
		) 

	if message.content.startswith('@everyone'):
		await message.channel.send(
			'pinging the whole server...? this better be important!!'
		)

	if message.content.startswith('!aya'):
		await message.channel.send(file=discord.File('img\/ayaya.gif'))

@shioriBot.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f'enjoy your stay {member.name}~!!!')

shioriBot.run(TOKEN)