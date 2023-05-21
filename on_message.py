import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import check
import ast
import pandas as pd
import random

def data_csv():
	data = pd.read_csv("allowed_guilds.csv")
	return data

class allowed_guilds:
	def __init__(self, num):
		self.num = num
	def id(self):
		data = pd.read_csv("allowed_guilds.csv")
		arr = data["id"].values
		return int(arr[self.num])
	def admin(self, admin_num):
		data = pd.read_csv("allowed_guilds.csv")
		arr = data["admins"].values
		return int(arr[self.num].split()[admin_num])
	def urlch(self, chnum):
		data = pd.read_csv("allowed_guilds.csv")
		arr = data["urlch"].values
		return int(arr[self.num].split()[chnum])
	def chid(self, id):
		data = pd.read_csv("allowed_guilds.csv")
		arr = data["chn"].values
		return int(arr[self.num].split()[id])
	def ch_welcome(self):
		data = pd.read_csv("allowed_guilds.csv")
		arr = data["ch_welcome"]
		return int(arr[self.num])


class vip_guilds(allowed_guilds):
	def emoji(self, id):
		data = pd.read_csv("allowed_guilds.csv")
		arr = data["emoji"]
		return int(arr[self.num].split()[id])


#special guilds or guilds admin
Qoqnus_master = vip_guilds(2)
amir_fire = allowed_guilds(3)
mahdi_designer = allowed_guilds(4)
madsb10 = allowed_guilds(1)
ancient_netherite = vip_guilds(5)
programming_forum = vip_guilds(6)

ad_list = [
	[
		"『𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗶𝗻𝗴 𝗙𝗼𝗿𝘂𝗺』",
		"\n",
		"\n"
		"╗ 🧑‍💻  دارای فروم برای رفع باگ های کداتون تو هر زبان برنامه‌نویسی 🔥",
		"╣  📰  اخبار به روز تکنولوژی 🔥",
		"╣ 🎮  رفع مشکل تو کد زدن تو ماینکرفت یا مود سازی تو ماینکرفت 🔥",
		"╣ 💻 کد های متن باز **جذاااااب** 🔥",
		"╝ 🌐 فیلترشکن نابییی همیشه وصل 🔥",
		"\n",
		"پس منتظر چی نشستی 😐",
		"👇 زود تر جوین شو 👇",
		"〘 https://discord.gg/VArrJDPvDK 〙",
	],
]

Vip = [
Qoqnus_master.id(),
ancient_netherite.id(),
programming_forum.id(),
]


async def ad_f(msg):
	global ad_list
	global Vip
	for i in Vip:
		if msg.guild.id == i:
			return
	ad = random.sample(ad_list, 1)[0]
	ad2 = ""
	for i in ad:
		ad2 += i
		ad2 += "\n"
	await msg.channel.send(ad2 + "\n" + "تبلیغات ققنوس بات 👆👆\n برای غیر فعال کردن به سرور ققنوس مستر مراجعه کنید https://Qoqnus-master.netlify.app")


async def hello(msg):
	if msg.author.id == madsb10.admin(0):
		await msg.reply("سلام خاله دینا ❤️🙂")
	elif msg.author.id == Qoqnus_master.admin(0) and msg.guild.id != programming_forum.id():
		await msg.reply("سلام بابا جونم❤️❤️")
	elif msg.author.id == Qoqnus_master.admin(0) and msg.guild.id == programming_forum.id():
		await msg.reply("سلام به ققنوس مستر🔥🔥👋")
	elif msg.author.id == amir_fire.admin(0):
		await msg.reply("سلام امیر😊❤️")
	elif msg.author.id == mahdi_designer.admin(0):
		await msg.reply("سلام مهدی جون❤️❤️")
	elif msg.author.id == 1089845349436375040: #fire bot
		await msg.reply("سلام ف.ایر بات")
	elif msg.author.id == 1090624303059451924 and msg.guild.id == Qoqnus_master.id(): #ancient netherite
		await msg.reply("سلام به ندرایت گودرتی🗿🤌")
	elif msg.author.id == 1090624303059451924 and msg.guild.id == programming_forum.id():
		await msg.reply("سلام بر برنامه‌نویس گودرتمند باستانی 🔥🔥")
	else:
		await msg.reply("سلام کاربر عزیز")
	await ad_f(msg)


async def byef(msg):
	if msg.author.id == madsb10.admin(0):
		await msg.reply("باییی خاله دینا ❤️🙂")
	elif msg.author.id == Qoqnus_master.admin(0) and msg.guild.id != programming_forum.id():
		await msg.reply("بای بابا جونم❤️❤️")
	elif msg.author.id == Qoqnus_master.admin(0) and msg.guild.id == programming_forum.id():
		await msg.reply("خداحافظ ققنوس مستر🔥👋")
	elif msg.author.id == amir_fire.admin(0):
		await msg.reply("بای امیر😊❤️")
	elif msg.author.id == mahdi_designer.admin(0):
		await msg.reply("بایی مهدی❤️❤️")
	elif msg.author.id == 1090624303059451924 and msg.guild.id == Qoqnus_master.id(): #ancient netherite
		await msg.reply("بای ندرایت گودرتی 🗿")
	elif msg.author.id == 1090624303059451924 and msg.guild.id == programming_forum.id():
		await msg.reply("خداحافظ بر برنامه‌نویسی گودرتمند باستانی 🔥🔥")
	else:
		await msg.reply("خداحافظ کاربر عزیز")
	await ad_f(msg)


async def chimf(msg):
	if False:
		return
	else:
		await msg.reply("چیپس مخوره🍿")
	await ad_f(msg)


async def Minecraftfd(msg):
	if msg.guild.id == mahdi_designer.id:
		await msg.reply("ماین کرفت جدیدو از اینجا دان کن \n  <#929388674783805470>")
	else:
		await msg.reply("از اینجا ماین جدیدو دان کن\n https://Qoqnus-master.netlify.app/#download")
	await ad_f(msg)


async def anti_url(msg):
	data = pd.read_csv("allowed_guilds.csv")
	urlch = data["urlch"]
	urlch2 = []
	for i in urlch:
		urlch3 = i.split()
		for y in urlch3:
			if not y == '0':
				urlch2 += [int(y)]
	if msg.channel.id in urlch2:
			await msg.delete()
			await msg.channel.send("<@{0}> ارسال لینک در این کانال از این سرور ممنوع است".format(msg.author.id))


async def badwordf(msg):
		if False:
			return
		elif msg.channel.id == 1107614713791119391: #programming_forum technology-news
			return
		else:
			await msg.delete()
			await msg.channel.send("<@{0}> لطفا مودب باشید".format(msg.author.id))


async def instaadatf(msg):
	this = "اینو بفرست برا سومین نفر شیرت بهش درخواست ازدواج بده💩 \n نخوام ازدواج کنم باید کیو ببینم🤧🤧😐"
	#await msg.reply(this)
	#await ad_f(msg)
	return


async def firebot_hi_f(msg):
	if msg.author.id == Qoqnus_master.admin(0) :
		await msg.channel.send("سلام فایر بات 😊❤️")
	await ad_f(msg)


async def not_secure_url(msg):
	if msg.channel.id == Qoqnus_master.chid(0): #mahi bot test
		return
	else:
		await msg.delete()
		await msg.channel.send("<@{0}>این سایت فاقد گواهیssl میباشد لطفا از سایت های دارای https که گواهی ssl دارند و ایمن هستند استفاده کنید".format(msg.author.id))


async def website_f(msg):
	embed = discord.Embed()
	embed.set_image(url='https://qoqnus-master.netlify.app/logo.jpg')
	embed.add_field(name="سایت ققنوس مستر", value="https://Qoqnus-master.netlify.app/")
	await msg.reply(embed= embed)

async def welcome_f(member, client):
	print("khanda makeny??")
	print(member.guild.id)
	if member.guild.id == Qoqnus_master.id():
		embed_welcome = discord.Embed()
		embed_welcome.add_field(name="خوش اومدی😊❤️", value="<@{0}> به سرور ققنوس مستر خوش اومدی".format(member.id))
		channel_welcome = client.get_channel(Qoqnus_master.ch_welcome())
		await channel_welcome.send(embed=embed_welcome)

