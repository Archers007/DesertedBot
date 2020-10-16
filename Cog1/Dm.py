import discord
import os
from discord.ext import commands

class Dm(commands.Cog):
    
    def __inti__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Dm Cog is Running, AKA: Cog')
        
    
    @commands.command(pass_context=True)
    async def dm(self, ctx, user: discord.User, *, args=None):
        if args !=None:
            #Message
            embeD = discord.Embed(
                description=("`{}` From the Server: `{}`, Sent you this message:`{}`".format(ctx.author.name, ctx.author.guild, args)),
                color=0x0000FF,
                title='New Message From {}'.format(ctx.author.name)
            )
            embeD.set_thumbnail(url=ctx.author.avatar_url)
            embeD.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await user.send(embed=embeD)
            await ctx.message.delete()
         
         #Alert for sent
         
        embed = discord.Embed(
            color=0x0000FF,
            title='Message Was Sent to: `{}`'.format(user.name)
        )
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Dm(client))
    
def teardown(client):
    print('Dm Cog is now not running, AKA: Cog')