from discord.ext import commands
import os
import random
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def roll(ctx):
    roll_index = random.randint(0, 1000)
    rolled_role = 'none'

    if roll_index % 5 == 0:
        rolled_role = 'Top'
    elif roll_index % 5 == 1:
        rolled_role = 'Jg'
    elif roll_index % 5 == 2:
        rolled_role = 'Mid'
    elif roll_index % 5 == 3:
        rolled_role = 'Adc'
    elif roll_index % 5 == 4:
        rolled_role = 'Sup'

    await ctx.send(rolled_role)


bot.run(token)
