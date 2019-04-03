from selenium import webdriver
from time import sleep

# PROFILE_PATH = "/home/joseoliveira/.config/google-chrome"
# DRIVER_PATH = "/usr/lib/chromium/chromedriver"
FIREFOX_PATH = "/home/joseoliveira/.mozilla/firefox"


def main():
    # global options
    # options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=" + PROFILE_PATH)
    # global driver
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    fp = webdriver.FirefoxProfile(FIREFOX_PATH)
    driver = webdriver.Firefox(fp)

    url = "https://web.whatsapp.com/"
    driver.get(url)

    input("Log on your WhatsApp Web and press enter when chat opens.")

    driver.close()


if __name__ == "__main__":
    main()
