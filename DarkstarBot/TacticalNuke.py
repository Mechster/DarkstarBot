import discord
from discord.ext import commands
import asyncio
import traceback


def __init__(self, bot):
        self.bot = bot


class TacticalNuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def chatICBM(self, ctx, iterations=100):
        if await self.defcon1(ctx, "Chat Inter-Continental Ballistic Missile"):
            await ctx.send("Confirmation failed. Defcon 5 status restored")
            return
        await ctx.send("Confirm Fire: Y/N")
        message = await self.bot.wait_for('message', check= self.check)
        message = message.content.lower()

        if message != "y":
            await ctx.send("Firing aborted. Defcon 5 status restored")
            return
        async for iteration in self.arange(iterations):
            mgs = []
            msgs = await ctx.message.channel.history(limit=1).flatten()
            await ctx.message.channel.delete_messages(msgs)

    @commands.command(pass_context = True)
    async def mentionABomb(self, ctx, user: discord.Member, iterations = 100):
        if await self.defcon1(ctx, "Mention @tom Bomb"):
            await ctx.send("Confirmation failed. Defcon 5 status restored")
            return
        await ctx.send("Confirm Fire: Y/N")
        message = await self.bot.wait_for('message', check= self.check)
        message = message.content.lower()

        if message != "y":
            await ctx.send("Firing aborted. Defcon 5 status restored")
            return
        async for iteration in self.arange(iterations):
            await ctx.send("{}".format(user.mention))
            mgs = []
            msgs = await ctx.message.channel.history(limit=1).flatten()
            await ctx.message.channel.delete_messages(msgs)

    async def check(self, m):
        return (m.author.id == 243369955679141888 or m.author.id == 194988977181294602)
    
    async def defcon1(self, ctx, weapon):
        if ctx.message.author.id != 243369955679141888 or m.author.id != 194988977181294602:
            await ctx.send("This account is not authorised. Returning to defcon 5")
            return True
        else:
            await ctx.send("Credentials confirmed. Moving to defcon 1")
            await ctx.send("Enter Confirmation Code:")
            message = await self.bot.wait_for('message', check=self.check)
            code = message.content.strip()

            try:
                code = int(code)
                if code == 178712:
                    await ctx.send("Confirmation code correct, {} now initialising".format(weapon))
                    return False
                await ctx.send("Incorrect code. Returning to defcon 5")
                return True
            except:
                await ctx.send("Unknown error. Returning to defcon 5")
                return True

    async def arange(self, count):
        for i in range(count):
            yield (i)
def setup(bot):
    bot.add_cog(TacticalNuke(bot))
    print('TacticalNuke Commands loaded')