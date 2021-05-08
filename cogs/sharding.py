import discord
from discord.ext import commands

class Sharding(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def shardinfo(self, ctx):
    shards = self.bot.shards
    for i in range(len(shards)):
      await ctx.send(f'Shard {i} has latency {round(shards[i].latency * 1000, 3)}ms')