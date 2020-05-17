from selenium import webdriver

def test():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    print('Okay, about to launch chromedriver.. fingers crossed')
    driver.get("https://www.google.com/?gws_rd=ssl")  # gets google.com
    driver.set_window_size(1280, 720)
    driver.find_element_by_name("q").click()
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys("cat")
    driver.find_element_by_id("tsf").submit()
    driver.find_element_by_link_text("Images").click()  ## Depending on your language, this will only work on english google!
    print('It has finished')

if __name__ == "__main__":
    test = test()