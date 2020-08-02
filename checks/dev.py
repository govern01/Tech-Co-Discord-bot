from discord.ext import commands
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('bot.ini')


class NotDev(commands.CommandError):
    pass


def is_dev(ctx: commands.Context):
    author_id = str(ctx.author.id)
    dev_ids_str = cfg['DEV']['developer_ids']  # dev ids in CSV style
    dev_ids = dev_ids_str.split(',')
    if author_id in dev_ids:
        return True
    else:
        raise NotDev()
