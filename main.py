import discord
import asyncio
from base64 import b64decode as b64
from discord.ext import tasks, commands
from pretty_help import PrettyHelp, DefaultMenu
from random import randrange

from cogs.bal import Bal
from cogs.bet import Bet
from cogs.add import Add
from cogs.ping import Ping

def mixedCase(*args):
  total = []
  import itertools
  for string in args:
    a = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in string)))
    for x in list(a): total.append(x)
  return list(total)

secret_token = "T0RNNU9UVTBNVGc1TnpZMU56QTFOelE0LllKUktUQS5HTjJPSzZNNURSUlVneDQzZ1dHb3MxanA3b1E="
#secret_token = "T0RNMU5qYzBPREl4TURrME5EQTRNakV6LllJUzQwdy5PTDVpVUo3NEkwbklDZU93TTZqV0JzNVZ5dUU="

bot = commands.Bot(case_insensitive=True,command_prefix=mixedCase("sbd!"), help_command=PrettyHelp())
bot.help_command = PrettyHelp()

#cog loading
bot.add_cog(Bal(bot))
bot.add_cog(Bet(bot))
bot.add_cog(Add(bot))
bot.add_cog(Ping(bot))

ending_note = "{ctx.bot.user.name}\nLieutenantLark, 2021"

nav = DefaultMenu(page_left="⬅️", page_right="➡️", remove="🇽")

color = discord.Color.dark_gold()

l1 = randrange(50, 100)
l2 = randrange(101, 200)
l3 = randrange(201, 300)

bot.help_command = PrettyHelp(no_description="E", navigation=nav, color=color, active_time=10, ending_note=ending_note)

@bot.event
async def on_message(message):
  for x in message.mentions:
    if (x == bot.user):
      await message.channel.reply("**My prefix is sb! try using sb!help for further assistance.**")
  await bot.process_commands(message)

@bot.event
async def on_ready():
  print('Logged on as', bot.user.name, 'with id', bot.user.id)    
  status_change.start()

@tasks.loop(seconds=45)
async def status_change():
  servers = len(bot.guilds)
  s = ''
  if len(bot.guilds) == 1:
    s = ''
  elif len(bot.guilds) >=2:
    s = "s"
  activity_string = f'{servers} server{s}.'
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity_string))
  servers = len(bot.guilds)
  members = 0
  for guild in bot.guilds:
    members += guild.member_count - 1
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{servers} server{s} and {members} members'))

@bot.command()
async def servers(ctx):
  message = await ctx.send('Fetching Server Info...')
  await asyncio.sleep(2)
  await message.delete()
  embed = discord.Embed(title="Server Count")
  embed.add_field(name=f'{bot.user.name} is used in ', value=f'{len(bot.guilds)} servers.')
  await ctx.send(embed=embed)

@bot.command()
async def close(ctx):
  my_ID = 547941645304201247
  if (ctx.author.id == my_ID):
    msg = await ctx.send("Closing")
    await asyncio.sleep(2)
    await msg.delete()
    message = await ctx.send("Bot Offline!")
    await bot.close()
    await asyncio.sleep(10)
    await message.delete()
  elif (ctx.author.id != my_ID):
    print(ctx.author.id)
    await ctx.reply("Only papa Lark can use this command.")

#@bot.command()
#async def wlr(ctx):
#    auth(str(ctx.author.id))
#    user = myDB.get_user(str(ctx.author.id))
#    embedVar = discord.Embed(title="W/L/T",
#                             description="Here's your current stats!",
#                             color=0x00ff00)
#    embedVar.add_field(name="Wins", value=f'{user.wins}', inline=True)
#    embedVar.add_field(name="Losses", value=f'{user.losses}', inline=True)
#    embedVar.add_field(name="Ties", value=f'{user.ties}', inline=True)
#    embedVar.add_field(name="Win %", value=get_ratio(user.stats), inline=False)
#    await ctx.send(embed=embedVar)

#@bot.event
#async def on_command_error(ctx, error):
#    list1 = ["Slow it down, bro!", "Take a chill pill!", "Im not as fast as I used to be...","What are you doing, speedrunning?", "Creative-Title-Name-Here"]
#    randfrolist = random.choice(list1)
#    if isinstance(error, commands.CommandOnCooldown):
#     em = discord.Embed(title=randfrolist, description=f"Try again in ``{round(error.retry_after)}``s.", color=0xFF0000)
#     await ctx.send(embed=em)

bot.run(b64(secret_token).decode())