import requests
s = requests.Session()
s.get('https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/')
s.get('https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/')
r = s.get('https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_win32.zip')
with open('chromedriver2.exe','wb') as file:
    file.write(r.content)
    file.close()
print('saved file')