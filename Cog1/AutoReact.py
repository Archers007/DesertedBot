import discord
import os
import random
from Main import channel_list
from Main import emojii
from discord.ext import commands

class AutoReact(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Autoreact Cog is Running')
        
        
        
    @commands.command()
    async def addreact(self, ctx, args=None):
        if args !=None:
            if ctx.channel.id not in channel_list:
                channel_list.append(ctx.channel.id)
                emojii.append(args)
                print(channel_list)
                print(emojii)
    
    @commands.command()
    async def removeReact(self, ctx):
        emojii.pop(0)
        channel_list.pop(0)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in channel_list:
            await message.add_reaction(emojii[0])
            print(message.content)
    
    
def setup(client):
        client.add_cog(AutoReact(client))

def teardown(client):
    print('AutoReact Cog is now not running')