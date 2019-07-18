import requests
from bs4 import BeautifulSoup
import smtplib

# The URL of the Amazon UK page you wish to scrape.
URL = '<Amazon-URL>'

# Google 'my user agent' to find your own.
headers = {"User-Agent":
'<Your-User-Agent>'
}

def check_price():
  page = requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')

  # id may be different for your chosen product.
  # 'Inspect' title and price and replace with correct id if needed.
  title = soup.find(id="productTitle").get_text()
  price = soup.find(id="priceblock_dealprice").get_text()
  converted_price = float(price[1:4])

  if(converted_price < 300):
    send_mail()


def send_mail():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('<Your-Gmail-Account>', '<Your-Gmail-Password>')

  subject = 'Price Drop!'
  body = 'Check the link: <Amazon-URL>'

  msg = f"Subject: {subject}\n\n{body} "

  server.sendmail(
    '<Your-Gmail-Account>',
    '<Recipient-Email-Account>,
    msg
  )

  print('Email Sent!')

  server.quit()

  check_price()