import webbrowser
import time

def open_chrome():
   url = 'www.amazon.com'
   url2 = 'www.google.com'
   browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

   webbrowser.get(browser)
   #You can do webbrowser.open(url, 0) if you want to open in the same window, 1 is a new window, 2 is a new tab. Default behaviour opens them in a new tab anyway.
   #See https://docs.python.org/2/library/webbrowser.html
   for i in range(100):
    webbrowser.open(url) 
   #time.sleep(2) -- Commented this out as I didn't find it neccessary.
   webbrowser.open(url2)

open_chrome()