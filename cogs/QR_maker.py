import discord
import qrcode
import os
import random

from discord.ext import commands
from discord import Interaction
from discord import app_commands

class qr_maker(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@app_commands.command(name = "qr-code-maker", description = "text to qr code")
	async def qr_code(self, ctx: Interaction,text:str=None):
		if text == None:
			await ctx.response.send_message("لطفا جهت ساخت qrcode یک متن وارد کنید")
		else:
			img = qrcode.make(text)
			img_name = random.randint(1000,1000000) + ".png"
			img.save(img_name)
			await ctx.response.send_message(file=discord.File(img_name))
			os.system(f"rm {img_name}")

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(qr_maker(bot))
    else:
        await bot.add_cog(
                qr_maker(bot),
                guild=discord.Object(id=bot.config["test-server-id"])
            )