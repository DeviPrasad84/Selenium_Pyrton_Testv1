from selenium import webdriver

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoqa.com/")
print("new line")
time.sleep(10)
