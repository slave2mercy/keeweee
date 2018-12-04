import discord
from discord.ext import commands

class KickCog:

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member: discord.User):
        try:
            await member.kick()
        except Exception as e:
            await ctx.send("Could not kick the user: `{}`".format(str(e)))
        else:
            await ctx.send("Kicked {}".format(member))

def setup(client):
    client.add_cog(KickCog(client))