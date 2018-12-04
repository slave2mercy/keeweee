import discord
from discord.ext import commands

class HelpCog:

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(color=discord.Color.red())
        embed.set_author(name="Help command")
        embed.add_field(name="Moderation Commands", value="s!kick <user> - Kick a user.\ns!ban <user> - Ban a user.")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(HelpCog(client))