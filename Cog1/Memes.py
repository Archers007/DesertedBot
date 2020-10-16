import discord
import os
import random
from discord.ext import commands

class Memes(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Meme Cog is Running')
    
    
        
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        rl1 = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        ]
    
        rl2 = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        ]
            
        rn1 = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0',
        
        ]
            
        rl3 = random.choice(rl1)
        rl4 = random.choice(rl2)
        rn2 = random.choice(rn1)
        await ctx.channel.send('https://imgflip.com/i/4hy{}{}{}'.format(rl3, rl4, rn2,))
    
def setup(client):
    client.add_cog(Memes(client))
    
def teardown(client):
    print('Meme Cog is now not running')