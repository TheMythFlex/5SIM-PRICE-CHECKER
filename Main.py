import os
import re
import threading
import time

import colorama
import requests
from colorama import Fore
import termcolor
colorama.init()

os.system("title Made by Flex#8629")

s = requests.session()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print(Fore.YELLOW + """


              ███████╗░░░░░░░██████╗██╗███╗░░░███╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
              ██╔════╝░░░░░░██╔════╝██║████╗░████║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
              ██████╗░█████╗╚█████╗░██║██╔████╔██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
              ╚════██╗╚════╝░╚═══██╗██║██║╚██╔╝██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
              ██████╔╝░░░░░░██████╔╝██║██║░╚═╝░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
              ╚═════╝░░░░░░░╚═════╝░╚═╝╚═╝░░░░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                            
                                                            < 5SIM Price Checker > 


""", )

print(Fore.LIGHTYELLOW_EX + "Enter Product: " + Fore.RESET + Fore.LIGHTGREEN_EX, end="")
pro = input()

os.system("title Made by Flex#8629  ✦  Product: {}".format(pro.upper()))

clearConsole()

print(Fore.YELLOW + """


              ███████╗░░░░░░░██████╗██╗███╗░░░███╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
              ██╔════╝░░░░░░██╔════╝██║████╗░████║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
              ██████╗░█████╗╚█████╗░██║██╔████╔██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
              ╚════██╗╚════╝░╚═══██╗██║██║╚██╔╝██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
              ██████╔╝░░░░░░██████╔╝██║██║░╚═╝░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
              ╚═════╝░░░░░░░╚═════╝░╚═╝╚═╝░░░░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

                                                            < 5SIM Price Checker > 

""", )

print(Fore.LIGHTYELLOW_EX + "(Slow/Fast) Mode?: " + Fore.RESET + Fore.LIGHTGREEN_EX, end="")
mode = input().lower()

clearConsole()

os.system("title Made by Flex#8629  ✦  Product: {}  ✦  Mode: {}".format(pro, mode))

print(Fore.YELLOW + """


              ███████╗░░░░░░░██████╗██╗███╗░░░███╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
              ██╔════╝░░░░░░██╔════╝██║████╗░████║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
              ██████╗░█████╗╚█████╗░██║██╔████╔██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
              ╚════██╗╚════╝░╚═══██╗██║██║╚██╔╝██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
              ██████╔╝░░░░░░██████╔╝██║██║░╚═╝░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
              ╚═════╝░░░░░░░╚═════╝░╚═╝╚═╝░░░░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

                                                            < 5SIM Price Checker > 

""", )

def fast():
    global pro
    country = ["Russia", "India", "USA", "Afghanistan", "Albania", "Algeria", "Angola", "Anguilla",
               "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas",
               "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
               "Bosnia and Herzegovina", "Botswana", "Brazil", "Bulgaria", "Burkina faso", "Burundi", "Cambodia",
               "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Chad", "Chile", "China", "Colombia", "Comoros",
               "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cyprus", "Czech", "Djibouti", "Dominica",
               "Dominicana", "Ecuador", "Egypt", "England", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia",
               "Finland", "France", "French Guiana", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
               "Grenada", "Guadeloupe", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
               "Hongkong", "Hungary", "Indonesia", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan",
               "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lesotho", "Liberia", "Lithuania",
               "Luxembourg", "Macau", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mauritania", "Mauritius",
               "Mexico", "Moldova", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar",
               "Namibia", "Nepal", "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria",
               "North Macedonia", "Norway", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru",
               "Philippines", "Poland", "Portugal", "Puerto Rico", "Reunion", "Rwanda", "Saint Kitts and Nevis",
               "Saint Lucia", "Saint Vincent and the Grenadines", "Salvador", "Samoa", "Sao Tome and Principe",
               "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
               "Solomon Islands", "South Africa", "Spain", "Sri Lanka", "Suriname", "Swaziland", "Sweden",
               "Switzerland", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor", "Togo", "Tonga",
               "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks And Caicos", "Uganda", "Ukraine",
               "Uruguay", "USA", "Uzbekistan", "Venezuela", "Vietnam", "Virgin isl.", "Zambia", "Zimbabwe"]
    count = 0
    op = 0
    while True:
        r = s.get("https://5sim.net/v1/guest/prices?country={}&product={}".format(country[int(count)], pro).lower())

        vid = re.findall('"cost":(.*?),', str(r.text))
        print(Fore.RED + "Country" + Fore.RESET + ": " + Fore.YELLOW + str(country[int(count)]).upper() + Fore.RESET,
              end="")
        count += 1
        for videolink in vid[0:4]:
            op += 1
            res = videolink
            print(" [" + Fore.LIGHTMAGENTA_EX + "Operator" + Fore.RESET + "-" + Fore.LIGHTMAGENTA_EX + str(
                op) + ": " + Fore.RESET + "₽:" + Fore.LIGHTGREEN_EX + res + Fore.RESET + "]", end="")
        op = 0
        os.system("title Made by Flex#8629  ✦  Product: {}  ✦  Mode: {}  ✦  Country's: ({}/174)".format(pro, mode, count))
        print("\n")
        if count == 174:
            break
    print(Fore.RED + "Press enter to exit: ", end="")
    input()

def slow():
    country = ["Russia", "India", "USA", "Afghanistan", "Albania", "Algeria", "Angola", "Anguilla",
               "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas",
               "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
               "Bosnia and Herzegovina", "Botswana", "Brazil", "Bulgaria", "Burkina faso", "Burundi", "Cambodia",
               "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Chad", "Chile", "China", "Colombia", "Comoros",
               "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cyprus", "Czech", "Djibouti", "Dominica",
               "Dominicana", "Ecuador", "Egypt", "England", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia",
               "Finland", "France", "French Guiana", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece",
               "Grenada", "Guadeloupe", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
               "Hongkong", "Hungary", "Indonesia", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan",
               "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lesotho", "Liberia", "Lithuania",
               "Luxembourg", "Macau", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mauritania", "Mauritius",
               "Mexico", "Moldova", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar",
               "Namibia", "Nepal", "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria",
               "North Macedonia", "Norway", "Oman", "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru",
               "Philippines", "Poland", "Portugal", "Puerto Rico", "Reunion", "Rwanda", "Saint Kitts and Nevis",
               "Saint Lucia", "Saint Vincent and the Grenadines", "Salvador", "Samoa", "Sao Tome and Principe",
               "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
               "Solomon Islands", "South Africa", "Spain", "Sri Lanka", "Suriname", "Swaziland", "Sweden",
               "Switzerland", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor", "Togo", "Tonga",
               "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks And Caicos", "Uganda", "Ukraine",
               "Uruguay", "USA", "Uzbekistan", "Venezuela", "Vietnam", "Virgin isl.", "Zambia", "Zimbabwe"]
    count = 0
    op = 0
    while True:
        r = s.get("https://5sim.net/v1/guest/prices?country={}&product={}".format(country[int(count)], pro).lower())
        vid = re.findall('"cost":(.*?),', str(r.text))
        print(Fore.RED + "Country" + Fore.RESET + ": " + Fore.YELLOW + str(country[int(count)]).upper() + Fore.RESET,
              end="")
        count += 1
        for videolink in vid[0:4]:
            op += 1
            res = videolink
            print(" [" + Fore.LIGHTMAGENTA_EX + "Operator" + Fore.RESET + "-" + Fore.LIGHTMAGENTA_EX + str(
                op) + ": " + Fore.RESET + "₽:" + Fore.LIGHTGREEN_EX + res + Fore.RESET + "]", end="")
        op = 0
        os.system("title Made by Flex#8629  ✦  Product: {}  ✦  Mode: {}  ✦  Country's: ({}/174)".format(pro, mode, count))
        print("\n")
        time.sleep(1)
        if count == 174:
            break
    print(Fore.RED + "Press enter to exit: ", end="")
    input()



if mode == "fast":
    for i in range(1):
        x = threading.Thread(target=fast)
        x.start()

if mode == "slow":
    for i in range(1):
        x = threading.Thread(target=slow)
        x.start()
