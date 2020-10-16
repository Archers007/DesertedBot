import discord
import os
import random
from discord.ext import commands

class TarekInsult(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('TarekInsult Cog is Running')
    
    
    @commands.command()
    async def rank(self, ctx):
        Insult = [
        
        '<@!363735258279051265> u suck',
        '<@!363735258279051265> hahahhahhahaahhahahha ur not #1',
        '<@!363735258279051265> ur never gonna get there u absolute apricot',
        '<@!363735258279051265> Take the L loser your not first',
        '<@!363735258279051265> your the owner and your still not first'
        
        
        ]
        response = random.choice(Insult)
        await ctx.channel.send(response)
    
    @commands.command()
    async def AddInsult(self, ctx, *args):
        if args:
            Insult.append(' '.join(args))
            print(Insult)
            await ctx.message.delete()
            await ctx.send(Insult)
    
def setup(client):
    client.add_cog(TarekInsult(client))

def teardown(client):
    print('TarekInsult Cog is now not running')