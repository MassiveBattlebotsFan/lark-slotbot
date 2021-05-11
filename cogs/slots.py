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

class Blackjack():
  def __init__(self):
    #player and bot
    self.p_num = randrange(1, 13) + randrange(1, 13) + randrange(1, 13)
    self.b_num = randrange(1, 13) + randrange(1, 13) + randrange(1, 13)
    self.p_over = False
    self.b_over = False
    self.p_win = False
    self.b_win = False
    self.tie = False

  def logic(self):
    #L O G I K  1 0 0
    if self.p_num > 21:
     self.p_over = True
    if self.b_num > 21:
      self.b_over = True
    if self.p_num > self.b_num and not self.p_over:
      self.p_win = True
    if self.b_num > self.p_num and not self.b_over:
      self.b_win = True
    #pain
    if (self.p_over and self.b_over) or (self.p_num == self.b_num):
      self.tie = True
    return self.p_num, self.p_over, self.p_win, self.b_num, self.b_over, self.b_win, self.tie

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
    
    #this is what you can work with, in order as returned by Blackjack.logic():
    #p_num, p_over, p_win, b_num, b_over, b_win, tie
    blackjack = Blackjack()

    #your gui output thingy goes here
    await ctx.send(blackjack.logic())
    