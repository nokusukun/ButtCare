#Buttcare-ifier by noku
import clipboard
import requests
import sys
import time
import re
import validators
from win10toast import ToastNotifier

toaster = ToastNotifier()
KEY = "heyheresenpai"
API = "http://easy.butt.care/api/v2/action/shorten"


if __name__ == '__main__':
    last = ""
    lastLink = "" #won't re-shorten the last unshortened link.
    while True:
        time.sleep(1)
        url = clipboard.paste() #gets clipboard data

        if validators.url(url) and last != url and lastLink != url:
            print("Link Found: {0}".format(url))
            toSend = requests.get(API, {"key" : KEY, "url" : url})

            if validators.url(str(toSend.text)):
                lastLink = url
                last = str(toSend.text)
                clipboard.copy(str(toSend.text))
                toaster.show_toast("Butts", "Link converted to something more sexy.")
    
    pass

    