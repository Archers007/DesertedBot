import discord
import os
import random
import requests
from discord.ext import commands
import os.path
import shutil
import time

class Cat(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cat Cog is Running')
    
    
        
    @commands.command(pass_context=True)
    async def Cat(self, ctx):

        seconds = time.time()
        print("Seconds since epoch =", seconds)

        await ctx.channel.send("https://cataas.com/cat?{}" .format(str(seconds)))
        
        
        
    
    
def setup(client):
    client.add_cog(Cat(client))
    
def teardown(client):
    print('Cat Cog is now not running')