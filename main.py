from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("https://yoursite.com")

title=driver.title
title


links = driver.find_elements(By.TAG_NAME, "a")
links

all_links = [link.get_attribute('href') for link in links]
filtered_links = [link for link in all_links if link is not None and not link.endswith((".com", ".com/", "/home", "/sitemap", "/.xml", "/feed.xml"))]
filtered_links = [link for link in filtered_links if link.startswith("https://yoursite.com/") and not any(word in link for word in ["login", "signup", "sign-up", "auth"])]
filtered_links = list(set(filtered_links))
filtered_links

scraped_bodies = []
for link in filtered_links:
    driver.get(link)
    time.sleep(10)
    body2 = driver.find_element(By.TAG_NAME, "body")
    body_text = body2.text
    scraped_bodies.append(body_text)
    print("body.............", body_text)



