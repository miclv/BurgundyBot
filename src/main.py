import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
Token = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='?')


#class MyClient(discord.Client):

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))


@bot.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


#client = MyClient()
bot.run(Token)