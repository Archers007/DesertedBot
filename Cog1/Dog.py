import discord
import os
import random
import requests
from discord.ext import commands
import os.path
import shutil
import time

class Dog(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Dog Cog is Running')
    
    
        
    @commands.command(pass_context=True)
    async def Dog(self, ctx):

        seconds = time.time()
        print("Seconds since epoch =", seconds)
def teardown(client):
    print('Dog Cog is now not running')