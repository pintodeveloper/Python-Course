import requests

miReq = requests.get("https://ufpso.edu.co/")

#print(miReq.status_code)

#print(miReq.headers)

# Me quede sin datos


print(miReq.text)

