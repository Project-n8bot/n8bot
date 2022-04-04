import discord, discord.utils
from discord import Color
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embed = discord.Embed(title=f'Error: {error}', description='Type ?help to see a list of commands', color=discord.Color.red())
        
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):

        guild = member.guild
        channel = discord.utils.get(guild.channels.lower(), name='welcome')
        role = discord.utils.get(guild.roles, name='Member') # make case insensitive later

        embed = discord.Embed(title=f'Welcome to the server {member.name}!', description='Hope you enjoy your stay :)', color=discord.Color.teal())

        embed.set_thumbnail(url=member.avatar_url)

        await member.add_roles(role)
        msg = await channel.send(embed=embed)
        await msg.add_reaction('👋')

def setup(client):
    client.add_cog(Events(client))