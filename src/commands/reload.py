import discord
from discord.ext import commands

@commands.command()
async def reload(ctx, extension):
    client = ctx.bot

    client.reload_extension(extension)
    await ctx.send(f'{extension} has been reloaded.')