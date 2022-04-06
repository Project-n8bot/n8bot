import discord
from discord.ext import commands

@commands.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member: discord.Member):
    guild = ctx.guild
    banned_users = await guild.bans()
    
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name and user.discriminator) == (member_name and member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'User has been unbanned.')

def setup(client):
    client.add_command(unban)