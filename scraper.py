import requests


# The URL of the website you wish to scrape.
URL = 'https://www.amazon.co.uk/LG-49UK6300PLB-49-Inch-Smart-Freeview/dp/B07BN3RCXW?ref_=Oct_MWishedForC_560864_0&pf_rd_r=YRDE2AH6NBBPWSVNFD9G&pf_rd_p=b0d77b0a-c5e0-5343-8b66-cd36853c24c1&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=560864&pf_rd_m=A3P5ROKL5A1OLE'

# Google 'my user agent' to find your own.
headers = {"User-Agent":
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}