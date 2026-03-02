from bs4 import BeautifulSoup

miDoc ="""

    <html>
    
    <style>
    77
    <style>
    
    <body>
    <p> Este es el primer parrafo</p>
    <p>Este es el segundo parrafo</>
    </body>
    </html>

"""
soup = BeautifulSoup(miDoc, 'html.parser')

for parrafo in soup.find_all("p"):
    print(parrafo)
    
print(soup)