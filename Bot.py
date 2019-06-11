import discord, json, math, os, re
from discord.ext.commands import Bot

my_bot = Bot(command_prefix="!")

@my_bot.event
async def on_message(message):
    if message.content.startswith('!meme'):
        await message.channel.send('Meme')

my_bot.run('DISCORD_TOKEN')
