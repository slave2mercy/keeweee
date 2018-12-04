import discord
from discord.ext import commands

class BanCog:

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self, ctx, member: discord.User):
        try:
            await member.ban()
        except Exception as e:
            await ctx.send("Could not ban the user: `{}`".format(str(e)))
        else:
            await ctx.send("Banned {}".format(member))

def setup(client):
    client.add_cog(BanCog(client))