from discord.ext import commands
import discord, os, aiohttp, asyncio
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')

activity = discord.Game('spoon 🥄')
client = commands.Bot(command_prefix='?', intents=discord.Intents.all(), activity=activity)

client.session = aiohttp.ClientSession()
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot online.')


for file in os.listdir('src\commands'):
    if file.endswith('.py'):
        client.load_extension(f'commands.{file[:-3]}')

for file in os.listdir('src\cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')

client.run(token)