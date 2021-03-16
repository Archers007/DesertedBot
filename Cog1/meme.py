import discord
import os
import random
import requests
from discord.ext import commands
import time

class Memes(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Meme Cog is Running')
    
    
        
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        seconds = time.time()
        await ctx.channel.send("https://imgflip.com/i?{}".format(str(seconds)))
        
    
def setup(client):
    client.add_cog(Memes(client))
    
def teardown(client):
    print('Meme Cog is now not running')