import requests
import os
print(f"System: {os.name}")
if os.name == 'nt':
    chromeversion = os.popen('chromeversion.bat').read()
    if "pv    REG_SZ    " in chromeversion:
        chromeversion = chromeversion.split('REG_SZ    ')
        chromeversion = chromeversion[2].replace('\n', '')
        print(f"Chrome Version: {chromeversion}")
        filepath = "https://chromedriver.storage.googleapis.com/" + chromeversion + "/chromedriver_win32.zip"
        os.system(f"curl {filepath} -o chromedriver3.exe")
        print(f"curl {filepath} -o chromedriver3.exe")
else:
    #linux/mac (posix) here
    pass