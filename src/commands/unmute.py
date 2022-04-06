import discord, discord.utils
from discord.ext import commands

@commands.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='muted')

    await member.remove_roles(role)
    await ctx.send('Member has been unmuted.')

def setup(client):
    client.add_command(unmute)