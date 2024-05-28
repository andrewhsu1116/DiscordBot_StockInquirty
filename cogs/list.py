import discord
from discord.ext import commands

class list():
    def __init__(self, bot: commands.bot):
        self.bot = bot

@commands.command
async def list(cxt:commands.context,extension):
    await cxt.send("hi")


async def setup(bot: commands.bot):
    await bot.add_cog(list(bot))