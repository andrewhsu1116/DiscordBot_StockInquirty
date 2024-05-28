import os
import asyncio
import discord
from discord.ext import commands

TOKEN="MTI0MjQxNDMwMTI5MDAzNzI1OA.GWECDK.BkOwCJ9HGqYaRgF5A7RJLOWaCxAzRASA_lJmvw"
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)


# 當機器人完成啟動時
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    
# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    try:
        await bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension} done.")
    except Exception as e:
        await ctx.send(f"Loaded {extension} fail.error：{e}")  

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    try:
        await bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"UnLoaded {extension} done.")
    except Exception as e:
        await ctx.send(f"UnLoaded {extension} fail.error：{e}")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    try:
        await bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"ReLoaded {extension} done.")
    except Exception as e:
        await ctx.send(f"Loaded {extension} fail.error：{e}")
#顯示所有已載入檔案，列出所有指令的名稱和說明
@bot.command()
async def command_list(ctx):
    all_commands = bot.all_commands
    print(all_commands)
    embed = discord.Embed()
    embed.title="指令表"
    embed.description="指令概要"
    for name, command in all_commands.items():
        embed.add_field(name=f"指令名稱: {name}",value=f"說明: {command.help}")
    await ctx.send(embed=embed)
    

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    cogs_dir = r"C:\Users\SuperUSER\Desktop\Discordbot_StockInquirty\Master\Discordbot_StockInquirty\cogs"
    current_directory = os.getcwd()
    # 輸出當前工作目錄的路徑
    print("當前所在資料夾的路徑：", current_directory)
    
    if not os.path.exists(cogs_dir):
        print(f"list {cogs_dir} does not exit.")
        return

    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py"):
            cog_name = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(cog_name)
                print(f"add cog：{cog_name} successful")
            except Exception as e:
                print(f"add cog {cog_name} fail.error：{e}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())