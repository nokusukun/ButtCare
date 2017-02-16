#Buttcare-ifier by noku
import clipboard
import requests
import sys
import time
import re
import validators
from win10toast import ToastNotifier

toaster = ToastNotifier()
KEY = "bb53b5f779511dc0152ae3cd366714"
API = "http://easy.butt.care/api/v2/action/shorten"


if __name__ == '__main__':
    last = ""
    while True:
        time.sleep(1)
        url = clipboard.paste()

        if validators.url(url) and last != url:
            print("Link Found: {0}".format(url))
            toSend = requests.get(API, {"key" : KEY, "url" : url})

            if validators.url(str(toSend.text)):
                last = str(toSend.text)
                clipboard.copy(str(toSend.text))
                toaster.show_toast("Butts", "Link converted to something more sexy.")
    
    pass

    