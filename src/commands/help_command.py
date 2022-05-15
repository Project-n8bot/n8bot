import discord, os
from discord.ext import commands
from discord import Color
import json

@commands.command(aliases=['help'])
async def help_command(ctx, command=None):
    commands = json.load(open("src/commands.json"))
    if command is None:
        embed = discord.Embed(title='Help Menu', colour=Color.teal())
        for command in commands:
            command_data = commands[command]
            embed.add_field(name=command, value=command_data['description'])
        
        await ctx.send(embed=embed)
    else:
        if command in commands:
            embed = discord.Embed(title=command, colour=Color.teal(), description=commands[command]['description'])
            command_data = commands[command]
            for arg in command_data['args']:
                embed.add_field(name=arg['name'], value=arg['description'])
            await ctx.send(embed=embed)
        else:
            await ctx.send("Command not found")

def setup(client):
    client.add_command(help_command)
