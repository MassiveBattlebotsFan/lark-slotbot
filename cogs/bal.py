import discord
from discord.ext import commands
#import main
import random
from users import db
users = db()
class Bal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bal(self,ctx):
      user = await self.bot.fetch_user(ctx.author.id)
      money = users.get_money(user_id=ctx.author.id)
      if money == "err":
        await ctx.send("You are not registered in the DB")
        users.reg_user(ctx.author.id)
      else:
        embedVar = discord.Embed(title=f"{user}'s Balance", description="", color=0x00ff00)
        embedVar.add_field(name="You have:", value=f"${money}", inline=False)
        await ctx.send(embed=embedVar)
      


