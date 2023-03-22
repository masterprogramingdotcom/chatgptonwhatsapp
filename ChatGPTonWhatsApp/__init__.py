from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import openai
import os
import time

class ChatGPTonWhatsApp:
    def start(ChatGPT_API_KEY):
        home_dir = os.path.expanduser("~")
        # Construct the path to the Chrome user data directory based on the operating system
        if os.name == "nt":  # Windows
            chrome_data_dir = os.path.join(home_dir, "AppData", "Local", "Google", "Chrome", "User Data", "Default")
        else:  # Unix-like
            chrome_data_dir = os.path.join(home_dir, ".config", "google-chrome", "Default")

        options = Options()
        options.add_argument(f"--user-data-dir={chrome_data_dir}")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument("--disable-extensions")
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu/')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument("--log-level=3")
        options.add_argument('--hide-scrollbars')
        options.add_argument("--disable-popup-blocking")
        options.add_argument('window-size=0x0')
        # options.add_argument('--headless=new')
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        options.add_experimental_option("useAutomationExtension",False)

        browser = webdriver.Chrome(options=options)
        user_agent = browser.execute_script("return navigator.userAgent;")
        browser.get('https://web.whatsapp.com/')
        browser.maximize_window()
        options.add_argument('--user-agent={}'.format(user_agent))

        def find_mess():
            soup = BeautifulSoup(browser.page_source, "html.parser")
            for i in soup.find_all("div", class_="message-in"):
                message = i.find("span", class_="selectable-text")
                num = i.find_all("span")[2]
                if message:
                    message2 = message.find("span").text

            num = i.find_all("span")[2]
            number = str(num)
            number = number[18:33]
            return message2,number

        def reply(ans):
            reply = browser.find_elements(By.XPATH,'//div[@title="Type a message"]')[0]
            reply.send_keys(ans)
            try:
                if reply != '':
                    wait = WebDriverWait(browser, 5)
                    element = wait.until(EC.element_to_be_clickable((By.XPATH,'//span[@data-icon="send"]')))
                    element.click()
                    print(f"ChatGPT - {ans}" + '\n')

                time.sleep(2)
                reset = browser.find_elements(By.XPATH, '//*[@id="pane-side"]')[0]
                reset.click()

            except Exception as e:
                pass

        while True:
            try:
                wait = WebDriverWait(browser, 12)
                element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME ,'_1pJ9J')))
                element.click()

                message2,number = find_mess()

                if number != " selectable-tex" and number != 'v" role="button':
                    print(f"{number.replace('></span','')} - {message2} ","user")

                if number == 'v" role="button':
                    print(f"Group - {message2} ","user")
                
                try:
                    openai.api_key = ChatGPT_API_KEY
                    try:
                        response = openai.Completion.create(
                            model="text-davinci-003",
                            prompt=f"Replay To This :\n\n{message2}\n\n1.",
                            temperature=0.5,
                            max_tokens=1000,
                            top_p=1,
                            frequency_penalty=0,
                            presence_penalty=0
                        )
                        
                        results = response['choices'][0]['text'].strip()
                        reply(results)
                        reset = browser.find_elements(By.XPATH, '//*[@id="pane-side"]')[0]
                        reset.click()

                    except Exception:
                        reset = browser.find_elements(By.XPATH, '//*[@id="pane-side"]')[0]
                        reset.click()
                except Exception:
                    reset = browser.find_elements(By.XPATH, '//*[@id="pane-side"]')[0]
                    reset.click()
                    print("ChatGPT is Not Working")
            except Exception as e:
                # print("Not Found ")
                pass
