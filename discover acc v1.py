import requests
import os
import webbrowser
a = input (f"plases Enter The target : ")
while True:
    os.system ("cls")
    print("--------------------------------------------------------")
    print ("by : vgd6 ") # don't change this plases o_O -------------------------------------
    print ("The target is : " +a)
    print("---------------------")
    print ("1 - take a youtube acc")
    print("---------------------")
    print ("2 - take a TikTok acc")
    print("---------------------")
    print ("3 - take a telegram acc")
    print("------------------------------")
    print ("4 - change a target ")
    print("5 - exit")
    print("-------------------------------------------------------")
    p = input ("choice the you want my brother ! : ")
    if p=="1":
        url = "https://www.youtube.com/@" + a
        print("Checking...")
        try:
            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if r.status_code == 200:
                print("Account found! Opening...")
                webbrowser.open_new_tab(url)
            else:
                print("Account not found.")
        except requests.RequestException:
            print("Connection error.")
        input("Press Enter to continue...")

    elif p=="2":
        url = "https://www.tiktok.com/@" + a
        print("Checking...")
        try:
            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if r.status_code == 200:
                print("Account found! Opening...")
                webbrowser.open_new_tab(url)
            else:
                print("Account not found.")
        except requests.RequestException:
            print("Connection error.")
        input("Press Enter to continue...")

    elif p=="3":
        url = "https://web.telegram.org/k/#@" + a
        print("Checking...")
        try:
            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if r.status_code == 200:
                print("Account found! Opening...")
                webbrowser.open_new_tab(url)
            else:
                print("Account not found.")
        except requests.RequestException:
            print("Connection error.")
        input("Press Enter to continue...")

    elif p=="4":
        a = input (f"plases Enter The target : ").strip()
    elif p=="5":
        print("Bye Bye ! ")
        break