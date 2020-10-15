import discord
import os
from discord.ext import commands

class UserInfo(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('UserInfo Cog Is A Go, AKA: Cog2')
    
    @commands.command()
    async def Info(self, ctx, user: discord.User):
        em = discord.Embed(timestamp=ctx.message.created_at, colour=0x708DD0)
        em.add_field(name='User ID', value=user.id, inline=True)
        if isinstance(user, discord.Member):
            em.add_field(name='Nick', value=user.nick, inline=True)
            em.add_field(name='Status', value=user.status, inline=True)
            em.add_field(name='In Voice', value=voice_state, inline=True)
            em.add_field(name='Game', value=user.activity, inline=True)
            em.add_field(name='Highest Role', value=role, inline=True)
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
        em.set_thumbnail(url=user.avatar_url_as(format="png"))
        em.set_author(name=user, icon_url=user.avatar_url_as(format="png"))
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(UserInfo(client))
    
def teardown(client):
    print('UserInfo Cog is now not running, AKA: Cog3')