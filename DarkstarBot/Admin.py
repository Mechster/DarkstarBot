import discord
from discord.ext import commands
import asyncio
import datetime

rankList = ["Super admin", "Founders", "Admin", "ESL 2020"]


def __init__(self, bot):
        self.bot = bot


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def promote(self, ctx, user: discord.Member, *, role):
        if await self.rankcheck(ctx):
            role = role.strip()
            await user.edit(role=discord.utils.get(user.guild.roles, name=role))

    @commands.command()
    async def clear(self, ctx):
        if await self.rankcheck(ctx):
            return
        msgs = await ctx.message.channel.history(limit=200).flatten()
        await ctx.message.channel.delete_messages(msgs)

    # @commands.command(pass_context=True, hidden=True)
    # async def setname(self, ctx, *, name):
    #     if rankcheck(ctx):
    #         return
    #     name = name.strip()
    #
    #     try:
    #         await self.bot.edit_profile(username=name)
    #     except:
    #         await self.bot.say("Failed to change name")
    #     else:
    #         await self.bot.say("Successfuly changed name to {}".format(name))

    # @commands.command(pass_context=True, hidden=True)
    # async def setgame(self, ctx, *, game):
    #     if rankcheck(ctx):
    #         return
    #     game = game.strip()
    #     if game != "":
    #         try:
    #             await self.bot.change_presence(game=discord.Game(name=game))
    #         except:
    #             await self.bot.say("Failed to change game")
    #         else:
    #             await self.bot.say("Successfuly changed game to {}".format(game))

    # @commands.command(pass_context=True)
    # async def kick(self, ctx, user: discord.Member, *, reason):
    #     if rankcheck(ctx):
    #         return
    #     await self.kickfunc(ctx, user, reason)
    #
    # @commands.command(pass_context=True)
    # async def ban(self, ctx, user: discord.Member, *, reason):
    #     if rankcheck(ctx):
    #         return
    #     await self.banfunc(ctx, user, reason)

    @commands.command()
    async def nickname(self, ctx, user: discord.Member, *, name):
        if await self.rankcheck(ctx):
            return
        name = name.strip()
        try:
            await user.edit(nick=name)
        except:
            await ctx.send("Failed to change name")
        else:
            await ctx.send("Name successfully changed!")

    @commands.command()
    async def clearnick(self, ctx, user: discord.Member):
        if await self.rankcheck(ctx):
            return
        try:
            await user.edit(nick=None)
        except:
            await ctx.send("Failed to change name")
        else:
            await ctx.send("Name successfully changed!")

    @commands.command(pass_context=True)
    async def delete(self, ctx, num: int):
        if await self.rankcheck(ctx):
            return
        number = num
        msgs = await ctx.message.channel.history(limit=number).flatten()
        await ctx.message.channel.delete_messages(msgs)
   
    @commands.command()
    async def membertime(self, ctx, user: discord.Member):
        if await self.rankcheck(ctx):
            return
        fmt = "%Y-%m-%d %H:%M:%S"
        joined = user.joined_at.strftime(fmt)

        now = datetime.datetime.utcnow().strftime(fmt)

        timedelta = datetime.datetime.strptime(now, fmt) - datetime.datetime.strptime(joined, fmt)

        await ctx.send("This user has been a member for {} days".format(timedelta.days))

    # async def banfunc(self, ctx, user: discord.Member, reason):
    #
    #     flag = True
    #     while flag:
    #         await self.bot.say("How many days do you want to ban them for? (-1-->permaban)")
    #         message = await self.bot.wait_for_message(author=ctx.message.author)
    #         days = message.content.strip()
    #         try:
    #             days = int(days)
    #             if days < -1:
    #                 await self.bot.say("you gave me an invalid number of days")
    #
    #             else:
    #                 flag = False
    #
    #         except TypeError:
    #             await self.bot.say("you gave me an invalid number of days")
    #     dateandtime = datetime.datetime.utcnow()
    #     if days == -1:
    #         bantype = "Permaban"
    #         unban = "never"
    #     else:
    #         bantype = "{} day ban".format(days)
    #         unban = str(dateandtime + datetime.timedelta(days=days))
    #
    #     await self.bot.send_message(user, "You have been banned from the server. Reason: {}. Time of "
    #                                  "unban is {}".format(reason, unban))
    #     await self.bot.send_message(user, "If you wish to rejoin please contact a server mod on or after the "
    #                                  "aforementioned date")
    #
    #     channel = self.bot.get_channel('576507719104593994')
    #
    #     await self.bot.say("Thou hath been stuck with the ban hammer :hammer:")
    #     await self.bot.ban(user)
    #
    #     time = datetime.datetime.now().time()
    #     date = datetime.date.today()
    #     await self.bot.send_message(channel, """Time: {} GMT
    #     Date: {}
    #     Person involved: {}
    #     Reason for ban: {}
    #     Action taken: {}
    #     Time of unban: {}
    #     Action taker: {}""".format(time, date, user.name, reason, bantype, unban, ctx.message.author.name))
    #
    # async def kickfunc(self, ctx, user: discord.Member, reason):
    #     channel = self.bot.get_channel('576507719104593994')
    #     if rankcheck(ctx):
    #         return
    #
    #     await self.bot.send_message(user, "You have been kicked from the server. Reason: {}".format(reason))
    #
    #     if user != "":
    #         await self.bot.say("Bye Bye {}".format(user.name))
    #         await self.bot.kick(user)
    #
    #     else:
    #         await self.bot.say("You forgot to give me a user!")
    #
    #     time = datetime.datetime.now().time()
    #     date = datetime.date.today()
    #     await self.bot.send_message(channel, """Time: {} GMT
    # Date: {}
    # Person involved: {}
    # Reason for kick: {}
    # Action taken: kick
    # Action taker: {}""".format(time, date, user.name, reason, ctx.message.author.name))

    async def rankcheck(self, ctx):
        if ctx.message.author.top_role.name not in rankList:
            await ctx.send("You do not have permission to use this command")
            return True
        return False


def setup(bot):
    bot.add_cog(Admin(bot))
    print('Admin Commands loaded')
