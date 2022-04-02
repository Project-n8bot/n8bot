import discord
from discord.ext import commands

@commands.command()
async def ban(ctx, member: discord.Member, reason=None):
    guild = ctx.guild

    embed = discord.Embed(title='You have been banned!', color=discord.Color.teal())

    embed.add_field(name='From:', value=guild.name)
    embed.add_field(name='For:', value=reason)

    embed.set_thumbnail(url=guild.icon_url)

    await member.ban()
    await member.send(embed=embed)
    await ctx.send('Member has been banned.')

def setup(client):
    client.add_command(ban)