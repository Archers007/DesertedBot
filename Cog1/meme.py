import discord
import os
import random
import requests
from discord.ext import commands

class Memes(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Meme Cog is Running')
    
    
        
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        f = open("LookFor.txt", "w")
        f.write('\n')
        f.close()
        
        
        url = "https://imgflip.com/i"
        x = requests.get(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
        
        f = open("LookFor.txt", "w")
        f.write(x.text)
        f.close()
        
        
        file1 = open('LookFor.txt', 'r')
        Lines = file1.readlines()
        
        count = 0
        
        for line in Lines:
            count += 1
            
            if count == 58:
                print(line)
                z = line[-33:-5]
        print(z)
        
        await ctx.channel.send(z)
        
    
def setup(client):
    client.add_cog(Memes(client))
    
def teardown(client):
    print('Meme Cog is now not running')