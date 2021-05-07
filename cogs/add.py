import discord
from discord.ext import commands
from users import db

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def add(self,ctx, money: int, user: discord.Member):
      users = db(user.id)
      idlst = [547941645304201247, 576631663904161812]
      if money > 1000000000:
        await ctx.reply("You can't give away that much money at a time!")
        return
      if ctx.author.id in idlst:
        users.add_money(money)
        await ctx.reply(f"Added {money} to {user}s balance!")
      elif ctx.author.id not in idlst:
        print(ctx.author.id)
        await ctx.reply("Only papa Lark can use this command.")

      