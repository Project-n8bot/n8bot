import discord, asyncio
from discord.ext import commands

@commands.command(aliases=['purge', 'prune'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    channel = ctx.channel
    
    await channel.purge(limit=amount+1)
    msg = await ctx.send(f'`{amount}` message(s) has/have been cleared!')

    await asyncio.sleep(2)
    await msg.delete()

def setup(client):
    client.add_command(clear)