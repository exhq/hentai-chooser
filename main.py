import webbrowser
import random
import time
print("do you want to open the website or just get the link? (y for opening, n for printing)")
print("warning: choosing y will open a new tab in your browser, it might fuck up your ram lol")
x = input("")
while True:
    time.sleep(0.5)
    num = random.randint(0,400000)
    if x == "y":
        webbrowser.open('https://nhentai.net/g/' + str(num))
    else:
        print('https://nhentai.net/g/' + str(num))
