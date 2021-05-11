import discord
from discord.ext import commands
#import main
import asyncio
from random import randrange
from users import db

def num2emote(num: int):
  #init number emojis, using dict to be safe
  numbers = {0 : ':zero:', 1 : ':one:', 2 : ':two:', 3 : ':three:', 4 : ':four:', 5 : ':five:', 6 : ':six:', 7 : ':seven:', 8 : ':eight:', 9 : ':nine:'}

  numstr = str(num)
  emotestr = ''
  for char in numstr:
    emotestr += numbers[int(char)]

class Slots(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1, 1, commands.BucketType.user)
  async def slots(self,ctx, money: int = None):
    
    #did they gib me money?
    if money == None:
      await ctx.send("You need to supply money, this ain't free :rofl:")
      return

    #generate two players and add three draws together
    players = {'player' : randrange(1, 10) + randrange(1, 10) + randrange(1, 10), 'bot' : randrange(1, 10) + randrange(1, 10) + randrange(1, 10)}
    
    #why did i do this again? ah well...
    p = players['player']
    b = players['bot']
    
    #attributes i should have made into a class...
    p_over = False
    b_over = False
    p_win = False
    b_win = False
    tie = False

    #L O G I K  1 0 0
    if p > 21:
      p_over = True
    
    if b > 21:
      b_over = True

    if p > b and not p_over:
      p_win = True

    if b > p and not b_over:
      b_win = True
    
    #pain
    if (p_over and b_over) or (p == b):
      tie = True

    #your gui output thingy goes here