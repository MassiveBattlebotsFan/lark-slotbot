import discord
from discord.ext import commands
from random import randrange
from users import db

class Bet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(3, 15, commands.BucketType.user)
    async def bet(self,ctx, money: int = None):
      users = db(ctx.author.id)
      try:
        if money <= 0:
          await ctx.send("I need money to gamble!")
          return
        #main.auth(str(ctx.author.id))
        current_balance = users.get_money()
        if money > current_balance:
          await ctx.reply(f"You don't have enough money! \nYou are trying to bet ${money}, and you have ${users.get_money()} remaining. \nCome back to me when you're a little bit... hmm... ***richer***")
          return
        if current_balance >= 10000000:
          await ctx.reply("You're too rich to play this game!")
          return
        if money <= 0:
          await ctx.reply("Are you trying to scam me?")
          return
        if money >= 500001:
          await ctx.reply("You can't bet that high!")
          return
        if money < 100:
          await ctx.send("You can't bet that low!")
          return
          
        r = randrange(10)
        r2 = randrange(randrange(2), 10)
        if (r > r2):
            #users[ctx.author.id]["wins"]
            users.add_money(round(money + (0.10 * money)))
            await ctx.reply(
                f"You Win with {r} to {r2}. You have ${users.get_money()} remaining.")
        elif (r < r2):
            #user["losses"] += 1
            users.remove_money(money)
            await ctx.reply(
                f"You Lose with {r} to {r2}. You have ${users.get_money()} remaining.")
        elif (r == r2):
            #user.update('ties')
            await ctx.reply(f"Tie, {r} to {r2}. You have ${users.get_money()} remaining.")
      except BaseException as error:
        print(f"error: {error}")
      
