import discord, discord.utils
from discord.ext import commands

@commands.command()
@commands.has_permissions(ban_members=True)
async def mute(ctx, member: discord.Member):
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name='muted')
    
    if role:
        await member.add_roles(role)
        await ctx.send('Member has been muted. :skull:')
    else:
        permissions = discord.Permissions(send_messages=False)
        member_role = discord.utils.get(guild.roles, name='member')
        position = member_role.position + 1
        
        await guild.create_role(name='muted', permissions=permissions)

        role = discord.utils.get(guild.roles, name='muted')

        await role.edit(position=position)

        for category in guild.categories:
            await category.set_permissions(role, send_messages=False)
            
        await member.add_roles(role)
        await ctx.send('Member has been muted. :skull:')

def setup(client):
    client.add_command(mute)