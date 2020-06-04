import requests
import os

class downloadError(Exception):
    pass
class unzipError(Exception):
    pass

# Download the file using requests
# google chrome change versions micro versions (which changes the download link too)
# faster than i can write code so it has to find latest micro version for main version
# if that makes any sense...
# Returns the file name that was saved
def downloadFile(version, system):
    baseURL = r'https://chromedriver.storage.googleapis.com/'
    winUrl =  r'chromedriver_win32.zip'
    macURL =  r'chromedriver_mac64.zip'
    linuxURL = r'chromedriver_linux64.zip' 
    fileURLs = {'linux':linuxURL, 'macintosh':macURL, 'windows':winUrl}  # is mac == macintosh?
    fileURL = fileURLs[system]
    s = requests.Session()
    
    print(f"Download File: going for: {fileURL}")
    
    # get the newest micro version
    version = version.split('.')[0]  # general version (eg. 83.x.x.x)  
    print(f"Download File: GET\'ing: {baseURL + 'LATEST_RELEASE_' + version}")
    req = s.get(baseURL + 'LATEST_RELEASE_' + version)
    print('Download File: GET\'ing: https://chromedriver.storage.googleapis.com/LATEST_RELEASE_83')
    version = req.text
    print(f"Latest micro-version: {version}")
    s.get(baseURL + 'index.html?path=' + version + '/')  #  cookies... 
    print(f"Download File: GET\'ing: {baseURL + version + '/' + fileURL}")
    req = s.get(baseURL + version + '/' + fileURL)
    with open(fileURL,'wb') as file:
        file.write(req.content)
        file.close()
    print(f'Saved file: {fileURL}')
    return fileURL  # The file name
# Unzip the file, Return True on Success
def unzipFile(filename):
    return False


# Get system, chrome version and pass to downloadFile()
try:
    print(f"System: {os.name}")
    if os.name == 'nt':
        chromeversion = os.popen('chromeversion.bat').read()
        if "pv    REG_SZ    " in chromeversion:
            chromeversion = chromeversion.split('REG_SZ    ')
            chromeversion = chromeversion[2].replace('\n', '')
            print(f"Chrome Version: {chromeversion}")
            filename = downloadFile(chromeversion, 'windows')
            if filename != None:
                if not(unzipFile(filename)):
                    raise unzipError
            else:
                raise downloadError  # just random different error instead of making a new error class   
    
    else:
        #linux/mac (posix) here
        pass

except downloadError:
    print("Something went wrong!")
    print("Instead of using setup.py you can download the right chrome webdriver for your chrome version from https://chromedriver.chromium.org/downloads and put in the same directory.")
except unzipError:
    print("Something went wrong!")
    print("Please unzip the chrome driver manually")