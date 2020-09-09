import discord
from discord.ext import commands
import time 

bot = commands.Bot(command_prefix = "al!")

class BotData:
    def __init__(self):
        self.welcome_channel = None
        self.goodbye_channel = None

        self.reaction_role = None
        self.reaction_message = None

botdata = BotData()
@bot.event
async def on_ready():
    print("farhan bhai bot started successfully prifix is = al!dm_all  ")


@bot.command()
async def dm_all(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print( "sent to: " + member.name)
                time.sleep(300)

            except:
                print("Couldn't send to: " + member.name)
              
    else:
        await ctx.channel.send("A message was not provided.")

bot.run ("NzUyOTM2ODUwNjk5NTgzNjA4.X1e5Fg.qNbI0_QK4fmGZHlpIo6HP_vwBM8")
