import discord, aiohttp
from discord.ext import commands
from discord import Color

@commands.command()
async def dog(ctx):
    session = ctx.bot.session
    
    async with session.get('https://dog.ceo/api/breeds/image/random') as response:
        
        image_url = (await response.json())['message']

        embed = discord.Embed(title='Have a cute dog image!', color=Color.teal())
        embed.set_image(url=image_url)
        embed.set_footer(text='Powered by: DOG API')

        await ctx.send(embed=embed)

def setup(client):
    client.add_command(dog)