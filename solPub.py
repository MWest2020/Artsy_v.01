#! python3
# solPub.py - Launches a address in the browser 
# using an address from the command line or clipboard A web3 webscraper for the Solana Blockchain 

# By Mark Westerweel (Assignment Programming, DT1, HVA Amsterdam)

import webbrowser, sys, pyperclip
# sys.argv is a list.
print(sys.argv)

if len(sys.argv) > 1:
    #Get address from command line
    address = ''.join(sys.argv[1:])

else:
    # Get address from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://explorer.solana.com/address/'+address)
# webbrowser.open('https://explorer.solana.com/address/')


import time
time.sleep(10.0)

import requests, bs4

res = requests.get('https://explorer.solana.com/'+address)
res.raise_for_status()
noStarchSoup  = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)

print(noStarchSoup.body)
# print(noStarchSoup.select('#root'))