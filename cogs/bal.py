import discord
from discord.ext import commands
#import main
import random
from users import db

class Bal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bal(self, ctx, user: discord.Member = None):
      if user == None:
        user = ctx.author
      users = db(user.id)
      money = users.get_money()
      embedVar = discord.Embed(title=f"{user}'s Balance", description="", color=0x00ff00)
      embedVar.add_field(name="You have:", value=f"${money}", inline=False)
      await ctx.send(embed=embedVar)
      


