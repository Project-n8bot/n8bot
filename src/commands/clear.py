import discord
from discord.ext import commands

@commands.command(aliases=['purge', 'prune'])
async def clear(ctx, amount):
    channel = ctx.channel
    
    await channel.purge(limit=amount+1)
    await ctx.send(f'{amount} message(s) has/have been cleared!')

def setup(client):
    client.add_command(clear)