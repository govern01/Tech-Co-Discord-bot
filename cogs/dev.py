from discord.ext import commands
from checks.dev import is_dev
from checks.dev import NotDev
from extensions_list import extensions
import asyncio


class DevCog(commands.Cog, name="Developer Commands"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx: commands.Context):
        return is_dev(ctx)

    @commands.command()
    async def reload_cog(self, ctx: commands.Context, extension: str = None):
        if not extension:
            await ctx.send('dw father I shall reload the extensions')
            with ctx.typing():
                await asyncio.sleep(0.5)  # this is only here because extensions load too quickly atm
                for ex in extensions:
                    self.bot.reload_extension(ex)
                await ctx.send('Extensions have been reloaded father')
        else:
            await ctx.send(f'reloading {extension}')
            with ctx.typing():
                await asyncio.sleep(0.5)
                self.bot.reload_extension(extension)
                await ctx.send(f'{extension} reloaded successfully')

    @commands.command(name="debug")
    async def debug_command(self, ctx: commands.Context):
        await ctx.send("Debug Command Called!")

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, NotDev):
            await ctx.send("You are not a dev, get that nose out of where the sun don't shine :triumph:")


def setup(bot: commands.Bot):
    bot.add_cog(DevCog(bot))


def teardown(bot: commands.Bot):
    bot.remove_cog('Developer Commands')
