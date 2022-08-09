#Brandon Gustavo Malagon Gonzalez
from urllib import request
import requests as req

resp = req.get("https://www.google.com")
print(resp.text)