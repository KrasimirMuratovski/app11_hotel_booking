import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

df = pd.read_csv("articles.csv")

class Article:
	def buy(self, article_id):
		df.loc[df["id"]==article_id,"in stock"] -=1
		df.to_csv("articles.csv", index=False)

print(df)
# print(df.loc[df["id"]==101]["in stock"].squeeze())
# df.loc[df["id"]==101, "in stock"]=50
# print(df.loc[df["id"]==101]["in stock"].squeeze())

article = Article()
article_id = int(input("Enter the article ID: "))
		# df.loc[df["id"]==101]["in stock"].squeeze()
target_amount = df.loc[df["id"]==article_id]["in stock"].squeeze()
if target_amount > 0:
	article.buy(article_id)

name = df.loc[df["id"]==article_id]["name"].squeeze()

price = df.loc[df["id"] == article_id]["price"].squeeze()
price = df.loc[df["id"] == article_id, 'price'].squeeze()
print(name, price)


# df.loc[df["id"] == self.hotel_id, "available"] = "no"
