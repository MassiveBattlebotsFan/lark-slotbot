import discord
from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(brief='Shows ping', description='This command shows the ping of the bot')
  @commands.cooldown(1, 15, commands.BucketType.user)
  async def ping(self, ctx):
    color = 0x00FF00
    ping = round(self.bot.latency * 1000, 3)
    if ping >= 1 and ping <= 74:
      color = 0x00FF00
    if ping >= 75 and ping <= 124:
      color = 0xFFA500
    if ping >= 125:
      color = 0xFF0000
    embed = discord.Embed(title="Pong!" , color=color)
    embed.add_field(name = 'Current Ping:', value = f'{ping}ms')
    await ctx.reply(embed = embed)