import discord
from discord.ext import commands

TOKEN = 'NTE4NjE4OTQ3MTI2NTU4NzIw.DuTZ7A.y646cFyro388XT8LbEBBX0aUnFc'
client = commands.Bot(command_prefix = '!')

extensions = ['fun']

@client.event
async def on_ready():
	print('Bot Online')
	
@client.command()
async def load(extension):
	try:
		client.load_extension(extension)
		print('Loaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be loaded. [{}]'.format(extension, error))
		
@client.command()
async def unload(extension):
	try:
		client.unload_extension(extension)
		print('Unloaded {}'.format(extension))
	except Exception as error:
		print('{} cannot be unloaded. [{}]'.format(extension, error))
	
if __name__ == '__main__':
	for extension in extensions:
		try:
			client.load_extension(extension)
		except Exception as error:
			print('{} cannot be loaded. [{}]'.format(extension, error))
	
	client.run(TOKEN)
