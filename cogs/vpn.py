import discord
import qrcode
import os
from pathlib import Path

from discord.ext import commands
from discord import Interaction
from discord import app_commands


class button(discord.ui.View):
	def __init__(self, timeout=180,blob=None,rand_receipt=None):
		super().__init__(timeout=timeout)
		self.blob = blob
		self.rand_receipt = rand_receipt
		self.v2ray = []
		self.ssh = []
		self.other = []
		self.all = []
		for file in Path("vpn").glob("*.ehi"):
			file_name = file.name.split(".")[0]
			is_v2ray = file_name.split("-")[0] == "v2ray"
			is_ssh = file_name.split("-")[0] == "ssh"
			is_other = file_name.split("-")[0] == "other"
			if is_v2ray:
				self.v2ray += [discord.File("./vpn/" + file_name + ".ehi")]
			elif is_ssh:
				self.ssh += [discord.File("./vpn/" + file_name + ".ehi")]
			elif is_other:
				self.other += [discord.File("./vpn/" + file_name + ".ehi")]
			self.all += [discord.File("./vpn/" + file_name + ".ehi")]
	
	@discord.ui.button(label="v2ray", style=discord.ButtonStyle.green)
	async def button(self, ctx:Interaction, button:discord.ui.Button):
		if self.v2ray != []:
			await ctx.response.send_message(files=self.v2ray, ephemeral=True)
		else:
			await ctx.response.send_message("کانفیگ v2ray نداریم", ephemeral=True)
	
	@discord.ui.button(label="ssh", style=discord.ButtonStyle.green)
	async def button2(self, ctx:Interaction, button:discord.ui.Button):
		if self.ssh != []:
			await ctx.response.send_message(files=self.ssh, ephemeral=True)
		else:
			await ctx.response.send_message("کانفیگ ssh نداریم", ephemeral=True)

	@discord.ui.button(label="other | دیگر پروتکل ها", style=discord.ButtonStyle.green)
	async def button3(self, ctx:Interaction, button:discord.ui.Button):
		if self.other != []:
			await ctx.response.send_message(files=self.other, ephemeral=True)
		else:
			await ctx.response.send_message("کانفیگ other نداریم", ephemeral=True)
	
	@discord.ui.button(label="all | همه", style=discord.ButtonStyle.green)
	async def button4(self, ctx:Interaction, button:discord.ui.Button):
		if self.all != []:
			await ctx.response.send_message(files=self.all, ephemeral=True)
		else:
			await ctx.response.send_message("کانفیگ  نداریم", ephemeral=True)
	
	@discord.ui.button(label="click me| منو کلیک کن", style=discord.ButtonStyle.danger)
	async def button5(self, ctx:Interaction, button:discord.ui.Button):
		await ctx.response.send_message("کانفیگ ها برای این برنامه میباشد: https://apksos.com/app/com.evozi.injector", ephemeral=True)
		

class vpn(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@app_commands.command(name = "vpn", description = "give u http injector config")
	async def vpn(self, ctx: Interaction):
		await ctx.response.send_message("یک پروتوکل انتخاب کنید:",view=button(),ephemeral=True)

async def setup(bot):
    if bot.config["test-server-id"] == "":
        await bot.add_cog(vpn(bot))
    else:
        await bot.add_cog(
                vpn(bot),
                guild=discord.Object(id=bot.config["test-server-id"])
            )