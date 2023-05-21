import discord
import qrcode
import os
from pathlib import Path
import json

from discord.ext import commands
from discord import Interaction
from discord import app_commands

class button2(discord.ui.View):
	def __init__(self, timeout=180,blob=None,rand_receipt=None):
		super().__init__(timeout=timeout)
		self.blob = blob
		self.rand_receipt = rand_receipt
	
	@discord.ui.button(label="http injector", style=discord.ButtonStyle.green)
	async def button(self, ctx:Interaction, button:discord.ui.Button):
		await ctx.response.send_message("لینک: https://apksos.com/app/com.evozi.injector", ephemeral=True)
	
	@discord.ui.button(label="vpn client pro", style=discord.ButtonStyle.green)
	async def button2(self, ctx:Interaction, button:discord.ui.Button):
		await ctx.response.send_message("لینک:  https://apksos.com/app/it.colucciweb.vpnclientpro", ephemeral=True)

class button(discord.ui.View):
	def __init__(self, timeout=180,blob=None,rand_receipt=None):
		super().__init__(timeout=timeout)
		self.blob = blob
		self.rand_receipt = rand_receipt
		self.injector = []
		self.client_pro = []
		for file in Path("vpn").iterdir():
			file_name = file.name.split(".")[0]
			file_type = file_name.split("-")[0]
			if file_type == "injector":
				self.injector += [discord.File("vpn/" + file.name)]
			if file_type == "client_pro":
				self.client_pro += [discord.File("vpn/" + file.name)]
				
				
	
	@discord.ui.button(label="http injector", style=discord.ButtonStyle.green)
	async def button(self, ctx:Interaction, button:discord.ui.Button):
		if self.injector != []:
			await ctx.response.send_message(files=self.injector, ephemeral=True)
		else:
			await ctx.response.send_message("متاسفانه کانفیگ انجکتور نداریم", ephemeral=True)
	
	@discord.ui.button(label="vpn client pro", style=discord.ButtonStyle.green)
	async def button2(self, ctx:Interaction, button:discord.ui.Button):
		if self.injector != []:
			await ctx.response.send_message("password: Qoqnus-bot",files=self.client_pro, ephemeral=True)
		else:
			await ctx.response.send_message("متاسفانه کانفیگ کلاینت پرو نداریم", ephemeral=True)
	
	@discord.ui.button(label="دانلود برنامه مورد نیاز", style=discord.ButtonStyle.green)
	async def button3(self, ctx:Interaction, button:discord.ui.Button):
		await ctx.response.send_message("کدوم فیلترشکن زو میخای دان کنی:", view=button2(), ephemeral=True)


class vpn(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@app_commands.command(name = "vpn", description = "give u http injector config")
	async def vpn(self, ctx: Interaction):
		await ctx.response.send_message("برای چه برنامه ای کانفیگ میخای:",view=button(),ephemeral=True)

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(vpn(bot))
    else:
        await bot.add_cog(
                vpn(bot),
                guild=discord.Object(id=bot.config["test-server-id"])
            )