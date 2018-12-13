# ID     521947619363389442
# TOKEN  NTIxOTQ3NjE5MzYzMzg5NDQy.DvD2ZQ.KWu1-pq1BaZc7UhOHrRcd6g05aQ

# Permissions Integer 67648

# https://discordapp.com/oauth2/authorize?client_id=521947619363389442&scope=bot&permissions=67648 

import discord
import sys

client = discord.Client()  # starts the discord client.
token = open("token.txt","r").read()


@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')


# @client.event
# async def on_message(message):
# 	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
# 	if "hello" in message.content.lower():
# 		await message.channel.send('Hi!')



@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
	sentdex_guild = client.get_guild(521946919287914506)


	if "sentdebot.member_count" == message.content.lower():
		await message.channel.send(f"```py\n{sentdex_guild.member_count}```")
		# await message.channel.send(sentdex_guild.member_count)

	elif "sentdebot.community_report()" == message.content.lower():
		online = 0
		idle = 0
		offline = 0

		for m in sentdex_guild.members:
			if str(m.status) == "online":
				online += 1
			if str(m.status) == "offline":
				offline += 1
			else:
				idle += 1

		await message.channel.send(f"```Online: {online}.\nIdle/busy/dnd: {idle}.\nOffline: {offline}```")

	elif "sentdebot.logout()" == message.content.lower():
		await client.close()
		sys.exit()

client.run(token)