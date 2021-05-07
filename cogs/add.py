import discord
from discord.ext import commands
from users import db

class Add(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def add(self, ctx, *args):
      if args.len > 1:
        money = args[0]
        user = args[1]
        if type(user) == discord.Member: 
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
      elif args.len == 1:
        money = args[0]
        users = db(ctx.author.id)

        #moderator ID list
        idlst = [547941645304201247, 576631663904161812, 743549337434587327]

        if money > 1000000000:
          await ctx.reply("You can't give away that much money at a time!")
          return
        if ctx.author.id in idlst:
          users.add_money(money)
          await ctx.reply(f"Added {money} to {user}s balance!")
        elif ctx.author.id not in idlst:
          print(ctx.author.id)
          await ctx.reply("Only papa Lark and bot moderators can use this command.")
      else:
        await ctx.reply("Ya need to be lark or a moderator to use this commmand.")

