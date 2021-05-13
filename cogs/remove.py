import discord
from discord.ext import commands
from users import db

class Remove(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
      
  @commands.command()
  async def remove(self, ctx, money: int, user_ping: discord.Member = None):
    approved = ['547941645304201247', '743549337434587327']
    if str(ctx.author.id) not in approved:
      await ctx.send("only approved users can use add")
      return
    try:
      if user_ping == None:
        user_id = ctx.author
      elif type(user_ping) == discord.Member:
        user_id = user_ping
      users = db(user_id.id)
      moneya = users.get_money()
      if money > moneya:
        await ctx.reply(f'You cant take away more than the user has! \nThey have {moneya}, and you tried to take away {money}')
      else:
       users.remove_money(money)
       await ctx.send(f'${money} removed from {user_id}. They now have ${moneya - money}')
    except BaseException as error:
      print(f'Error: {error}')