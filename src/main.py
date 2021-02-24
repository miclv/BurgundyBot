import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
Token = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


bot.run(Token)