import os
import sys
import time
import webbrowser

def game_welcome():
    os.system("cls")
    print("\033[32m", end="")
    time.sleep(2)

    print("\n" + "=" * 50)
    print("Welcome to the Game!")
    print("Rule: Answer 'yes' or 'no' to my hot takes. Choose wisely! ")
    print("=" * 50)

    time.sleep(1)
    input("Press ENTER to start the game...")

    RESET = "\033[0m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"

    point = 0

    # Question 1
    while True:
        print(point)
        answer = input("\n1. Is F1(Formula One) the best race or the worst?: ").strip().lower()

        if answer == 'i':
            print(BLUE +  "Opening Wikipedia..." + RESET)
            time.sleep(1)
            webbrowser.open("https://www.google.com/search?q=F1&sca_esv=074237d04407bddc&sxsrf=APpeQnsXYvzH9IqOkQSv3jpEYftOPnsYCw%3A1791907140037&ei=RFXOauTQAZ-W4-EPwP2p-AI&biw=1766&bih=948&uact=5&oq=F1&gs_lp=Egxnd3Mtd2l6LXNlcnAiAkYxMgQQIxgnMgQQIxgnMgoQIxjwBRjJAhgnMg0QLhiABBiKBRhDGLEDMgoQABiABBiKBRhDMgYQABgHGB4yBhAAGAcYHjINEAAYgAQYigUYQxixAzIGEAAYBxgeMgYQABgHGB4yHBAuGIAEGIoFGEMYsQMYlwUY3AQY3gQY4ATYAQJI-wRQpwFYpwFwAXgBkAEAmAGkAqABpAKqAQMyLTG4AQPIAQD4AQGYAgKgArwCwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAhcQLhjcBhi4BhjaBhjYAhjIAxiwA9gBAZgDAIgGAZAGDLoGBAgBGBm6BgYIAhABGBSSBwUxLjMtMaAHkwmyBwMzLTG4B64CwgcDMy0yyAcSgAgB&sclient=gws-wiz-serp#:~:text=Formula%20One%20is%20the%20highest%20class%20of%20worldwide%20racing%20for%20open%2Dwheel%2C%20single%2Dseater%20formula%20racing%20cars%20run%20by%20the%20Formula%20One%20Group%20and%20sanctioned%20by%20the%20F%C3%A9d%C3%A9ration%20Internationale%20de%20l%27Automobile.")

        elif answer == "best":
            point += 1
            print(GREEN + "Correct! F1 is indeed the best race! (+1 point)" + RESET)
            break
        elif answer == "worst":
            point -= 1
            print(RED + "Incorrect! F1 is the best race! (-1 point)" + RESET)
            break
        else:
            print("Invalid input type 'best', 'worst' or 'i' for info")

    # Question 2
    while True:
        os.system("cls")
        print(point)
        answer = input("\n2.Does pizza taste better with pineapple? (yes/no): ").strip().lower()

        if answer == "yes":
            point -=1
            print(RED + "Nah bruh you kidding me? Pineapple on pizza is a crime against humanity! (-1 point)" + RESET)
        elif answer == "no":
            point += 1
            print(GREEN + "Correct! Pineapple on pizza is a crime against humanity! (+1 point)" + RESET)
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

#TODO: Add more questions and scoring logic as needed.