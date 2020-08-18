from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url="https://www.flipkart.com/search?q=redmi&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=redmi%7CMobiles&requestId=16c478ac-8e01-41db-abb6-57f44739718c&as-backfill=on"
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"_1UoZlX" })
#print(len(containers))
#print(soup.prettify(containers[0]))
container=containers[0]
#print(container.div.img["alt"])
price=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
#print(Price[0].text)
ratings=container.findAll("div",{"class":"niH0FQ"})
#print(Ratings[0].text)
filename="Product.csv"
f=open(filename,'w')
headers="Product_Name,Pricing,Ratings\n"
f.write(headers)
for container in containers:
    product_name=container.div.img["alt"]

    price_container=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
    price=price_container[0].text.strip()

    rating_container=container.findAll("div",{"class":"niH0FQ"})
    rating=rating_container[0].text

    '''print("product"+product_name)
    print("price"+price)
    print("ratings"+rating)
    '''
    #string parsing for to remove the unnecessary things like offer emi etc
    trim_price=''.join(price.split(','))
    rm_rupees=trim_price.split('₹')
    add_rs_price="Rs."+rm_rupees[1]
    split_price=add_rs_price.split('E')
    final_price=split_price[0]

    split_rating=rating.split(" ")
    final_rating=split_rating[0]

    print(product_name.replace(",","|")+","+final_price+","+final_rating+"\n")
    f.write(product_name.replace(",","|")+","+final_price+","+final_rating+"\n")

f.close()
