import discord
import os
from discord.ext import commands
from discord import Member

class CustomComands(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Custom commands Cog Is A Go')
    
    @commands.command()
    async def status(self, ctx, member: Member):
        await ctx.message.delete()
        await ctx.channel.send('{} is playing {}'.format(member, member.ActivityName))

def setup(client):
    client.add_cog(CustomComands(client))
    
def teardown(client):
    print('Custom Comands Cog is now not running')