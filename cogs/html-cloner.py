import discord
import os

from discord.ext import commands
from discord import Interaction
from discord import app_commands

class html_cloner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@app_commands.command(name = "html-cloner", description = "clone front-end file of website")
	async def html_cloner(self, ctx: Interaction, url:str=None,file_name:str=None):
		if file_name == None:
			await ctx.response.send_message("لطفا نام فایل را وارد کنید", ephemeral=False)
			return
		if url == None:
			await ctx.response.send_message("لطفا یک لینک وارد کنید", ephemeral=False)
		elif url.split("://")[0].lower() == "http" or url.split("://")[0].lower() == "https":
			#await ctx.response.send_message("به زودی...", ephemeral=True)
			url_format = file_name.split(".")[1]
			if url_format == "html" or url_format == "css" or url_format == "js":
				print(os.system(f"wget {url}"))
				await ctx.response.send_message(file= discord.File(f"./{file_name}"), ephemeral=False)
				print(os.system(f"rm {file_name}"))
			else:
				await ctx.response.send_message("لطفا یک لینک حاوی کد های فرانت-اند وارد کنید", ephemeral=False)
		else:
			await ctx.response.send_message("لطفا یک لینک معتبر وارد کنید", ephemeral=False)
			

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(html_cloner(bot))
    else:
        await bot.add_cog(
                html_cloner(bot),
                guild=discord.Object(id=bot.config["test-server-id"])
            )