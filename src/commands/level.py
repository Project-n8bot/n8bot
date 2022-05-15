import discord, database
from discord.ext import commands

@commands.command(aliases=["rank"])
async def level(ctx):
    user_id = ctx.message.author.id
    level = str(database.get_level(user_id))
    xp = str(database.get_xp(user_id))
    embed = discord.Embed(title=f"{ctx.message.author.name}'s Stats", color=discord.Color.teal())
    embed.add_field(name="Level", value=level)
    embed.add_field(name="XP", value=xp)
    await ctx.send(embed=embed)

def setup(client):
    client.add_command(level)