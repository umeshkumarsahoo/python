from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Path to the Brave browser executable
brave_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

# Path to the ChromeDriver executable
chrome_driver_path = "/Users/umesh/Developer/chromedriver"

# Set up Chrome options for Brave
chrome_options = Options()
chrome_options.binary_location = brave_path  # Specify the Brave browser binary location
chrome_options.add_argument("--start-maximized")  # Optional: Start Brave maximized

# Create a Service object
service = ChromeService(executable_path=chrome_driver_path)

# Initialize the WebDriver with Brave and ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to a URL
driver.get("https://chatgpt.com/")

# Optionally, perform more actions or validations here
# link=driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div[2]/div/div/form/div[2]/input')
# print(link.get_attribute("placeholder"))
# Close the driver after use
a=driver.find_element(By.CSS_SELECTOR,'.ProseMirror p')
a.send_keys("english")
a.send_keys(Keys.ENTER)

# for music in list_musics:
#     print(music.text)
driver.quit()
