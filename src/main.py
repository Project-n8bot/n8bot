from discord.ext import commands
import discord
from dotenv import load_dotenv

import os

load_dotenv()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot is ready.')
    print(f"Logged in as: {client.user.name}")


if __name__ == '__main__':
    client.run(os.getenv('TOKEN'))