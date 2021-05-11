import discord
from discord.ext import commands
from users import db

class Add(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
      
  @commands.command()
  async def add(self, ctx, money: int, user_ping: discord.Member = None):
    approved = ['547941645304201247', '743549337434587327', '585910898418253829']
    if str(ctx.author.id) not in approved:
      await ctx.send("only approved users can use add")
      return
    if money <= 0:
      await ctx.send('you gotta add an actual amount.')
      return
    try:
      if user_ping == None:
        user_id = ctx.author
      elif type(user_ping) == discord.Member:
        user_id = user_ping
      users = db(user_id.id)
      users.add_money(money)
      await ctx.send(f'${money} transferred to {user_id}')
    except BaseException as error:
      print(f'Error: {error}')