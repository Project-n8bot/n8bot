import discord
from discord.ext import commands

@commands.command()
async def reload(ctx, extension):
    client = ctx.bot

    client.reload_extension(f'commands.{extension}')
    await ctx.send(f'Reloading {extension}.')

def setup(client):
    client.add_command(reload)