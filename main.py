import discord
from base64 import b64decode as b64
from discord.ext import tasks, commands
from pretty_help import PrettyHelp, DefaultMenu

from cogs.bal import Bal
from cogs.bet import Bet
from cogs.add import Add
from cogs.ping import Ping
from cogs.sharding import Sharding
from cogs.remove import Remove
from cogs.slots import Slots
from cogs.wins import Wins
from cogs.info import UInfo

def mixedCase(*args):
  total = []
  import itertools
  for string in args:
    a = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in string)))
    for x in list(a): total.append(x)
  return list(total)

secret_token = "T0RNNU9UVTBNVGc1TnpZMU56QTFOelE0LllKUktUQS5HTjJPSzZNNURSUlVneDQzZ1dHb3MxanA3b1E="
#secret_token = "T0RNMU5qYzBPREl4TURrME5EQTRNakV6LllJUzQwdy5PTDVpVUo3NEkwbklDZU93TTZqV0JzNVZ5dUU="

bot = commands.AutoShardedBot(case_insensitive=True,command_prefix=mixedCase("bb!"), help_command=PrettyHelp())
bot.help_command = PrettyHelp()

bot.add_cog(Bal(bot))
bot.add_cog(Bet(bot))
bot.add_cog(Add(bot))
bot.add_cog(Ping(bot))
bot.add_cog(Sharding(bot))
bot.add_cog(Remove(bot))
bot.add_cog(Slots(bot))
bot.add_cog(Wins(bot))
bot.add_cog(UInfo(bot))

ending_note = "{ctx.bot.user.name}\nLieutenantLark, 2021"
nav = DefaultMenu(page_left="⬅️", page_right="➡️", remove="🇽")
color = discord.Color.dark_gold()
bot.help_command = PrettyHelp(no_description="E", navigation=nav, color=color, active_time=10, ending_note=ending_note)

@bot.event
async def on_ready():
  print('Logged on as', bot.user.name, 'with id', bot.user.id)    
  status_change.start()

@tasks.loop(seconds=30)
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
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{servers} server{s} and {members - 1} members'))
#@bot.event
#async def on_command_error(ctx, error):
#    list1 = ["Slow it down, bro!", "Take a chill pill!", "Im not as fast as I used to be...","What are you doing, speedrunning?", "[Creative Title Name Here]", "Ay Ay Ay, wait up!", "stfu you got 9 wpm, keep it that way", "Calm down, don't roleplay as Usain Bolt.", ]
#    randfrolist = random.choice(list1)
#    if isinstance(error, commands.CommandOnCooldown):
#     em = discord.Embed(title=randfrolist, description=f"Try again in ``{round(error.retry_after)}``s.", color=0xFF0000)
#     await ctx.send(embed=em)

bot.run(b64(secret_token).decode())