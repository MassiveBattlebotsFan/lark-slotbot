import discord
from discord.ext import commands
from users import db

class UInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, *, user: discord.Member = None):
      if user is None:
        user = ctx.author
      embed = discord.Embed(color=0x00FF00, title=f"{user.name}'s Stats and Information.")
      embed.set_footer(text=f"ID: {user.id}")
      embed.set_thumbnail(url=user.avatar_url_as(format="png"))
      embed.add_field( name="__**General information:**__",value=f"**Discord Name:** {user}\n"f"**Account created:** {user.created_at.__format__('%A %d %B %Y at %H:%M')}\n",inline=False)

      embed.add_field(name="__**Server-related information:**__",value=f"**Nickname:** {user.nick}\n"f"**Joined server:** {user.joined_at.__format__('%A %d %B %Y at %H:%M')}\n"f"**Roles:** {' '.join([r.mention for r in user.roles[1:]])}")
      await ctx.send(embed=embed)
