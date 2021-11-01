#! python3
# solScrape.py  - Opens address search results on the Solana blockchain.

from selenium import webdriver
import webbrowser, sys, pyperclip
browser = webdriver.Firefox()
type(browser)

if len(sys.argv) > 1:
    #Get address from command line
    address = ''.join(sys.argv[1:])

else:
    # Get address from the clipboard
    address = pyperclip.paste()
    
browser.get('https://explorer.solana.com/address/'+address)