# # Necessary webdrivers ned to be imported
# from selenium import webdriver
# # Get the instance of the webBrowser
# # window, here we are using Chrome
# webBrowser = webdriver.Chrome()
 
# # Lets open google.com in the first tab
# webBrowser.get('http://google.com')
 
# # Lets open https://www.bing.com/ in the second tab
# webBrowser.execute_script("window.open('about:blank','secondtab');")
# webBrowser.switch_to.window("secondtab")
# webBrowser.get('https://www.bing.com/')
 
# # Lets open https://www.facebook.com/ in the third tab
# webBrowser.execute_script("window.open('about:blank','thirdtab');")
# webBrowser.switch_to.window("thirdtab")
# webBrowser.get('https://www.facebook.com/')
# for x in range(1000):
#     webBrowser.execute_script("window.open('about:blank','thirdtab');")
#     webBrowser.switch_to.window("thirdtab")
#     webBrowser.get('https://www.facebook.com/')

# import webbrowser
# from selenium import webdriver
# driver = webdriver.Firefox()
# url = "https://www.example.com"
# url="www.youtube.com"
# for i in range(100):
#     driver.execute_script("window.open('" + url + "','_blank');")
    # subprocess.Popen(['xdg-open', url])

    # webbrowser.open_new_tab(url)
    # webbrowser.open_new_tab(url)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

urls = ["https://www.example1.com", "https://www.example2.com", "https://www.example3.com"]
driver = webdriver.Firefox()
for i in range(600):
    urls.append("https://www.youtube.com")
    print(i)
    driver.execute_script("window.open('" + "https://www.youtube.com" + "','_blank');")
# for url in urls:
#     driver.execute_script("window.open('" + url + "','_blank');")
