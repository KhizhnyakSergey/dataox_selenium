from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import timedelta, datetime
from selenium.webdriver.chrome.options import Options
from math import ceil
from database import Product
from apartment import save_products
from database import SessionLocal
import datetime
from selenium.webdriver.chrome.service import Service


def get_page_data(page, driver):
    url = f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273"
    driver.get(url)
    db = SessionLocal()
    products = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, './/*[@class="clearfix"]')))

    products_data = []
    for product in products:
        product_datum = Product()
        try:
            image = product.find_element(By.XPATH, './/div[@class="image"]/picture/img')
            product_datum.img_src = image.get_attribute("data-src")
        except:
            product_datum.img_src = None

        product_datum.title = product.find_element(By.XPATH, './/*[@class="title"]').text

        pr = product.find_element(By.XPATH, './/*[@class="price"]').text

        if pr == 'Please Contact' or 'Tra' in pr:
            product_datum.currency = None
            product_datum.price = None
        else:
            product_datum.currency = product.find_element(By.XPATH, './/*[@class="price"]').text[:1]
            pr = product.find_element(By.XPATH, './/*[@class="price"]').text[1:]
            product_datum.price = pr.replace(',', '')

        product_datum.location = product.find_element(By.XPATH, './/*[@class="location"]/span').text

        data_str = product.find_element(By.CLASS_NAME, 'date-posted').text
        data_str_split = data_str.split()

        if 'hours' in data_str_split:
            num = int(data_str_split[1])
            data_str = datetime.datetime.now() - timedelta(hours=num)
            dt_posted = data_str.strftime("%d-%m-%Y")
        elif 'minutes' in data_str_split or 'minute' in data_str_split:
            num = int(data_str_split[1])
            data_str = datetime.datetime.now() - timedelta(minutes=num)
            dt_posted = data_str.strftime("%d-%m-%Y")
        else:
            dt_posted = data_str.replace('/', '-')

        product_datum.date_posted = dt_posted
        product_datum.description = product.find_element(By.CLASS_NAME, 'description').text

        try:
            product_datum.bedrooms = product.find_element(By.CLASS_NAME, 'bedrooms').text.split(': ')[-1]
        except:
            product_datum.bedrooms = None

        products_data.append(product_datum)

    save_products(db, products_data)
    print(f'Page {page} success')
    db.close()


def gather_data():
    options = Options()
    options.headless = True
    options.add_argument('window-size=1920x1080')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    web = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"
    s = Service("C:/DataOx/chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)

    # Pagination 1
    driver.get(web)
    pages = driver.find_element(By.CLASS_NAME, 'resultsShowingCount-1707762110').text.split()
    pages_count = ceil(int(pages[5]) / 40)

    for page in range(1, pages_count + 1):
        get_page_data(page, driver)


def main():
    gather_data()


if __name__ == "__main__":
    main()
