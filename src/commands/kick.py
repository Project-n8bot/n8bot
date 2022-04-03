import discord
from discord.ext import commands

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, reason=None):
    guild = ctx.guild

    embed = discord.Embed(title='You have been kicked!', color=discord.Color.teal())

    embed.add_field(name='From:', value=guild.name)
    embed.add_field(name='For:', value=reason)

    embed.set_thumbnail(url=guild.icon_url)

    await member.kick()
    await member.send(embed=embed)
    await ctx.send('Member has been kicked.')

def setup(client):
    client.add_command(kick)