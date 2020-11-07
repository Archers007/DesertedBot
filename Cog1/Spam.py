import discord
import os
import random
from discord.ext import commands
from Main import UserSend
from Main import Message1
from Main import Message2

class Spam(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Spam Cog is Running')
        
        
        
    @commands.command(pass_context=True)
    async def Spamdm(self, ctx, user: discord.User, *, args=None):
        if args !=None:
            
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            await user.send(args)
            
    
    @commands.command(pass_context=True)
    async def Spam(self, ctx, *, args=None):
        if args !=None:
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            await ctx.channel.send(args)
            
    @commands.command()
    async def Coolfont(self, ctx, args1=None, args2=None, args3=None):
        if args1 !=None:
            if args2 !=None:
                if args3 !=None:
                    await ctx.channel.send('https://patorjk.com/software/taag/#p=display&h=1&v=1&f=Ogre&t={}%20{}%20{}'.format(args1, args2, args3))
                else:
                    await ctx.channel.send('https://patorjk.com/software/taag/#p=display&h=1&v=1&f=Ogre&t={}%20{}'.format(args1, args2))
            else:
                await ctx.channel.send('https://patorjk.com/software/taag/#p=display&h=1&v=1&f=Ogre&t={}'.format(args1))
    
def setup(client):
        client.add_cog(Spam(client))

def teardown(client):
    print('Spam Cog is now not running')