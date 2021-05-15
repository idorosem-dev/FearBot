import discord
from discord.ext import commands
import json
import asyncio

client = commands.Bot(command_prefix = 'f!')

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(activity=discord.Game("Fear"))

@client.command()
async def download(ctx):
    await ctx.send(':x: oops its seen likes the game was not ended... try agin leater...')

client.run('ODQyODU0Nzg1NDA0MzcwOTY0.YJ7XsA.tH_X_-epvgrisPWw2I_B1Vl8kAQ')