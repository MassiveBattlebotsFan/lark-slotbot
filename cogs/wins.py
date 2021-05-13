import discord
from discord.ext import commands
#import main
import random
from users import db

class Wins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wlr(self, ctx, user: discord.Member = None):
      if user == None:
        user = ctx.author
        
      users = db(user.id)
      wins = users.get_wins()
      losses = users.get_losses()
      ties = users.get_ties()


      if wins == 0 and losses == 0:
        perc = 'n/a'
        games = "0"
        embedVar = discord.Embed(title=f"{user}'s W/L Ratio", description="", color=0x00ff00)
        embedVar.add_field(name="Wins", value=f'{wins}', inline=True)
        embedVar.add_field(name="Losses", value=f'{losses}', inline=True)
        embedVar.add_field(name="Ties", value=f'{ties}', inline=True)
        embedVar.add_field(name="Game Count", value=f'{games}', inline=True)
        embedVar.add_field(name="You have a:", value=f"{perc} win average. \nPlay some more to get an accurate percentage", inline=False)
        await ctx.send(embed=embedVar)
      else:
        games = users.get_games()
        perc = wins / games * 100 
        embedVar = discord.Embed(title=f"{user}'s W/L Ratio", description="", color=0x00ff00)
        embedVar.add_field(name="Wins", value=f'{wins}', inline=True)
        embedVar.add_field(name="Losses", value=f'{losses}', inline=True)
        embedVar.add_field(name="Ties", value=f'{ties}', inline=True)
        embedVar.add_field(name="Game Count", value=f'{games}', inline=True)
        embedVar.add_field(name="You have a:", value=f"{round(perc)}% win average.", inline=False)
        await ctx.send(embed=embedVar)








