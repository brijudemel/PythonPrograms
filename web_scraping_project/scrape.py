import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect
parser=argparse.ArgumentParser()
parser.add_argument("--start_page",help="Enter the start page",type=int)
parser.add_argument("--end_page",help="Enter the end page",type=int)
parser.add_argument("--dbname",help="Enter the name of data base",type=str)
args=parser.parse_args()
start=args.start_page
end=args.end_page
connect.connect(args.dbname)
for n in range(start,(end+1)):
	url="http://quotes.toscrape.com/page/{}/".format(n)
	req=requests.get(url)
	content=req.content
	soup=BeautifulSoup(content,"html.parser")
	datas=soup.find_all("div",{"class":"quote"})
	for data in datas:
		quote_dict={}
		quote_dict["quote"]=data.find("span",{"class":"text"}).text
		quote_dict["author"]=data.find("small",{"class":"author"}).text
		connect.insert(args.dbname,tuple(quote_dict.values()))
connect.get_info(args.dbname)

