import pandas as pd

pd.option_context("display.max_rows", None)
data = pd.read_csv("allowed_guilds.csv")
c = ["name","id","admins","urlch","chn","emoji"]

for i in c:
	print(data[i])
	print("--------------------------")