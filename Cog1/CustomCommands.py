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
    async def joining(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send('hey guys {} is going to join u guys in a moment or two'.format(ctx.author.nick))
    
    @commands.command()
    async def booting(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send('hey guys {} is booting up so leave him alone'.format(ctx.author.nick))
        
    @commands.command()
    async def no(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send('hey guys {} is not going to join you guys rn'.format(ctx.author.nick))
    
    @commands.command()
    async def status(self, ctx, member: Member):
        await ctx.message.delete()
        await ctx.channel.send('{} is playing {}'.format(member, member.Game))

def setup(client):
    client.add_cog(CustomComands(client))
    
def teardown(client):
    print('Custom Comands Cog is now not running')