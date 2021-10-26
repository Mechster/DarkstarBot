import discord
from discord.ext import commands
import asyncio
import traceback
import random
import datetime

startup_extensions = ["Admin", "TacticalNuke"]
bot = commands.Bot(command_prefix="//")

rankList = ["Super admin", "Founder", "Admin"]
ban_list = []


@bot.event
async def on_ready():
    print("Ready to go")
    print("Logged in as:", bot.user.name)
    print("My ID is:", bot.user.id)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You forgot to tell me something!")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("You told me something that doesn't make sense!")
    elif isinstance(error, commands.CommandInvokeError):
        print("Exception in command '{}', {}".format(ctx.command.qualified_name, error.original))
        traceback.print_tb(error.original.__traceback__)


@bot.event
async def on_member_join(user: discord.Member):
    guild = bot.get_guild(543948708560109587)
    async for i in getRoles(guild.roles):
        if i.name == "Normals":
            role = i
            break
    await user.add_roles(role)


@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="Waste of time", description="Little bitch to code.", color=0xeee657)
    embed.add_field(name="Author", value="Mechanical Assassin")
    await ctx.send(embed=embed)


@bot.command()
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s information".format(user.name), description="Here's everything I know",
                          colour=0xff0000)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="User", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest rank", value=user.top_role)
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong :ping_pong:")


async def getRoles(roles):
    for role in roles:
        yield(role)


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))


bot.run("TOKEN")
