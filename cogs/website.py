import discord

from discord.ext import commands
from discord import Interaction
from discord import app_commands

class website(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@app_commands.command(name = "website", description = "return Qoqnus-master website url")
	async def ping(self, ctx: Interaction):
		embed = discord.Embed()
		embed.set_image(url='https://qoqnus-master.netlify.app/logo.jpg')
		embed.add_field(name="سایت ققنوس مستر", value="https://Qoqnus-master.netlify.app/")
		await ctx.response.send_message(embed= embed)

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(website(bot))
    else:
        await bot.add_cog(
                website(bot),
                guild=discord.Object(id=bot.config["test-server-id"])
            )