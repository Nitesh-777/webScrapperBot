from bs4 import BeautifulSoup
import requests 
import pymongo

# url's for amazon pages
url = "https://www.amazon.co.uk/Pepsi-Max-Cans-330ml-Pack/dp/B017NVHSF8?crid=XGKRPQGCIACO&dib=eyJ2IjoiMSJ9.X_w6RayhkiUxLMjK5ANIAA2DgVs6clG9uaSpTUAxaYC2J6cc7Q2mPwr_OWQU1ltoquGrD3DMU53ZfmkM5TfmTU_0HIferjZIV_M72T9xHRjRaQ8n1DS14zEHD4WcAFxrpGuhPvBgjQfcop6mpeLEFg.hUhJ1XadNgJ5xwfOhHC1a-mO0GQ8O8W0ZmCIHpfS8JA&dib_tag=se&keywords=pepsi%2Bmax%2Bcans%2B24pk&nsdOptOutParam=true&qid=1732313851&refinements=p_36%3A800-1000&rnid=355251031&sprefix=pepsi%2Bmax%2B%2Caps%2C77&sr=8-10&th=1"
url2 = "https://www.amazon.co.uk/ring-battery-video-doorbell-diy-wireless-video-doorbell-camera-with-head-to-toe-view-hd-video-easy-to-install-5-min-30-day-free-trial-of-ring-protect/dp/B0BZWQP9Z1?ref=dlx_black_dg_dcl_B0BZWQP9Z1_dt_sl7_97"

# parse HTML content
pepsi_max_24pc_page = requests.get(url)
soup = BeautifulSoup(pepsi_max_24pc_page.text, "html.parser") 


# scrape title
title_elem = soup.select_one('#productTitle')
title = title_elem.text.strip()
print(title)

# scrape rating
rating_elem = soup.select_one('#acrPopover')
rating_text = rating_elem.attrs.get('title')
rating = rating_text.replace('out of 5 stars', '')
print(rating)

# scrape price
price_elem = soup.select_one('span.a-price').select_one('span.a-offscreen')
price = price_elem.text
print(price)

# scrape image
img_elem = soup.select_one('#landingImage')
img = img_elem.attrs.get('src')
print(img)

# scrape description
desc_elem = soup.select_one('#feature-bullets')
desc = desc_elem.text
print(desc)




