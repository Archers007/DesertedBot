import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
from discord import Status

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

client = commands.Bot(command_prefix='!')

extensionsrun = [

    ]
class Loaders():
    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'Cog1.{extension}')
        extensionsrun.append(extension)
        print(extensionsrun)
        await ctx.channel.send("{} has been successfully loaded".format(extension))
    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f'Cog1.{extension}')
        extensionsrun.remove(extension)
        print(extensionsrun)
        await ctx.channel.send("{} has been successfully unloaded".format(extension))
    
    @client.command()
    async def unloadall(ctx):
        await ctx.channel.send('Successfully unloaded all Cogs')
        for filename in os.listdir('./Cog1'):
           if filename.endswith('.py'):
               client.unload_extension(f'Cog1.{filename[:-3]}')
               extensionsrun.remove(f'{filename[:-3]}')
    
    @client.command()
    async def loadall(ctx):
        await ctx.channel.send('Successfully loaded all Cogs')
        for filename in os.listdir('./Cog1'):
            if filename.endswith('.py'):
                client.load_extension(f'Cog1.{filename[:-3]}')
                extensionsrun.append(f'{filename[:-3]}')

for filename in os.listdir('./Cog1'):
    if filename.endswith('.py'):
        client.load_extension(f'Cog1.{filename[:-3]}')
        extensionsrun.append(f'{filename[:-3]}')
        print(extensionsrun)

class RunningInfo():
    @client.command()
    async def runninginfo(ctx):
        """Shows Panel Info"""

        embeded = discord.Embed(title="Script Panel", description='On/Off', color=0xEE8700)
        if 'Dm' in extensionsrun:
            embeded.add_field(name="DM: On", value='Dm' in extensionsrun)
        else:
            embeded.add_field(name="DM: On", value='Dm' in extensionsrun)
            
        if 'UserInfo' in extensionsrun:
            embeded.add_field(name="User Info: On", value='UserInfo' in extensionsrun)
        else:
            embeded.add_field(name="User Info: On", value='UserInfo' in extensionsrun)
        if 'ServerInfo' in extensionsrun:
            embeded.add_field(name="Server Info: On", value='ServerInfo' in extensionsrun)
        else:
            embeded.add_field(name="Server Info: On", value='ServerInfo' in extensionsrun)
        if 'Memes' in extensionsrun:
            embeded.add_field(name="Meme Generator: On", value='Memes' in extensionsrun)
        else:
            embeded.add_field(name="Meme Generator: On", value='Memes' in extensionsrun)
        if 'TarekRankInsult' in extensionsrun:
            embeded.add_field(name="Tarek Insult: On", value='TarekRankInsult' in extensionsrun)
        else:
            embeded.add_field(name="Tarek Insult: On", value='TarekRankInsult' in extensionsrun)

        await ctx.channel.send(embed=embeded)



@client.event
async def on_ready():
    print('Main Is Running')
client.run(TOKEN)