import discord
from discord.ext import commands

# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    # 前綴指令
    @commands.command()
    async def Hi(self, ctx: commands.Context):
        await ctx.send("Hi")

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "Hello":
            await message.channel.send("Hello, world!")

# Cog 載入 bot 中
async def setup(bot: commands.bot):
    await bot.add_cog(Main(bot))