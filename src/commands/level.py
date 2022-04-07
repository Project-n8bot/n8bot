import discord, database
from discord.ext import commands

@commands.command(aliases=["rank"])
async def level(ctx):
    user_id = ctx.message.author.id

    await ctx.send("You are now level " + database.get_level(user_id))

def setup(client):
    client.add_command(level)