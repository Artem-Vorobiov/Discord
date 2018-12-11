# ID     521947619363389442
# TOKEN  NTIxOTQ3NjE5MzYzMzg5NDQy.DvD2ZQ.KWu1-pq1BaZc7UhOHrRcd6g05aQ

# Permissions Integer 67648

# https://discordapp.com/oauth2/authorize?client_id=521947619363389442&scope=bot&permissions=67648 

import discord

client = discord.Client()  # starts the discord client.
@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/

async def on_ready():  # method expected by client. This runs once when connected
	print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	if "hello" in message.content.lower():
		await message.channel.send('Hi!')

client.run("NTIxOTQ3NjE5MzYzMzg5NDQy.DvD2ZQ.KWu1-pq1BaZc7UhOHrRcd6g05aQ")

