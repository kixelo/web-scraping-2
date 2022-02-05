#!/usr/bin/env python
# coding: utf-8

# In[382]:


from bs4 import BeautifulSoup
import requests
import pandas

r = requests.get("https://iherb.com/c/sports-accessories")
c = r.content
soup = BeautifulSoup(c, "html.parser")
#print(soup.prettify())
#all = soup.find_all("div", {"class":"product-cell-container col-xs-12 col-sm-12 col-md-8 col-lg-6"})
all = soup.find_all("div", {"class":"panel-stack defer-block"})
all
all[0].find("span", {"class":"price"}).text.replace("\n","")

page_nr=soup.find_all("a", {"class":"pagination-link"})[-1].text.replace("\n","")
page_nr


# In[392]:


l=[]
base_url="https://sk.iherb.com/c/sports-accessories?p="
for page in range(1,int(page_nr)+1,1):
    print(base_url+str(page))
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class":"product-cell-container col-xs-12 col-sm-12 col-md-8 col-lg-6"})
    for item in all:
        d={}
        d["Price"]=item.find("span", {"class":"price"}).text.replace("\n","")
        d["Product name"]=item.find_all("div", {"class":"product-title"})[0].find("bdi").text
        d["Reviews"]=item.find_all("a",{"class":"rating-count"})[0].find("span").text

        l.append(d)


# In[393]:


import pandas
df=pandas.DataFrame(l)
df


# In[394]:


df.to_csv("iherb_scraping.csv")

