"""

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(...)  # Or Chrome(), or Ie(), or Opera()

# To catch <input type="text" id="passwd" />
password = firefox.find_element(By.ID, "passwd")
# To catch <input type="text" name="passwd" />
password = driver.find_element(By.NAME, "passwd")

password.send_keys("Pa55worD")

driver.find_element(By.NAME, "submit").click()
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

edge_xstyle = "chrome-extension://hncgkmhphmncjohllpoleelnibpmccpj/manage.html"
firefox_xstyle = "moz-extension://fcb928ab-a898-4c47-9f85-2ff701b6e9dc/manage.html"
chrome_xstyle = "chrome-extension://hncgkmhphmncjohllpoleelnibpmccpj/manage.html"
edge_stylus = "chrome-extension://clngdbkpkpeebahjckkjfobafhncgmne/manage.html"
firefox_stylus = "moz-extension://ae95df29-277d-4ee3-aeb6-e4e84dfebada/manage.html"
chrome_stylus = "chrome-extension://clngdbkpkpeebahjckkjfobafhncgmne/edit.html"

# firefox_extensions = "about:debugging#/runtime/this-firefox"
# chrome_extensions = ""
# edge_extensions = ""


# -----------------------------------------------------------------------------------------------------------------------
chrome_opts = ChromeOptions()
chrome_opts.add_argument(r"--user-data-dir=/home/isaac/.config/google-chrome")

chrome = webdriver.Chrome(options=chrome_opts)

chrome.get(chrome_xstyle)
chrome.get(chrome_stylus)

# -----------------------------------------------------------------------------------------------------------------------
edge_opts = EdgeOptions()
edge_opts.add_argument(r"--user-data-dir=/home/isaac/.config/microsoft-edge")
# edge_opts.add_argument(r"--page-load-strategy=none")
# edge_opts.add_argument(r"--accept-insecure-certs=true")

edge = webdriver.Edge(options=edge_opts)

edge.get(edge_xstyle)
edge.get(edge_stylus)

# -----------------------------------------------------------------------------------------------------------------------
firefox_opts = FirefoxOptions()
firefox_opts.add_argument("-profile")
firefox_opts.add_argument("/home/isaac/.mozilla/firefox/uxoqb3lu.default-release")

firefox = webdriver.Firefox(options=firefox_opts)

firefox.get(firefox_xstyle)
firefox.get(firefox_stylus)
