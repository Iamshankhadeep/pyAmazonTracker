import requests
from bs4 import BeautifulSoup
import smtplib

URL="https://www.amazon.in/Apple-MacBook-13-inch-1-4GHz-Quad-core/dp/B07V2GVWKK/ref=sr_1_10?keywords=macbook&qid=1567091024&s=gateway&sr=8-10"

headers={"User-Agent":
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}

def check_price():

    page= requests.get(URL,headers=headers)

    soup= BeautifulSoup(page.content,"html.parser")

    title= soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    cov_price =float(price[2:13].replace(",",''))
    if(cov_price<120000):
        send_email()
    print(cov_price)


def send_email():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("from_where_emailId",'your_password')
    sub="Price fell down"
    body=" check the link https://www.amazon.in/Apple-MacBook-13-inch-1-4GHz-Quad-core/dp/B07V2GVWKK/ref=sr_1_10?keywords=macbook&qid=1567091024&s=gateway&sr=8-10"
    msg = f"Subject: {sub}\n\n {body}"
    server.sendmail("from_where_emailId",
        "to_where_emailId",msg)
    print("email sent")

check_price()