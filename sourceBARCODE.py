import urllib.request
import json
import pprint

api_key = "ocf2icn5x9tu587blclmvhv2xektv1"
url = "https://api.barcodelookup.com/v3/products?barcode=639277387080&formatted=y&key=" + api_key
# url = "https://api.barcodelookup.com/v3/products?barcode=9781874824549&formatted=y&key=" + api_key
# url = "https://api.barcodelookup.com/v3/products?barcode=843603074012&formatted=y&key=" + api_key

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

barcode = data["products"][0]["barcode_number"]
print("Barcode Number: ", barcode, "\n")

name = data["products"][0]["title"]
print("Title: ", name, "\n")

print("Entire Response:")
pprint.pprint(data)
