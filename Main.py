import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
from discord import Status

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

CP = ['!',]
channel_list = []
emojii = []
deleteUser = []
deleteUserChannel = []
UserSend = []
Message1 = []
Message2 = []
unloaded = []
extensionsrun = []
hole = []
hole1 = []
hole2 = []
hole3 = []
hole4 = []
hole5 = []
hole6 = []
hole7 = []
hole8 = []
hole9 = []
hole0 = []
hole11 = []
hole12 = []
hole13 = []
hole14 = []
hole15 = []
hole16 = []
hole17 = []
hole18 = []
hole19 = []



client = commands.Bot(command_prefix=CP)

class Loaders():
    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'Cog1.{extension}')
        extensionsrun.append(extension)
        await ctx.channel.send("{} has been successfully loaded".format(extension))
    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f'Cog1.{extension}')
        extensionsrun.remove(extension)
        await ctx.channel.send("{} has been successfully unloaded".format(extension))
    
    @client.command()
    async def unloadall(ctx):
        try:
            client.unload_extension(f'Cog1.{"Dm"}')
            extensionsrun.remove('Dm')
        except:
            print('Dm is already unloaded')
        try:
            client.unload_extension(f'Cog1.{"UserInfo"}')
            extensionsrun.remove('UserInfo')
        except:
            print('UserInfo is already unloaded')
        try:
            client.unload_extension(f'Cog1.{"ServerInfo"}')
            extensionsrun.remove('ServerInfo')
        except:
            print('ServerInfo is already unloaded')
        try:
            client.unload_extension(f'Cog1.{"meme"}')
            extensionsrun.remove('meme')
        except:
            print('meme is already unloaded')
        try:
            client.unload_extension(f'Cog1.{"AutoReact"}')
            extensionsrun.remove('AutoReact')
        except:
            print('AutoReact is already unloaded')
        try:
            client.unload_extension(f'Cog1.{"CustomCommands"}')
            extensionsrun.remove('CustomCommands')
        except:
            print('CustomCommands is already unloaded')
        try:
            client.unload_extension(f'Cog1.{"BanTxT"}')
            extensionsrun.remove('BanTxT')
        except:
            print('BanTxT is already unloaded')
    
    @client.command()
    async def loadall(ctx):
        try:
            client.load_extension(f'Cog1.{"Dm"}')
            extensionsrun.append('Dm')
        except:
            print('Dm is already loaded')
        try:
            client.load_extension(f'Cog1.{"UserInfo"}')
            extensionsrun.append('UserInfo')
        except:
            print('UserInfo is already loaded')
        try:
            client.load_extension(f'Cog1.{"ServerInfo"}')
            extensionsrun.append('ServerInfo')
        except:
            print('ServerInfo is already loaded')
        try:
            client.load_extension(f'Cog1.{"meme"}')
            extensionsrun.append('meme')
        except:
            print('meme is already loaded')
        try:
            client.load_extension(f'Cog1.{"AutoReact"}')
            extensionsrun.append('AutoReact')
        except:
            print('AutoReact is already loaded')
        try:
            client.load_extension(f'Cog1.{"CustomCommands"}')
            extensionsrun.append('CustomCommands')
        except:
            print('CustomCommands is already loaded')
        try:
            client.load_extension(f'Cog1.{"BanTxT"}')
            extensionsrun.append('BanTxT')
        except:
            print('BanTxT is already loaded')

for filename in os.listdir('./Cog1'):
    if filename.endswith('.py'):
        client.load_extension(f'Cog1.{filename[:-3]}')
        extensionsrun.append(f'{filename[:-3]}')
        

@client.command()
async def ChangeCP(ctx, args=None):
    if args !=None:
        CP.append(args)
        CP.pop(0)
        await ctx.channel.send('Successfully Changed Command Prefix to {}'.format(args))

@client.command()
async def ResetCP(ctx):
    CP.append('!')
    CP.pop(0)
    await ctx.channel.send('Successfully Reset Command Prefix to !')

class RunningInfo():
    @client.command()
    async def runninginfo(ctx):
        """Shows Panel Info"""

        embeded = discord.Embed(title="Script Panel", description='On/Off', color=0xEE8700)
        embeded.add_field(name="DM: On", value='Dm' in extensionsrun)
        embeded.add_field(name="User Info: On", value='UserInfo' in extensionsrun)
        embeded.add_field(name="Server Info: On", value='ServerInfo' in extensionsrun)
        embeded.add_field(name="Meme Generator: On", value='meme' in extensionsrun)
        embeded.add_field(name="AutoReact: On", value='AutoReact' in extensionsrun)
        embeded.add_field(name="Spam: On", value='Spam' in extensionsrun)
        embeded.add_field(name="BanTxT: On", value='BanTxT' in extensionsrun)
        embeded.add_field(name="CustomCommands: On", value='CustomCommands' in extensionsrun)
        await ctx.channel.send(embed=embeded)
    
    @client.command()
    async def LOGO(ctx):
        await ctx.channel.send('╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╭╮╭━━━╮╭━╮╭━╮╱╱╱╱╱╱╱╭╮')
        await ctx.channel.send('╰╮╭╮┃╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱┃┃┃╭━╮┃┃╭╯┃╭╯╱╱╱╱╱╱╱┃┃')
        await ctx.channel.send('╱┃┃┃┣━━┳━━┳━━┳┻╮╭╋━━┳━╯┃┃┃╱┃┣╯╰┳╯╰┳┳━━┳┳━━┫┃')
        await ctx.channel.send('╱┃┃┃┃┃━┫━━┫┃━┫╭┫┃┃┃━┫╭╮┃┃┃╱┃┣╮╭┻╮╭╋┫╭━╋┫╭╮┃┃')
        await ctx.channel.send('╭╯╰╯┃┃━╋━━┃┃━┫┃┃╰┫┃━┫╰╯┃┃╰━╯┃┃┃╱┃┃┃┃╰━┫┃╭╮┃╰╮')
        await ctx.channel.send('╰━━━┻━━┻━━┻━━┻╯╰━┻━━┻━━╯╰━━━╯╰╯╱╰╯╰┻━━┻┻╯╰┻━╯')



@client.event
async def on_ready():
    print('Main Is Running')
    print(extensionsrun)
    print('    ___                        _             _     ___   __   __  _        _         _ ')
    print('   /   \ ___  ___   ___  _ __ | |_  ___   __| |   /___\ / _| / _|(_)  ___ (_)  __ _ | |')
    print('  / /\ // _ \/ __| / _ \| `__|| __|/ _ \ / _` |  //  //| |_ | |_ | | / __|| | / _` || |')
    print(' / /_//|  __/\__ \|  __/| |   | |_|  __/| (_| | / \_// |  _||  _|| || (__ | || (_| || |')
    print('/____/  \___||___/ \___||_|    \__|\___| \__,_| \___/  |_|  |_|  |_| \___||_| \__,_||_|')
    print('')
    print('                                                 $$$$$')
    print('                                     $$$$       $$$   $$$$$')
    print('                                    $$$$$$     $$$   $$$$$$$')
    print('                                   $$$ $$$$   $$$  $$$$    $')
    print('                                   $    $$$$ $$$$ $$$')
    print('                                        $$$$$$$$$$   $$$$$')
    print('                                       $$$$$$$$$$$$_$$$$ $$$$$')
    print('                                      $$$$$$$$$$$$$$$$$     $$$')
    print('                                     $$$  $$$$$$$$$$$$        $')
    print('                                    $$   $$$$$$$$$$$$$$$$$')
    print('                                   $$   $$$$ $$$ $$$  $$$$$')
    print('                                   $   $$$$   $$  $$$$   $$$')
    print('                                       $$$     $$   $$$    $$')
    print('                                       $$      $$$   $$$    $')
    print('                                       $$       $$    $$$')
    print('                                       $        $$$    $$')
    print('                                                $$$    $')
    print('                                                $$$')
    print('                                                $$$')
    print('                                                $$$')
    print('                                                $$$')
    print('                                               $$$')
    print('                                              $$$$')
    print('                                            $$$$$')
    print('                                           $$$$$$')
    print('')
                                                                                       

    
client.run(TOKEN)