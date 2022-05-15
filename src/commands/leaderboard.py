import discord, database
from discord.ext import commands

@commands.command()
async def leaderboard(ctx):
    embed = discord.Embed(title="Leaderboard", color=discord.Color.teal())
    top10 = database.get_top_users(10)
    for i in range(len(top10)):
        user = discord.utils.get(ctx.guild.members, id=top10[i]["_id"])
        embed.add_field(name=f"{i+1}. {user.name}", value=f"Level: {top10[i]['level']} | XP: {top10[i]['xp']}")
    await ctx.send(embed=embed)

def setup(client):
    client.add_command(leaderboard)