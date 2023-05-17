import discord
from discord.ext import commands
import json
from pathlib import Path
import pandas as pd
from on_message import *

limited_guild = []
#data
dadlove = 0
dadlove2 = "تعداد فضولایی که دنبال عشق بابام میگردند: "

Minecrafthale = False

guild_count = 0

chimekhore = 0
chimekhore2 = "تعداد چی مخوره ها: "

Minecraft = 0
Minecraft22 = "تعداد درخواست دانلود ماین: "

fosh = 0
fosh2 = "تعداد فحش دادنا: "

#persion words
chim = "چی مخوره"
chim2 = "چیپس مخوره"
chim3 = "چه مخوره"
Minecraft4 = "ماینکرافت"

Minecraftnames = [
"ماینکرفت",
"ماینکرفتو",
"ماینکرافت",
"ماینکرافتو",
"ماین",
"ماینو",
"ماینم",
"ماینکرفتم",
"ماینکرافتم",
]
Minecraftezafe = [
"نسخه",
"دان",
"دانلود",
"جدید",
"قدیمی",
"قدیمیه",
]
Minecraftnew = [
"نسخه جدید رو از اینجا", 
"<#1076449814889369640>",
"یا اینجا",
"https://madsb10.netlify.app/#download",
"دان کن"
]
bye = [
"بای",
"خداحافظ",
"بایی",
"خدافظ",
]
badword = [
"تخمم",
"کیر",
"کص",
"خایه",
"کیرم",
"گاییدم",
"ساییدم"
"نساییدم",
"نگاییدم",
"کونی",
"کون",
"کصکش",
"کصخل",
"کصشعر",
"کصشر",
"به چپم",
"به راستم",
"میگام",
"میگاد",
"جنده",
"بی ناموس",
"بی ناموص",
"kir",
"kos",
"koon",
"cos",
"coon",
"cir",
]
badword2 = "لطفا مودب باشید"
chekhabar = [
"چه خبر",
"ماهی بات",
]

data = pd.read_csv("allowed_guilds.csv")
allowed_servers = []
for x in data["id"].values:
		allowed_servers += [x]

Version = "v2.2⚙️"


limit = "unlimited ✅"
limit_bool = False

ready = "ready✅"


class Bot(commands.Bot):
	def __init__(self, config):
		
		intent = discord.Intents.default()
		intent.message_content = True
		
		super().__init__(
			command_prefix= "$",
			help_command= None,
			intents= intent,
			application_id = config["aplication-id"]
		)
		
		self.config = config
	
	async def setup_hook(self):
		for file in Path("cogs").glob("*.py"):
			cog_name = file.name.split(".")[0]
			await self.load_extension(f"cogs.{cog_name}")
			print("Loaded extension:  ", file.name)
			
		if self.config["test-server-id"] == "":
			await self.tree.sync()
		else:
			await self.tree.sync(guild= discord.Object(self.config["test-server-id"]))
	
	async def on_ready(self):
		print("Bot is ready")
		guild_count = 0
		for guild in self.guilds:
			guild_count += 1
		global limited_guild
		data = pd.read_csv("allowed_guilds.csv")
		global allowed_servers
		allowed_servers = []
		for x in data["id"].values:
			allowed_servers += [x]
		repeat = 0
		for guild in self.guilds:
			for guild_id in allowed_servers:
				repeat += 1
				if guild_id == guild.id:
					repeat = 0
					break
				elif len(allowed_servers) <= repeat:
					limited_guild += [guild.id]
		guild_count = 0
		guild_member_count = 0
		for guild in self.guilds:
			guild_count += 1
			guild_member_count += guild.member_count
		await self.change_presence(activity=discord.Game(name="Qoqnus bot🤖 | {0} ️| {1} | {2} | watching {3} server and {4} member👀".format(Version, limit, ready, guild_count, guild_member_count)))

	
	async def on_message(self, message):
		guild_count = 0
		guild_member_count = 0
		for guild in self.guilds:
			guild_count += 1
			guild_member_count += guild.member_count
		await self.change_presence(activity=discord.Game(name="Qoqnus bot🤖 | {0} ️| {1} | {2} | watching {3} server and {4} member👀".format(Version, limit, ready, guild_count, guild_member_count)))
		global limited_guild
		global limit_bool
		data = pd.read_csv("allowed_guilds.csv")
		global allowed_servers
		allowed_servers = []
		for x in data["id"].values:
			allowed_servers += [x]
		for y in limited_guild:
			for z in allowed_servers:
				if not message.guild.id == y or not limit_bool or message.guild.id == z:
					if not message.author.id == 1092039637117182053:
						no_react = [
							ancient_netherite.id()
						]
						if message.guild.id in no_react:
							no_react = no_react
						else:
							await message.add_reaction("👀")
						for i in badword:
							if i.lower() in message.content.lower():
								await badwordf(message)
								return
						url_sample = ["https://", "http://"]
						for i in url_sample:
							if i.lower() in message.content.lower():
								await anti_url(message)
								return
						if "http://"in message.content:
							await not_secure_url(message)
						if "سلام"in message.content and "ققنوس بات"in message.content:
							await hello(message)
							return
						if chim in message.content or chim3 in message.content:
							await chimf(message)
							return 
						for i in bye:
							if i in message.content and "ققنوس بات"in message.content:
								await byef(message)
								return 
						for x in Minecraftnames:
							for y in Minecraftezafe:
								if x in message.content and y in message.content:
									await Minecraftfd(message)
									return
						if "اینستا" in message.content and "عادت" in message.content:
							await instaadatf(message)
						if "سایت"in message.content and "ققنوس"in message.content and "کجا"in message.content:
							await website_f(message)
							return
		
	async def on_message_edit(self, message_before, message_after):
			for i in badword:
				if i in message_after.content:
					await badwordf(message_after)
					break
			if "http://"in message_after.content:
				await not_secure_url(message_after)
			
if __name__ == "__main__":
	config = json.loads(open("config.json").read())
	bot = Bot(config)
	bot.run(config["token"])