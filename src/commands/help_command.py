import discord, os
from discord.ext import commands
from discord import Color
from inspect import signature

@commands.command(aliases=['help'])
async def help_command(ctx):
    embed = discord.Embed(title='Help Menu', colour=Color.teal())
    for file in os.listdir('src\commands'):
        file_name = file[:-3].title()
        if not file.startswith('__'):
            #arguments = str(signature(f'{file[:-3]}.{file[:-3]}()'))
            embed.add_field(name=file_name, value=(f'{file_name} command'), inline=False)
            #await ctx.send(arguments)
    
    await ctx.send(embed=embed)

def setup(client):
    client.add_command(help_command)
