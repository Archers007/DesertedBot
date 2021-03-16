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
inven = []
recipients = []
rolls = []




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

@client.command()
async def help(ctx):
    embeded = discord.Embed(title="Help Menu", description='List of Commands', color=0xbf00ff)
    embeded.add_field(name="Want to Invite me to your server [Click here](https://discord.com/api/oauth2/authorize?client_id=763422049871331339&permissions=8&scope=bot) :thumbsup: you should also check out my GIT account [Here](https://github.com/Archers007)")
    embeded.add_field(name="'''!addreact (emoji)'''", value= str)
    embeded.add_field(name="'''!removeReact'''", value= str)
    embeded.add_field(name="'''!Tban (***Admin ONLY***)'''", value= str)
    embeded.add_field(name="'''!UTban (***Admin ONLY***)'''", value= str)
    embeded.add_field(name="'''!BanTxT (***Admin ONLY***)'''", value= str)
    embeded.add_field(name="'''!Info (**User**)'''", value= str)
    embeded.add_field(name="'''!serverinfo'''", value= str)
    embeded.add_field(name="'''!Cat'''", value= str)
    embeded.add_field(name="'''!Dog'''", value= str)
    embeded.add_field(name="'''!meme'''", value= str)
    embeded.add_field(name="'''!Spam (*Amount of times spammed, message*)'''", value= str)
    embeded.add_field(name="'''!Spamdm (*Amount of times to spam, user to spam, message*)'''", value= str)
    embeded.add_field(name="'''!dm (*User to dm, Message to send*)'''", value= str)
    embeded.add_field(name="'''!Confide (*message to confide*)'''", value= str)
    await ctx.channel.send(embed=embeded)

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