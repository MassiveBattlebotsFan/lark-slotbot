import discord
from discord.ext import commands
from random import randrange
from users import db
users = db()
class Bet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bet(self,ctx, money: int = None):
      try:
        if money <= 0:
          await ctx.send("I need money to gamble!")
          return
        #main.auth(str(ctx.author.id))
        current_balance = users.get_money(ctx.author.id)
        if money > current_balance:
          await ctx.send("You don't have enough money!")
          return
        if current_balance >= 10000000:
          await ctx.send("You're too rich to play this game!")
          return
        if money <= 0:
          await ctx.send("Are you trying to scam me?")
          return
        if money >= 500001:
          await ctx.send("You can't bet that high!")
          return
        if money < 100:
          await ctx.send("You can't bet that low!")
          return
        #if money is max and current_balance < 100000:
        #await ctx.send("You don't have that much, dude!")
        # return
        if money == 'max':
          await ctx.send("You are about to spend max!")
          return
          
        r = randrange(10)
        r2 = randrange(randrange(2), 10)
        if (r > r2):
            #users[ctx.author.id]["wins"]
            await ctx.reply(
                f"You Win with {r} to {r2}.")
            users.add_money(ctx.author.id, round(money + (0.10 * money)))
        elif (r < r2):
            #user["losses"] += 1
            await ctx.reply(
                f"You Lose with {r} to {r2}.")
            users.remove_money(ctx.author.id, money)
        elif (r == r2):
            #user.update('ties')
            await ctx.reply(f"Tie, {r} to {r2}.")
      except BaseException as error:
        print(f"error: {error}")
      
