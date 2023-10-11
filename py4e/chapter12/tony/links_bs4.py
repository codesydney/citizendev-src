import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
position = int(input("Enter position: ")) - 1
count = int(input("Enter count: ")) + 1

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    print("Retrieving:", url)
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    url = tags[position].get("href", None)

# tony@boracay ~/projects/python % python3 links_bs4.py
# Enter URL: http://py4e-data.dr-chuck.net/known_by_Mehraz.html
# Enter position: 18
# Enter count: 7
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Mehraz.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Harleen.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Khelis.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Hirvaansh.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Elisabetta.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Shonagh.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Mohaddesa.html
# Retrieving: http://py4e-data.dr-chuck.net/known_by_Russell.html
