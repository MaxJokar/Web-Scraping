import requests
from bs4 import BeautifulSoup

res=requests.get("https://webscraper.io/test-sites/e-commerce/allinone") #STATIC WEBSITE
soup=BeautifulSoup(res.content,"html.parser")
items=soup.select("div.thumbnail")
print("===============HELLO & WELCOME TO WEB SCRAPING BY PYTHONG====================================")

print(f"Item counts :{len(items)}")
for item in items:
    # print(item)
      ProductName=item.select("h4>a")[0].text.strip()
      price=item.select("h4.price")[0].text.strip()
      imgSrc=item.select(".img-responsive")[0]['src']
      print(f"Name of Product  :{ProductName}\tPrice :{price}\t Image address:{imgSrc}")
print("=============================THE END ========================================================")
# inWeb1=input("Please Enter the Website you would like to Scape:") DYNAMIC WEBSITE TAKES URL FROM THE USER
# inWeb2=(f"""https://{inWeb1}.com""")        :  URL IS INTIALIZED 
# inWeb3='"'+inWeb2+'"'
# print(inWeb3)
# res=requests.get(inWeb3)


# items=soup.body
# for item in items:
#     print(item)

# print(soup.find_all('img'))   # img  gives the  Tag's name 

# items=soup.select(".img")     #.img gives the Tag's name which their class is ' img ' good for research 
                                                         #based of its Class 
# for item in items:
#     print(item)

# items=soup.select(".img-box")
# print(items)



# items=soup.select("#img")   #Gives the id of 'img'  #=id  id of img is =<main box>
# for item in items:
#     print(item)

# items=soup.select("body")
# for item in items:
#     print(item)

# items=soup.select("li")
# for item in items:
#     print(item)
