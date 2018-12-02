import discord
from discord.ext import commands

TOKEN = 'NTE4NjE4OTQ3MTI2NTU4NzIw.DuWeOQ.2XTY6YuKcpeZMwKFEbYiCzISbcE'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) +1):
        messages.append(message) 
    await client.delete_message(messages)
    await client.say('Messages deleted.')

client.run(TOKEN)