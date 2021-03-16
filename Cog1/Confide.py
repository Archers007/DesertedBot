import discord
import os
import random
import requests
from discord.ext import commands

class confide(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Confide Cog is Running')
    
    
        
    @commands.command(pass_context=True)
    async def confide(self, ctx, *, args):
        await ctx.message.delete()
        f = open(".Confide", "x")
        f = open(".Confide", "a")
        f.write('{} has confided this message: {}\n'.format(ctx.author.name, args))
        f.close()
        
        await ctx.channel.send("{} your message has been confided in me".format(ctx.author.name))
        
        
        
        
    
def setup(client):
    client.add_cog(confide(client))
    
def teardown(client):
    print('confide Cog is now not running')