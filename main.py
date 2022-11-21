import discord
from bot import bot_command
from coins import coins_command
from godot import godot_command
from dotenv import load_dotenv
from os import getenv


bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

load_dotenv()
bot.add_application_command(godot_command)
bot.add_application_command(coins_command)
bot.add_application_command(bot_command)
bot.run(getenv('TOKEN'))
