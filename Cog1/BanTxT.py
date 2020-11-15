import discord
import os
from discord.ext import commands
from discord import Member
from Main import deleteUser
from Main import deleteUserChannel

class Deleter(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Deleter Cog Is A Go')
        
    @commands.command()
    async def Tban(self, ctx, user: discord.User):
        if ctx.author.id not in deleteUser:
            deleteUser.append(user.id)
            print(deleteUser)
        
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in deleteUser:
            await message.delete()
    
    @commands.command()
    async def UTban(self, ctx, user: discord.User):
        if ctx.author not in deleteUser:
            deleteUser.remove(user.id)
    
    @commands.command()
    async def Ban?(self, ctx):
        await ctx.channel.send(deleteUser)
    

def setup(client):
    client.add_cog(Deleter(client))
    
def teardown(client):
    print('Deleter Cog is now not running')