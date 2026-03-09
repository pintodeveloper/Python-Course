import pandas as pd
import requests


dates_products = requests.get("https://dummyjson.com/products").json()

#df = pd.read_json('C:\\Users\\andre\\Desktop\\pinto77\\python-course\\pandas\\fichero_covid\\fichero_covid.json')

#print(dates_products.keys())
#print(dates_products.get("products"))


products = pd.DataFrame.from_dict(dates_products.get("products"))


print(products.keys())

print(77)
print("mini mini")