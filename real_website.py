from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.daraz.pk/catalog/?q=laptops").text
soup = BeautifulSoup(html_text,'lxml')
laptops = soup.find_all('div', class_='RfADt')

for laptop in laptops:
    company = laptop.find('div', class_='aBrP0')
    price = laptop.find('span', class_='ooOxS')

    if company and price:
        company_name = company.get_text(strip=True)
        price_text = price.get_text(strip=True)

        # Clean the price text → remove commas and "Rs."
        price_value = int(price_text.replace("Rs.", "").replace(",", "").strip())

        # Filter
        if price_value < 100000:
            print(f"Company: {company_name} | Price: {price_value}")
            print(f"company "{company})
