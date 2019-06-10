import discord, json, asyncio, time, random, aiohttp, re, os, sys, math, asyncpg
from time import gmtime
from discord.ext import commands

#-------------------DATA---------------------
bot = commands.Bot(command_prefix='-', description=None)
bot.remove_command("help")
underworking = ":warning: **Nem, ez még nincs kész...** :warning:"
timer = time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Brawlhalla"))

#-----------------COMMANDS-------------------

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


bot.run('DISCORD_TOKEN')
