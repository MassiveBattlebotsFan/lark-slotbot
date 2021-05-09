import discord
from discord.ext import commands
import asyncio

class Close(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
      
  @commands.command()
  async def close(self,ctx):
   my_ID = 547941645304201247
   if (ctx.author.id == my_ID):
    first_embed = discord.Embed(title='Bot Closing...', description="This will take some time to take full effect.")
    new_embed = discord.Embed(title='Bot Closed.')
    msg = await ctx.send(embed=first_embed)
    await asyncio.sleep(5)
    await msg.edit(embed=new_embed)
    await self.bot.close()
    await asyncio.sleep(10)
   elif (ctx.author.id != my_ID):
    print(ctx.author.id)
    await ctx.reply("Only papa Lark can use this command.")
    