from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from os import system, name

try:
    # Selenium stuff
    chrome_app_data = r'C:\Users\Argen\AppData\Local\Google\Chrome\User Data\Default'
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=' + chrome_app_data)
    options.add_argument('--profile-directory=Default')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    browser.get('https://web.whatsapp.com')
    sleep(5)
except Exception as e:
    if "user data directory is already in use" in str(e):
        print("Please close the brwser previously spawned by the bot")
    exit()

# Clear the screen
def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux os.name is 'posix')
    else:
        _ = system('clear')

# Open a new chat if name is not found in 'recent chats'
def new_chat(user_name):
    # Selecting the new chat search textbox
    new_chat = browser.find_element_by_xpath('//div[@title="New chat"]')
    new_chat.click()

    # Enter the name of chat
    new_user = browser.find_element_by_xpath('//div[@class="_2S1VP copyable-text selectable-text"]')
    new_user.send_keys(user_name)

    sleep(1)

    try:
        # Select for the title having user name
        user = browser.find_element_by_xpath(f'//span[@title="{user_name}"]')
        user.click()
    except NoSuchElementException:
        print(f'User "{user_name}" is not in your contact list')
    except Exception as e:
        # Close the browser
        browser.close()
        print(e)
        exit()

# Main loop asks for user and message and sends message to user
def main():
    bot_prefix = 'WhatsAppBot2.0: '
    user_name = input('enter username (or exit): ')
    while user_name.lower() != 'exit':
        message = bot_prefix + input('enter message: ') + '\n'
        try:
            # Select for the title having user name
            user = browser.find_element_by_xpath(f'//span[@title="{user_name}"]')
            user.click()
        except NoSuchElementException as se:
            new_chat(user_name)

        try:
            # Typing message into message box
            message_box = browser.find_element_by_xpath('//div[@class="_1Plpp"]')
            message_box.send_keys(message)
        except NoSuchElementException as se:
            print(se)

        try:
            clear_screen()
            text = browser.find_elements_by_xpath('//span[@class="_3FXB1 selectable-text invisible-space copyable-text"]')
            for item in text:
                if item.text.startswith(bot_prefix):
                    print(item.text)
                else:
                    print(user_name + ': ' + item.text)

        except NoSuchElementException:
            pass
        # Click on send button (but this was hard to do and adding \n in the message works better)
        # message_box = browser.find_element_by_xpath('//span[@data-icon="send')
        # message_box.click()
        user_name = input('enter username (or exit): ')
    print('Exiting... this might take a few seconds')
    browser.close()

main()
