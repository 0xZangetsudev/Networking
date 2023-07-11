import requests
import time

with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

sites_to_check = ["http://books.toscrape.com/", "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"]

counter = 0

for site in sites_to_check:
    for _ in range(5):
        try:
            print(f"Using the proxy: {proxies[counter]}")
            res = requests.get(site, proxies={"http": proxies[counter], "https": proxies[counter]}, timeout=5)
            print(res.status_code)
    
        except requests.exceptions.Timeout:
            print("Request time out")
        except:
            print("Failed")
        finally:
            counter += 1 
            #add line 'counter % len(proxies)' to use modulo if we have more sites_to_check than proxies
