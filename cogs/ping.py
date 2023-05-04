import discord

from discord.ext import commands

from discord import Interaction

from discord import app_commands

class Ping(commands.Cog):

	def __init__(self, bot):		self.bot = bot

	

	@app_commands.command(name = "ping", description = "return Qoqnus bot ping")

	async def ping(self, ctx: Interaction):

		embed=discord.Embed()

		embed.add_field(name="پونگ🏓😃", value="پینگ ققنوس بات {0}میلی ثانیه هستش".format(round(self.bot.latency * 1000, 0)), inline=False)

		await ctx.response.send_message( embed = embed, ephemeral= False)

async def setup(bot):

    if bot.config["test-server-id"] == "":

        await bot.add_cog(Ping(bot))

    else:

        await bot.add_cog(

                Ping(bot),

                guild=discord.Object(id=bot.config["test-server-id"])

            )
