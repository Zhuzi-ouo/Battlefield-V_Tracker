User=input ("Enter Your Battlefield V Username:")
import requests
from bs4 import BeautifulSoup

response=requests.get(f"https://battlefieldtracker.com/bfv/profile/origin/{User}/overview")
soup=BeautifulSoup(response.text,"html.parser")
BFVtracker=soup.find_all("span",class_="value")
print ("Kills",BFVtracker[2].string)
print ("Damage",BFVtracker[8].string)
print ("Deaths",BFVtracker[6].string)
print ("Wins",BFVtracker[5].string)
print ("K/D",BFVtracker[1].string)
