from selenium import webdriver


def test_get_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    driver.quit()


def test_get_facebook():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    driver.quit()


def test_get_ezball():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ezball9.live/")
    driver.quit()


def test_get_rophim():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.rophim.org/")
    driver.quit()


def test_get_chatgpt():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://chat.openai.com/chat")
    driver.quit()


def test_get_grok():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://grok.com/")
    driver.quit()


def test_get_github():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://github.com/")
    driver.quit()