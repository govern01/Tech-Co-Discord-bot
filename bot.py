from configparser import ConfigParser
from discord.ext import commands
from extensions_list import extensions
import discord

cfg = ConfigParser()
cfg.read('bot.ini')

bot = commands.Bot(command_prefix=cfg['BOT']['default_prefix'])


@bot.event
async def on_ready():
    print("Bot is initialising")
    for extension in extensions:
        bot.load_extension(extension)
    print("Bot initialised")


if __name__ == "__main__":
    bot.run(cfg['BOT']['token'])
