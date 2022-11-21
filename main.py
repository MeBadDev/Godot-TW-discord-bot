import discord
import logging
from bot import bot_command
from coins import coins_command
from godot import godot_command
from dotenv import load_dotenv
from os import getenv


bot = discord.Bot()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    print('Bot Ready!')
    print(f"Logged in as {bot.user}")

load_dotenv()
bot.add_application_command(godot_command)
bot.add_application_command(coins_command)
bot.add_application_command(bot_command)
bot.run(getenv('TOKEN'))
