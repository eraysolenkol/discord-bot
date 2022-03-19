from discord.ext import commands

class CogName(commands.Cog):

    def __init__(self, bot):
        self.bot = bot # now you'll use self.bot instead of just bot when referring to the bot in the code

    # instead of bot.command(), you'll use this:
    @commands.command()
    async def cmd(self, ctx): # self is the first param because it's in a class
        # some code

    @commands.command()
    async def othercmd(self, ctx, arg1, *, arg2): # e.g. args work as normal
        # other code

    # this is how you register events, instead of using @bot.event
    @commands.Cog.listener()
    async def on_message(self, message):
        # some code

# this setup function needs to be in every cog in order for the bot to be able to load it
def setup(bot):
    bot.add_cog(CogName(bot))