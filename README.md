# WhatsAppBot
Simple Python WhatsApp bot using selenium with the chrome webdriver.

Currently it's just a CLI client for whatsapp, no bot functionality yet.

## Install
1. Download the zip  
2. Extract it
3. Run setup.bat  

Alternatively  
```
$ git clone https://github.com/Argentix03/WhatsAppBot.git  
$ pip install -U selenium  
$ pip install -U requests
$ python setup.py
```
Note:  
If setup.py doesnt work you may have to go to https://chromedriver.chromium.org/downloads, download the right webdriver for your chrome/chromium version and put it in the same directory.

## Run
```
$ python bot.py
```

### Notes:
1. First run need to scan the QR code after the browser comes up.  
2. Cannot be run as root  
